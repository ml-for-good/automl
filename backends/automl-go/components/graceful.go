/*
* origin: https://github.com/tylerb/graceful/tree/v1.2.4
 */
package components

import (
	"crypto/tls"
	"log"
	"net"
	"net/http"
	"os"
	"sync"
	"time"

	"golang.org/x/net/netutil"
)

// Server wraps an http.Server with graceful connection handling.
// It may be used directly in the same way as http.Server, or may
// be constructed with the global functions in this package.
//
// Example:
//	srv := &graceful.Server{
//		Timeout: 5 * time.Second,
//		Server: &http.Server{Addr: ":1234", Handler: handler},
//	}
//	srv.ListenAndServe()
type Server struct {
	*http.Server

	// Timeout is the duration to allow outstanding requests to survive
	// before forcefully terminating them.
	Timeout time.Duration

	// Limit the number of outstanding requests
	ListenLimit int

	// ConnState specifies an optional callback function that is
	// called when a client connection changes state. This is a proxy
	// to the underlying http.Server's ConnState, and the original
	// must not be set directly.
	ConnState func(net.Conn, http.ConnState)

	// BeforeShutdown is an optional callback function that is called
	// before the listener is closed.
	BeforeShutdown func()

	// ShutdownInitiated is an optional callback function that is called
	// when shutdown is initiated. It can be used to notify the client
	// side of long lived connections (e.g. websockets) to reconnect.
	ShutdownInitiated func()

	// NoSignalHandling prevents graceful from automatically shutting down
	// on SIGINT and SIGTERM. If set to true, you must shut down the server
	// manually with Stop().
	NoSignalHandling bool

	// stopLock is used to protect against concurrent calls to Stop
	stopLock sync.Mutex

	// stopChan is the channel on which callers may block while waiting for
	// the server to stop.
	stopChan chan struct{}

	// chanLock is used to protect access to the various channel constructors.
	chanLock sync.RWMutex

	// connections holds all connections managed by graceful
	connections map[net.Conn]struct{}

	// notify shut down channel
	shutdownChan chan bool

	// notify done channel
	doneChan chan bool

	// notify kill channel
	killChan chan bool

	// target address
	addr string
}

// Run serves the http.Handler with graceful shutdown enabled.
//
// timeout is the duration to wait until killing active requests and stopping the server.
// If timeout is 0, the server never times out. It waits for all active requests to finish.
func Run(addr string, waitTimeout, readTimeout, writeTimeout time.Duration, n http.Handler) {
	srv := &Server{
		Timeout: waitTimeout,
		Server: &http.Server{
			Addr:         addr,
			Handler:      n,
			ReadTimeout:  readTimeout,
			WriteTimeout: writeTimeout,
		},
		shutdownChan: make(chan bool),
		doneChan:     make(chan bool),
		killChan:     make(chan bool),
	}

	if err := srv.ListenAndServe(); err != nil {
		if opErr, ok := err.(*net.OpError); !ok || (ok && opErr.Op != "accept") {
			logger := log.New(os.Stdout, "[graceful] ", 0)
			logger.Fatal(err)
		}
	}

}

// ListenAndServe is equivalent to http.Server.ListenAndServe with graceful shutdown enabled.
//
// timeout is the duration to wait until killing active requests and stopping the server.
// If timeout is 0, the server never times out. It waits for all active requests to finish.
func ListenAndServe(server *http.Server, timeout time.Duration) error {
	srv := &Server{Timeout: timeout, Server: server}
	return srv.ListenAndServe()
}

// ListenAndServe is equivalent to http.Server.ListenAndServe with graceful shutdown enabled.
func (srv *Server) ListenAndServe() error {
	// Create the listener so we can control their lifetime
	addr := srv.Addr
	if addr == "" {
		addr = ":http"
	}
	l, err := net.Listen("tcp", addr)
	if err != nil {
		return err
	}

	return srv.Serve(l)
}

// ListenAndServeTLS is equivalent to http.Server.ListenAndServeTLS with graceful shutdown enabled.
//
// timeout is the duration to wait until killing active requests and stopping the server.
// If timeout is 0, the server never times out. It waits for all active requests to finish.
func ListenAndServeTLS(server *http.Server, certFile, keyFile string, timeout time.Duration) error {
	srv := &Server{Timeout: timeout, Server: server}
	return srv.ListenAndServeTLS(certFile, keyFile)
}

// ListenTLS is a convenience method that creates an https listener using the
// provided cert and key files. Use this method if you need access to the
// listener object directly. When ready, pass it to the Serve method.
func (srv *Server) ListenTLS(certFile, keyFile string) (net.Listener, error) {
	// Create the listener ourselves so we can control its lifetime
	addr := srv.Addr
	if addr == "" {
		addr = ":https"
	}

	config := &tls.Config{}
	if srv.TLSConfig != nil {
		*config = *srv.TLSConfig
	}
	if config.NextProtos == nil {
		config.NextProtos = []string{"http/1.1"}
	}

	var err error
	config.Certificates = make([]tls.Certificate, 1)
	config.Certificates[0], err = tls.LoadX509KeyPair(certFile, keyFile)
	if err != nil {
		return nil, err
	}

	conn, err := net.Listen("tcp", addr)
	if err != nil {
		return nil, err
	}

	tlsListener := tls.NewListener(conn, config)
	return tlsListener, nil
}

// ListenAndServeTLS is equivalent to http.Server.ListenAndServeTLS with graceful shutdown enabled.
func (srv *Server) ListenAndServeTLS(certFile, keyFile string) error {
	l, err := srv.ListenTLS(certFile, keyFile)
	if err != nil {
		return err
	}

	return srv.Serve(l)
}

// ListenAndServeTLSConfig can be used with an existing TLS config and is equivalent to
// http.Server.ListenAndServeTLS with graceful shutdown enabled,
func (srv *Server) ListenAndServeTLSConfig(config *tls.Config) error {
	addr := srv.Addr
	if addr == "" {
		addr = ":https"
	}

	conn, err := net.Listen("tcp", addr)
	if err != nil {
		return err
	}

	tlsListener := tls.NewListener(conn, config)
	return srv.Serve(tlsListener)
}

// Serve is equivalent to http.Server.Serve with graceful shutdown enabled.
//
// timeout is the duration to wait until killing active requests and stopping the server.
// If timeout is 0, the server never times out. It waits for all active requests to finish.
func Serve(server *http.Server, l net.Listener, timeout time.Duration) error {
	srv := &Server{Timeout: timeout, Server: server}
	return srv.Serve(l)
}

// Serve is equivalent to http.Server.Serve with graceful shutdown enabled.
func (srv *Server) Serve(listener net.Listener) error {

	if srv.ListenLimit != 0 {
		listener = netutil.LimitListener(listener, srv.ListenLimit)
	}

	// Track connection state
	add := make(chan net.Conn)
	remove := make(chan net.Conn)

	srv.Server.ConnState = func(conn net.Conn, state http.ConnState) {
		switch state {
		case http.StateNew:
			add <- conn
		case http.StateClosed, http.StateHijacked:
			remove <- conn
		}
		if srv.ConnState != nil {
			srv.ConnState(conn, state)
		}
	}

	go srv.manageConnections(add, remove)

	interruptSignal := RegisterInterruptSignal("graceful net", false)
	go srv.handleInterrupt(interruptSignal, listener)

	// Serve with graceful listener.
	// Execution blocks here until listener.Close() is called, above.
	err := srv.Server.Serve(listener)

	srv.shutdown(interruptSignal)

	return err
}

// StopChan gets the stop channel which will block until
// stopping has completed, at which point it is closed.
// Callers should never close the stop channel.
func (srv *Server) StopChan() <-chan struct{} {
	srv.chanLock.Lock()
	if srv.stopChan == nil {
		srv.stopChan = make(chan struct{})
	}
	srv.chanLock.Unlock()
	return srv.stopChan
}

func (srv *Server) manageConnections(add, remove chan net.Conn) {
	srv.connections = map[net.Conn]struct{}{}
	isDone := false
	for {
		select {
		case conn := <-add:
			srv.connections[conn] = struct{}{}
		case conn := <-remove:
			delete(srv.connections, conn)
			if isDone && len(srv.connections) == 0 {
				srv.doneChan <- true
				return
			}
		case <-srv.shutdownChan:
			isDone = true
			if len(srv.connections) == 0 {
				srv.doneChan <- true
				return
			}
		case <-srv.killChan:
			for k := range srv.connections {
				_ = k.Close() // nothing to do here if it errors
			}
			return
		}
	}
}

func (srv *Server) handleInterrupt(interruptSignal *OverallSignal, listener net.Listener) {
	(*interruptSignal).Wait()

	listener.Close() // we are shutting down anyway. ignore error.
	srv.SetKeepAlivesEnabled(false)
}

func (srv *Server) shutdown(interruptSignal *OverallSignal) {
	// Request done notification
	srv.shutdownChan <- true

	if srv.Timeout > 0 {
		select {
		case <-srv.doneChan:
		case <-time.After(srv.Timeout):
			close(srv.killChan)
		}
	} else {
		<-srv.doneChan
	}
	// Close the stopChan to wake up any blocked goroutines.
	srv.chanLock.Lock()
	if srv.stopChan != nil {
		close(srv.stopChan)
	}
	srv.chanLock.Unlock()
	(*interruptSignal).Done()
}

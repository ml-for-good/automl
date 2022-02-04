import axios, { AxiosPromise, AxiosRequestConfig } from 'axios';

function httpRequest(axiosConfig: AxiosRequestConfig): AxiosPromise {
  const service = axios.create({
    // baseURL: 'https://some-domain.com/api/',
    // timeout: 1000,
    // headers: {'X-Custom-Header': 'foobar'}
  });

  // request interceptor
  service.interceptors.request.use(
    config => {
      return config;
    }, 
    error => {
      return Promise.reject(error);
    }
  );

  // response interceptor
  service.interceptors.response.use(
    response => response.data,
    error => {
      return Promise.reject(error);
    }
  );

  return service(axiosConfig)
}

export default httpRequest;

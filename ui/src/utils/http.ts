import axios from 'axios'

export const axiosInstance = axios.create({
  // baseURL: 'https://some-domain.com/api/',
  // timeout: 1000,
  // headers: {'X-Custom-Header': 'foobar'}
})

// request interceptor
axiosInstance.interceptors.request.use(
  config => config, 
  error => Promise.reject(error)
)

// response interceptor
axiosInstance.interceptors.response.use(
  response => response.data,
  error => Promise.reject(error)
)

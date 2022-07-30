import axios from 'axios';
import { config } from "../Constants";

export const automlApi = {
  getHello,
	getSample,
	getDashboard,
}

function getHello() {
  return instance.get('/hello')
}

function getSample(token) {
	return instance.get('/sample', 
		{
			headers: {
				'Authorization': bearerAuth(token),
			}
		}
	);
}

function getDashboard(token) {
	console.log(token);
	return instance.get('/dashboard', 
		{
			headers: {
				'Authorization': bearerAuth(token),
			}
		}
	);
}

// axios related
const instance = axios.create({
	baseURL: config.url.API_BASE_URL,
})

instance.interceptors.response.use(response => {
	return response;
}, function (error) {
	if (error.response.status === 404) {
		return { status: error.response.status };
	}
	return Promise.reject(error.response);
});

// -- Helper functions

function bearerAuth(token) {
	return `Bearer ${token}`
}

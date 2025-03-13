import axios from 'axios'

const apo = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/' , // URL da API Django
});

export default api;
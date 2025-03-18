import axios from "axios"

// Used in the middleware to forward the local proxy requests to the backend
export const baseApiUrl = "http://localhost:8085"

const api = axios.create({
    baseURL: baseApiUrl,
})

export default api


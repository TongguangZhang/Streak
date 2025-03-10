import axios from "axios"

const isServer = typeof window === "undefined"

// Used in the middleware to forward the local proxy requests to the backend
export const baseApiUrl = "http://localhost:8085"

// Proxied url that sends requests through the middleware, requests from the middleware cannot use the local proxy and must be sent to the backend directly
export const localProxyUrl = "http://localhost:3000/api"
const api = axios.create({
    baseURL: baseApiUrl,
})

export default api


import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

// Use the environment variable with a fallback to localhost:8000
const baseUrl = import.meta.env.VITE_API_BASE_URL;

export const emptySplitApi = createApi({
  baseQuery: fetchBaseQuery({ baseUrl, credentials: "include" }),
  endpoints: () => ({}),
});
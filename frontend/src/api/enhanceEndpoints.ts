import { api } from "../api/apiStore.gen";

export const enhancedAPI = api.enhanceEndpoints({
    addTagTypes: ["Project"],
    endpoints: {
        readProjectsProjectsGet: {
            providesTags: ["Project"]
        },
        createProjectProjectsPost: {
            invalidatesTags: ["Project"]
        }
    },
});
import { api } from "../api/apiStore.gen";

export const enhancedAPI = api.enhanceEndpoints({
    addTagTypes: ["Project", "Nodes", "Sets", "Edges"],
    endpoints: {
        projectsList: {
            providesTags: ["Project"]
        },
        projectsCreate: {
            invalidatesTags: ["Project"]
        },
        objectsCreate: {
            invalidatesTags: ["Nodes", "Sets"]
        },
        nodesDestroy: {
            invalidatesTags: ["Nodes", "Sets", "Edges"]
        },
        edgesCreate: {
            invalidatesTags: ["Edges"]
        },
        edgesList: {
            providesTags: ["Edges"]
        },
        setsList: {
            providesTags: ["Sets"]
        },
        nodesList: {
            providesTags: ["Nodes"]
        }
    },
});
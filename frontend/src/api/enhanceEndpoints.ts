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
        nodesDestroy: {
            invalidatesTags: ["Nodes", "Sets", "Edges"]
        },
        nodesCreate: {
           invalidatesTags: ["Nodes", "Sets", "Edges"] 
        },
        nodesPartialUpdate: {
            invalidatesTags: ["Nodes", "Sets"]
        },
        edgesCreate: {
            invalidatesTags: ["Edges"]
        },
        propertiesPartialUpdate: {
            invalidatesTags: ["Sets"]
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
import { api } from "../api/apiStore.gen";

export const enhancedAPI = api.enhanceEndpoints({
    addTagTypes: ["Project", "Nodes", "Sets", "Edges", "Controllers", "Weather"],
    endpoints: {
        projectsList: {
            providesTags: ["Project"]
        },
        projectsDestroy: {
            invalidatesTags: ["Project"]
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
            invalidatesTags: ["Sets", "Nodes", "Controllers"]
        },
        edgesList: {
            providesTags: ["Edges"]
        },
        setsList: {
            providesTags: ["Sets"]
        },
        nodesList: {
            providesTags: ["Nodes"]
        },
        controllersPartialUpdate: {
            invalidatesTags: ["Nodes", "Controllers", "Sets", "Weather"]
        },
        controllersRetrieve: {
            providesTags: ["Controllers"]
        },
        weatherDataPartialUpdate: {
            invalidatesTags: ["Weather", "Nodes", "Sets"]
        },
        weatherDataRetrieve: {
            providesTags: ["Weather"]
        },
    },
});
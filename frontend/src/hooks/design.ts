import { EdgeRead, NodeRead, PropertySetRead, useEdgesListQuery, useNodesListQuery, useSetsListQuery } from "@/api/apiStore.gen";
import { useProjectId } from "./project";


export function useNodes(){
    const projectID = useProjectId();
    const {data: nodes} = useNodesListQuery({projectId: projectID});
    return nodes as NodeRead[]
}

export function usePropertySets(){
    const projectID = useProjectId();
    const {data: sets} = useSetsListQuery({projectId: projectID});
    return sets as PropertySetRead[]
}

export function useGetPropertySet(){
    const sets = usePropertySets();
    const getPropertySet = (setId: number) => {
        if(!sets) return undefined;
        const propertySet: PropertySetRead | undefined = sets.find(set => set.id == (setId));
        return propertySet;
    }
    return getPropertySet
}

export function useEdges(){
    const projectID = useProjectId();
    const {data: edges} = useEdgesListQuery({projectId: projectID});
    return edges as EdgeRead[] 
}
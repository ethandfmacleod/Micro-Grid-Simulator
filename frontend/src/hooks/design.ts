import { NodeRead, PropertySetRead, useNodesListQuery, useSetsListQuery } from "@/api/apiStore.gen";
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
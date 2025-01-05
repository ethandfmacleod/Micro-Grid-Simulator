import { ControllerRead, EdgeRead, NodeRead, ProjectRead, PropertySetRead, useControllersRetrieveQuery, useEdgesListQuery, useNodesListQuery, useSetsListQuery, useWeatherDataRetrieveQuery, WeatherDataRead } from "@/api/apiStore.gen";
import { useCurrentProject, useProjectId } from "./project";


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
    return getPropertySet;
}

export function useEdges(){
    const projectID = useProjectId();
    const {data: edges} = useEdgesListQuery({projectId: projectID});
    return edges as EdgeRead[];
}

export function useController(): ControllerRead | undefined{
    const project: ProjectRead | undefined = useCurrentProject();
    const {data: controller} = useControllersRetrieveQuery({id: project?.controller!}, { skip: !project });
    return controller!;
}

export function useWeatherData(): WeatherDataRead | undefined{
    const controller: ControllerRead | undefined = useController();
    const {data: weatherData} = useWeatherDataRetrieveQuery({id: controller?.weather!}, { skip: !controller });
    return weatherData!;
}
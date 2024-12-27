import { api, NodeRead, PropertyInfoRead, PropertySetRead, TypeEnum, useEdgesCreateMutation, useNodesCreateMutation, useNodesDestroyMutation, useNodesPartialUpdateMutation, useObjectsCreateMutation, usePropertiesPartialUpdateMutation } from "@/api/apiStore.gen";
import { useProjectId } from "@/hooks/project";
import { useAppDispatch } from "@/store/hooks";
import { Connection } from "node_modules/@xyflow/system/dist/esm/types/general";
import { toast } from "sonner";

export const useHandleNodeChange = () => {
    const dispatch = useAppDispatch();
    const projectID = useProjectId();

    const handleNodeChange = (changes: any) => {
        dispatch(
            api.util.updateQueryData(
                "nodesList",
                { projectId: projectID },
                (nodes) => {
                    changes.forEach((change: any) => {
                        if (change.type === "position") {
                            const nodeToUpdate = nodes.find(
                                (node: NodeRead) => node.id === change.id
                            );
                            if (nodeToUpdate) {
                                nodeToUpdate.position = change.position;
                            }
                        }
                    });
                }
            )
        );
    };
    return handleNodeChange;
};

export const useHandlePropertychange = () => {
    const dispatch = useAppDispatch();
    const projectID = useProjectId();
    const [updateProperty] = usePropertiesPartialUpdateMutation()

    const handleUpdateProperty = (property: PropertyInfoRead, value: any) => {

        if(value == '' || value == property.value){
            return;
        }

        dispatch(
            api.util.updateQueryData(
                "setsList",
                { projectId: projectID },
                (sets) => {
                    const targetPropertySet: PropertySetRead | undefined = sets.find(set => set.id == property.set)
                    if (targetPropertySet) {
                        const targetProperty: PropertyInfoRead = targetPropertySet.properties.find((prop: PropertyInfoRead) => prop.id == property.id)!
                        targetProperty.value = value
                    }
                }
            )
        );

        updateProperty({
            id: property.id,
            patchedPropertyInfo: { value: value }
        })
        .unwrap()
        .then(() => toast.success(`Updated ${property.display_name} to ${value}`))
    }
    
    return handleUpdateProperty
}

export const useHandleDeleteNode = () => {
    const [deleteNode] = useNodesDestroyMutation();
    const handleDeleteNode = (nodeID: number) => {
        deleteNode({id: nodeID})
    };
    return handleDeleteNode;
}

export const useHandleNodeDragEnd = () => {
    const [updateNode] = useNodesPartialUpdateMutation();
    const updateNodePosition = (event: React.MouseEvent, node: NodeRead, nodes: NodeRead[]) => {
        updateNode({id: +node.id, patchedNode: { position: node.position}})
    };
    return updateNodePosition;
};

export const useHandleObjectCreate = () => {
    const projectID = useProjectId();
    const [createObject] = useNodesCreateMutation();
    const handleObjectCreate = (type: TypeEnum) => {
        createObject(
            {
                createNode: {
                    type: type,
                    project: +projectID
                }
            }
        )
    }
    return handleObjectCreate;
}

export const useHandleNodeDelete = () => {
    const [deleteNode] = useNodesDestroyMutation();
    const handleNodeDelete = (nodes: NodeRead[]) => {
        nodes.forEach((node) => {
            deleteNode({
                id: +node.id
            });
        });
    };
    return handleNodeDelete;
};

export const useHandleConnect = () => {
    const [createEdge] = useEdgesCreateMutation();
    const projectID = useProjectId();
    const handleConnect = (connection: Connection) => {
        createEdge({
            edge: {
                project: +projectID,
                source: +connection.source,
                target: +connection.target
            }
        })
    };
    return handleConnect;
}
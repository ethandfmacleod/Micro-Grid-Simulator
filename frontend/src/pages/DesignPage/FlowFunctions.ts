import { api, NodeRead, TypeEnum, useEdgesCreateMutation, useNodesDestroyMutation, useNodesPartialUpdateMutation, useObjectsCreateMutation } from "@/api/apiStore.gen";
import { useProjectId } from "@/hooks/project";
import { useAppDispatch } from "@/store/hooks";
import { Connection } from "node_modules/@xyflow/system/dist/esm/types/general";

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

export const useHandleNodeDragEnd = () => {
    const [updateNode] = useNodesPartialUpdateMutation();
    const updateNodePosition = (event: React.MouseEvent, node: NodeRead, nodes: NodeRead[]) => {
        updateNode({id: +node.id, patchedNode: { position: node.position}})
    };
    return updateNodePosition;
};

export const useHandleObjectCreate = () => {
    const projectID = useProjectId();
    const [createObject] = useObjectsCreateMutation();
    const handleObjectCreate = (type: TypeEnum) => {
        createObject(
            {
                objectBase: {
                    type: type,
                    project: +projectID
                }
            }
        )
    }
    return handleObjectCreate
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
    }
    return handleConnect
}
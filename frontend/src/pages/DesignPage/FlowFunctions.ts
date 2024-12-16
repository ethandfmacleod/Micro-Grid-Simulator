import { api, NodeRead, useNodesPartialUpdateMutation } from "@/api/apiStore.gen";
import { useProjectId } from "@/hooks/project";
import { useAppDispatch } from "@/store/hooks";

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
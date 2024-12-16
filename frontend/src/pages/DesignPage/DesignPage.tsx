import StartPage from "@/components/layout/StartPage";
import { Background, BackgroundVariant, Controls, MiniMap, ReactFlow } from '@xyflow/react';
import '@xyflow/react/dist/base.css';
import { SolarNode, WindNode } from "./CustomNodes";
import { useEdges, useNodes } from "@/hooks/design";
import { useHandleNodeChange, useHandleNodeDragEnd } from "./FlowFunctions";

// Register Node Types
const nodeTypes = {
    solar_panel: SolarNode,
    wind_turbine: WindNode,
};

export function DesignPage() {
    const nodes = useNodes();
    const edges = useEdges();
    const handleNodeChange = useHandleNodeChange();
    const updateNodePosition = useHandleNodeDragEnd();
    const noop = () => { };

    return (
        <StartPage>
            <div style={{ width: '100vw', height: '100vh' }}>
                <ReactFlow
                    nodes={nodes}
                    edges={edges}
                    onNodesChange={handleNodeChange}
                    onNodeDragStop={updateNodePosition}
                    onEdgesChange={noop}
                    onConnect={noop}
                    onInit={noop}
                    onDragEnd={noop}
                    onDragOver={noop}
                    onNodeClick={noop}
                    onDrag={noop}
                    nodeTypes={nodeTypes}
                    fitView
                >
                    <Controls />
                    <MiniMap />
                    <Background variant={BackgroundVariant.Dots} gap={12} size={1} />
                </ReactFlow>
            </div>
        </StartPage>
    )
}
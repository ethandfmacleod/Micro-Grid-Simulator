import StartPage from "@/components/layout/StartPage";
import { addEdge, Background, BackgroundVariant, Controls, MiniMap, ReactFlow, useEdgesState, useNodesState } from '@xyflow/react';
import '@xyflow/react/dist/base.css';
import { useCallback } from "react";
import { SolarNode, WindNode } from "./CustomNodes";
import { useNodes } from "@/hooks/design";

// Register Node Types
const nodeTypes = {
    solar_panel: SolarNode,
    wind_turbine: WindNode,
};

// Sample EnergyIn Data
const energyInData = [
    {
        id: "1", position: { x: 0, y: 0 }, type: 'solar_panel', data: {
            "watts": 874,
            "price": 465.24,
            "daily_emissions": 4.67,
            "type": "solar",
            "name": "Panel 345",
            "panel_type": "monocrystalline",
            "width": 2,
            "length": 3,
            "cells": 127,
            "material": "silicon",
            "id": 5271
        }
    },
    {
        id: "2", position: { x: 0, y: 100 }, type: 'wind_turbine', data: {
            "watts": 1893,
            "price": 6728.38,
            "daily_emissions": 15.27,
            "type": "wind",
            "name": "Turbine 456",
            "rotor_diameter": 63,
            "rotation": 23,
            "cut_in_speed": 8,
            "rated_speed": 16,
            "cut_off_speed": 32,
            "id": 2942
        }
    },
];

const initialEdges = [{ id: 'e1-2', source: "1", target: "2" }];

export function DesignPage() {
    const nodes = useNodes();
    const [stateNodes, _, onNodesChange] = useNodesState(nodes);
    const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

    console.log(nodes);

    const onConnect = useCallback(
        (params: any) => setEdges((eds) => addEdge(params, eds)),
        [setEdges],
    );

    const noop = () => { };

    return (
        <StartPage>
            <div style={{ width: '100vw', height: '100vh' }}>
                <ReactFlow
                    nodes={stateNodes}
                    edges={edges}
                    onNodesChange={onNodesChange}
                    onEdgesChange={onEdgesChange}
                    onConnect={onConnect}
                    onInit={noop}
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
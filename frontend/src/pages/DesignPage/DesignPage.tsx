import StartPage from "@/components/layout/StartPage";
import { Background, BackgroundVariant, Controls, MiniMap, Panel, ReactFlow } from '@xyflow/react';
import '@xyflow/react/dist/base.css';
import { LithiumIonNode, SolarNode, WindNode } from "./CustomNodes";
import { useEdges, useNodes } from "@/hooks/design";
import { useHandleConnect, useHandleNodeChange, useHandleNodeDelete, useHandleNodeDragEnd, useHandleObjectCreate } from "./FlowFunctions";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Button } from "@/components/ui/button";
import { TypeEnum } from "@/api/apiStore.gen";

// Register Node Types
const nodeTypes = {
    solar_panel: SolarNode,
    wind_turbine: WindNode,
    lithium_ion: LithiumIonNode
};

export function DesignPage() {
    const nodes = useNodes();
    const edges = useEdges();

    const handleNodeChange = useHandleNodeChange();
    const updateNodePosition = useHandleNodeDragEnd();
    const handleObjectCreate = useHandleObjectCreate();
    const handleNodeDelete = useHandleNodeDelete();
    const handleConnect = useHandleConnect();

    const noop = () => { };

    return (
        <StartPage>
            <div style={{ width: '100vw', height: '100vh' }}>
                <ReactFlow
                    nodes={nodes}
                    edges={edges}
                    onNodesChange={handleNodeChange}
                    onNodeDragStop={updateNodePosition}
                    onNodesDelete={handleNodeDelete}
                    onEdgesChange={noop}
                    onConnect={handleConnect}
                    onInit={noop}
                    onDragEnd={noop}
                    onDragOver={noop}
                    onNodeClick={noop}
                    onDrag={noop}
                    nodeTypes={nodeTypes}
                    fitView
                >
                    <Panel className="bg-background shadow-lg rounded-md px-4 text-semibold" position="top-right">
                        <Accordion type="single" collapsible>
                            {/* Parent Accordion */}
                            <AccordionItem value="categories">
                                <AccordionTrigger className="font-semibold">
                                    Create Nodes
                                </AccordionTrigger>
                                <AccordionContent>
                                    {/* Energy Inputs Group */}
                                    <Accordion type="multiple" defaultValue={["energy_inputs", "energy_outputs", "consumers"]}>
                                        <AccordionItem value="energy_inputs">
                                            <AccordionTrigger>Energy Inputs</AccordionTrigger>
                                            <AccordionContent>
                                                <div className="flex flex-col gap-2">
                                                    <Button variant="ghost" className="p-0" onClick={() => handleObjectCreate(TypeEnum.SolarPanel)}>
                                                        Solar Panel
                                                    </Button>
                                                    <Button variant="ghost" onClick={() => handleObjectCreate(TypeEnum.WindTurbine)}>
                                                        Wind Turbine
                                                    </Button>
                                                </div>
                                            </AccordionContent>
                                        </AccordionItem>

                                        {/* Energy Outputs Group */}
                                        <AccordionItem value="energy_outputs">
                                            <AccordionTrigger>Energy Outputs</AccordionTrigger>
                                            <AccordionContent>
                                                <div className="flex flex-col gap-2">
                                                    <Button variant="ghost" onClick={() => handleObjectCreate(TypeEnum.LithiumIon)}>
                                                        Lithium Ion Battery
                                                    </Button>
                                                </div>
                                            </AccordionContent>
                                        </AccordionItem>

                                        {/* Consumers Group */}
                                        <AccordionItem value="consumers">
                                            <AccordionTrigger>Consumers</AccordionTrigger>
                                            <AccordionContent>
                                                <div className="flex flex-col gap-2">
                                                    <Button variant="ghost" onClick={() => handleObjectCreate("home")}>Home</Button>
                                                </div>
                                            </AccordionContent>
                                        </AccordionItem>
                                    </Accordion>
                                </AccordionContent>
                            </AccordionItem>
                        </Accordion>
                    </Panel>
                    <Controls />
                    <MiniMap />
                    <Background variant={BackgroundVariant.Dots} gap={12} size={1} />
                </ReactFlow>
            </div>
        </StartPage>
    )
}
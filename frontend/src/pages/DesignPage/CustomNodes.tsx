import { PropertySetList } from "@/components/PropertySetList";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Separator } from "@/components/ui/separator";
import { useGetPropertySet } from "@/hooks/design";
import { Handle, NodeToolbar, Position } from "@xyflow/react";
import { Eclipse, Fan, BatteryCharging, X } from "lucide-react";
import { ReactNode } from "react";
import { useHandleDeleteNode, useHandlePropertychange } from "./FlowFunctions";
import { CalculationMode } from "@/components/CalculationMode";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils"

// Custom Edge Style
const EdgeStyling = "w-[12px] h-[12px] !bg-background bg-opacity-100 border-2 border-primary rounded-full hover:border-green-500";

interface CustomNodeProps {
    icon: ReactNode;
    propertySetIds: number[];
    name: string;
    selected: boolean;
    calculationMode: string;
    nodeID: number;
};

export const CustomNode = ({ icon, propertySetIds, name, calculationMode, selected, nodeID }: CustomNodeProps) => {
    const getPropertySet = useGetPropertySet();
    const handleUpdateProperty = useHandlePropertychange();
    const handleDeleteNode = useHandleDeleteNode();
    const propertySets = propertySetIds.map((id) => getPropertySet(id)).filter((propertySet) => propertySet !== undefined);
    const outputPropertySet = propertySets.find((set) => set.name === "Outputs");
    const calculationPropertySet = propertySets.find((set) => set.name === calculationMode);

    return (
        <>
            <CustomNodeToolbar onClick={() => handleDeleteNode(nodeID)} visible={selected} />
            <div className="bg-background p-4 rounded-md border-2 border-primary w-max min-w-[225px] py-2">
                <Accordion type="single" collapsible>
                    <AccordionItem value="node">
                        <AccordionTrigger className="flex flex-row justify-between items-center gap-2 mb-1">
                            {icon}
                            <div className="font-semibold">{name}</div>
                        </AccordionTrigger >
                        <AccordionContent>
                            <div className="mb-4">
                                <CalculationMode calculationMode={calculationMode} propertySets={propertySets} nodeID={nodeID} />
                            </div>
                            <Separator className="bg-foreground mb-2 h-[1px]" />
                            <div className="mb-4">
                                <PropertySetList propertySet={outputPropertySet} handleUpdateProperty={handleUpdateProperty} />
                            </div>
                            <Separator className="bg-foreground mb-2 h-[1px]" />
                            <PropertySetList propertySet={calculationPropertySet} handleUpdateProperty={handleUpdateProperty} />
                        </AccordionContent>
                    </AccordionItem>
                    {/* Handle Connections */}
                    <Handle
                        type="target"
                        id="target"
                        position={Position.Left}
                        className={EdgeStyling}
                    />
                    <Handle
                        type="source"
                        id="source"
                        position={Position.Right}
                        className={EdgeStyling}
                    />
                </Accordion >
            </div >
        </>
    );
};

interface CustomNodeToolbarProps {
    onClick: () => void;
    visible: boolean;
}

const CustomNodeToolbar = ({ onClick, visible }: CustomNodeToolbarProps) => {
    return (
        <NodeToolbar
            isVisible={visible}
            position={Position.Top}
            align="center"
            className="flex flex-row gap-4 items-center text-sm"
        >
            <ToolbarButton icon={<X />} onClick={onClick} className="border-red-500" />
        </NodeToolbar>
    );
}

interface ToolbarButtonProps {
    icon: ReactNode;
    className?: string;
    onClick: () => void;
}

const ToolbarButton = ({ icon, onClick, className = '' }: ToolbarButtonProps) => {
    return (
        <Button
            variant={"outline"}
            size="icon"
            onClick={onClick}
            className={cn("text-sm bg-background rounded-full p-0", className)}>
            {icon}
        </Button>
    )
}

export const SolarNode = ({ data, isSelected }: { data: any, isSelected: boolean }) => {
    return (
        <CustomNode
            icon={<Eclipse />}
            propertySetIds={data.ids}
            name="Solar Panel"
            calculationMode={data.calculationMode}
            nodeID={data.nodeID}
            selected={isSelected}
        />
    );
}

export const WindNode = ({ data, isSelected }: { data: any, isSelected: boolean }) => {
    return (
        <CustomNode
            icon={<Fan />}
            propertySetIds={data.ids}
            name="Wind Turbine"
            calculationMode={data.calculationMode}
            nodeID={data.nodeID}
            selected={isSelected}
        />
    );
}

export const LithiumIonNode = ({ data, isSelected }: { data: any, isSelected: boolean }) => {
    return (
        <CustomNode
            icon={<BatteryCharging />}
            propertySetIds={data.ids}
            name="Lithium Battery"
            calculationMode={data.calculationMode}
            nodeID={data.nodeID}
            selected={isSelected}
        />
    );
}
import { PropertySetList } from "@/components/PropertySetList";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Separator } from "@/components/ui/separator";
import { useGetPropertySet } from "@/hooks/design";
import { Handle, NodeToolbar, Position } from "@xyflow/react";
import { Eclipse, Fan, BatteryCharging, X, House, DatabaseZap, Factory } from "lucide-react";
import { ReactNode } from "react";
import { useHandleDeleteNode, useHandlePropertychange } from "./FlowFunctions";
import { CalculationMode } from "@/components/CalculationMode";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils"
import { useCurrentObject } from "@/hooks/params";

interface CustomNodeProps {
    icon: ReactNode;
    propertySetIds: number[];
    name: string;
    calculationMode: string;
    nodeID: number;
};

export const CustomNode = ({ icon, propertySetIds, name, calculationMode, nodeID }: CustomNodeProps) => {
    const getPropertySet = useGetPropertySet();
    const handleUpdateProperty = useHandlePropertychange();
    const handleDeleteNode = useHandleDeleteNode();
    const propertySets = propertySetIds.map((id) => getPropertySet(id)).filter((propertySet) => propertySet !== undefined);
    const outputPropertySet = propertySets.find((set) => set.name === "Outputs");
    const calculationPropertySet = propertySets.find((set) => set.name === calculationMode);
    const currentObject = useCurrentObject();
    const selected = currentObject !== null ? nodeID === +currentObject : false;
    const EdgeStyling = "w-[12px] h-[12px] !bg-background bg-opacity-100 border-2 border-primary rounded-full hover:border-green-500";

    return (
        <>
            <CustomNodeToolbar onClick={() => handleDeleteNode(nodeID)} visible={selected} />
            <div className="bg-background p-4 rounded-md border-2 border-primary w-max min-w-[225px] py-2">
                <Accordion type="single" collapsible>
                    <AccordionItem value="node">
                        <AccordionTrigger className="flex flex-row justify-between items-center gap-2 mb-1">
                            <span
                                className={cn(
                                    "transition-transform duration-300 transform-origin-center",
                                    "[data-state=open]:rotate-180"
                                )}
                            >
                                {icon}
                            </span>
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
            onClick={onClick}
            className={cn("text-sm bg-background rounded-full p-0 h-5 w-5", className)}>
            {icon}
        </Button>
    )
}

export const SolarNode = ({ data }: { data: any }) => {
    return (
        <CustomNode
            icon={<Eclipse />}
            propertySetIds={data.ids}
            name="Solar Panel"
            calculationMode={data.calculationMode}
            nodeID={data.nodeID}
        />
    );
}

export const WindNode = ({ data }: { data: any }) => {
    return (
        <CustomNode
            icon={<Fan />}
            propertySetIds={data.ids}
            name="Wind Turbine"
            calculationMode={data.calculationMode}
            nodeID={data.nodeID}
        />
    );
}

export const LithiumIonNode = ({ data }: { data: any }) => {
    return (
        <CustomNode
            icon={<BatteryCharging />}
            propertySetIds={data.ids}
            name="Lithium Battery"
            calculationMode={data.calculationMode}
            nodeID={data.nodeID}
        />
    );
}

export const HomeNode = ({ data }: { data: any }) => {
    return (
        <CustomNode
            icon={<House />}
            propertySetIds={data.ids}
            name="Home"
            calculationMode={data.calculationMode}
            nodeID={data.nodeID}
        />
    );
}

export const InverterNode = ({ data }: { data: any }) => {
    return (
        <CustomNode
            icon={<DatabaseZap />}
            propertySetIds={data.ids}
            name="Inverter"
            calculationMode={data.calculationMode}
            nodeID={data.nodeID}
        />
    );
}

export const GridNode = ({ data }: { data: any }) => {
    return (
        <CustomNode
            icon={<Factory />}
            propertySetIds={data.ids}
            name="Grid"
            calculationMode={data.calculationMode}
            nodeID={data.nodeID}
        />
    );
}
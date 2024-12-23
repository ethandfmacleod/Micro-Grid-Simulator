import { PropertySetList } from "@/components/PropertySetList";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Separator } from "@/components/ui/separator";
import { useGetPropertySet } from "@/hooks/design";
import { Handle, Position } from "@xyflow/react";
import { Eclipse, Fan, BatteryCharging } from "lucide-react";
import { ReactNode } from "react";
import { useHandlePropertychange } from "./FlowFunctions";
import { CalculationMode } from "@/components/CalculationMode";

interface CustomNodeProps {
    icon: ReactNode;
    propertySetIds: number[];
    name: string;
    calculationMode: string;
    nodeID: number;
}

export const CustomNode = ({ icon, propertySetIds, name, calculationMode, nodeID }: CustomNodeProps) => {
    const getPropertySet = useGetPropertySet();
    const handleUpdateProperty = useHandlePropertychange();
    const propertySets = propertySetIds.map((id) => getPropertySet(id)).filter((propertySet) => propertySet !== undefined);
    const outputPropertySet = propertySets.find((set) => set.name === "Outputs");
    const calculationPropertySet = propertySets.find((set) => set.name === calculationMode);

    return (
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
                <Handle type="target" position={Position.Left} id="target" />
                <Handle type="source" position={Position.Right} id="source" />
            </Accordion >
        </div >
    );
};

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
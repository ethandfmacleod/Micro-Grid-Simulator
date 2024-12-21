import { PropertySetList } from "@/components/PropertySetList";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Separator } from "@/components/ui/separator";
import { useGetPropertySet } from "@/hooks/design";
import { Handle, Position } from "@xyflow/react";
import { Eclipse, Fan, BatteryCharging } from "lucide-react";
import { ReactNode } from "react";
import { useHandlePropertychange } from "./FlowFunctions";

interface CustomNodeProps {
    icon: ReactNode;
    propertySetId: number;
    name: string;
}

export const CustomNode = ({ icon, propertySetId, name }: CustomNodeProps) => {
    const getPropertySet = useGetPropertySet();
    const handleUpdateProperty = useHandlePropertychange();

    return (
        <div className="bg-background p-4 rounded-md border-2 border-primary w-max min-w-[225px] py-2">
            <Accordion type="single" collapsible>
                <AccordionItem value="node">
                    <AccordionTrigger className="flex flex-row justify-between items-center gap-2 mb-1">
                        {icon}
                        <div className="font-semibold">{name}</div>
                    </AccordionTrigger >
                    <AccordionContent>
                        <Separator className="bg-foreground mb-2" />
                        <PropertySetList propertySet={getPropertySet(propertySetId)} handleUpdateProperty={handleUpdateProperty} />
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
        <CustomNode icon={<Eclipse />} propertySetId={data.id} name="Solar Panel" />
    );
}

export const WindNode = ({ data }: { data: any }) => {
    return (
        <CustomNode icon={<Fan />} propertySetId={data.id} name="Wind Turbine" />
    );
}

export const LithiumIonNode = ({ data }: { data: any }) => {
    return (
        <CustomNode icon={<BatteryCharging />} propertySetId={data.id} name="Lithium Battery" />
    );
}
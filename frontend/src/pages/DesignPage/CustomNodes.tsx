import { PropertyInfoRead, PropertySetRead } from "@/api/apiStore.gen";
import { PropertySetList } from "@/components/PropertySetList";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Separator } from "@/components/ui/separator";
import { useGetPropertySet } from "@/hooks/design";
import { Handle, Position } from "@xyflow/react";
import { Eclipse, Fan, BatteryCharging } from "lucide-react";
import { ReactNode } from "react";

interface CustomNodeProps {
    icon: ReactNode;
    propertySetId: number;
    name: string;
}

export const CustomNode = ({ icon, propertySetId, name }: CustomNodeProps) => {
    const getPropertySet = useGetPropertySet();
    const propertySet: PropertySetRead | undefined = getPropertySet(propertySetId);
    const properties: PropertyInfoRead[] = propertySet ? propertySet.properties : []
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
                        {propertySet ? (
                            <PropertySetList properties={properties} />
                        ) : (
                            <div className="text-sm text-gray-500">Loading properties...</div>
                        )}
                    </AccordionContent>
                </AccordionItem>
                {/* Handle Connections */}
                <Handle type="target" position={Position.Top} id="target" />
                <Handle type="source" position={Position.Bottom} id="source" />
            </Accordion >
        </div >
    );
};

export const SolarNode = ({ id }: { id: number }) => {
    return (
        <CustomNode icon={<Eclipse />} propertySetId={id} name="Solar Panel" />
    );
}

export const WindNode = ({ id }: { id: number }) => {
    return (
        <CustomNode icon={<Fan />} propertySetId={id} name="Wind Turbine" />
    );
}

export const LithiumIonNode = ({ id }: { id: number }) => {
    return (
        <CustomNode icon={<BatteryCharging />} propertySetId={id} name="Lithium Battery" />
    );
}
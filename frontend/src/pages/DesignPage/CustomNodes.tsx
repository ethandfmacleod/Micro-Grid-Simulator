import { PropertyInfoRead, PropertySetRead } from "@/api/apiStore.gen";
import { PropertySetList } from "@/components/PropertySetList";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Separator } from "@/components/ui/separator";
import { useGetPropertySet } from "@/hooks/design";
import { Handle, Position } from "@xyflow/react";
import { Eclipse, Fan } from "lucide-react";
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
        <div className="bg-background p-4 rounded-md border-2 border-primary">
            <Accordion type="single">
                <AccordionItem value="node">
                    <AccordionTrigger className="flex flex-row justify-between items-center gap-2 mb-1">
                        {icon}
                        <div className="font-semibold">{name}</div>
                    </AccordionTrigger >
                    <AccordionContent>
                        <Separator className="bg-foreground mb-2" />
                        <PropertySetList properties={properties} />
                    </AccordionContent>
                </AccordionItem>
                {/* Handle Connections */}
                <Handle type="target" position={Position.Top} id="target" />
                <Handle type="source" position={Position.Bottom} id="source" />
            </Accordion >
        </div >
    );
};

export const SolarNode = ({ propertySet, name }: { propertySet: number, name: string }) => {
    return (
        <CustomNode icon={<Eclipse />} propertySetId={propertySet} name={name || "New Object"} />
    );
}

export const WindNode = ({ propertySet, name }: { propertySet: number, name: string }) => {
    return (
        <CustomNode icon={<Fan />} propertySetId={propertySet} name={name || "New Object"} />
    );
}
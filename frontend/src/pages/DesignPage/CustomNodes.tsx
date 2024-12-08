import { SolarPanelSchema, WindTurbineSchema } from "@/api/apiStore.gen";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Separator } from "@/components/ui/separator";
import { Handle, Position } from "@xyflow/react";
import { Eclipse, Fan } from "lucide-react";
import { ReactNode } from "react";

// Generic Custom Node Component
interface CustomNodeProps<T> {
    icon: ReactNode;
    data: Omit<T, 'type' | 'id'>; // Omit 'type' and 'id' fields
}

export const CustomNode = <T extends object>({ icon, data }: CustomNodeProps<T>) => {

    return (
        <div className="bg-background p-4 rounded-md border-2 border-primary">
            <Accordion type="single">
                <AccordionItem value="node">
                    <AccordionTrigger className="flex flex-row justify-between items-center gap-2 mb-1">
                        {icon}
                        <div className="font-semibold">{data.name}</div>
                    </AccordionTrigger >
                    <AccordionContent>
                        <Separator className="bg-foreground mb-2" />
                        {Object.keys(data).map((key) => (
                            key !== 'name' && key !== 'type' && key !== 'id' && (
                                <div key={key}>
                                    {key}: {data[key as keyof typeof data]}
                                </div>
                            )
                        ))}
                    </AccordionContent>
                </AccordionItem>
                {/* Handle Connections */}
                <Handle type="target" position={Position.Top} id="target" />
                <Handle type="source" position={Position.Bottom} id="source" />
            </Accordion >
        </div >
    );
};

export const SolarNode = ({ data }: {data: SolarPanelSchema}) => {
    return (
        <CustomNode icon={<Eclipse />} data={data} />
    );
}

export const WindNode = ({ data }: {data: WindTurbineSchema}) => {
    return (
        <CustomNode icon={<Fan />} data={data} />
    );
}
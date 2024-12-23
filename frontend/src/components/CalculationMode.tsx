import { PropertySet, useNodesPartialUpdateMutation } from "@/api/apiStore.gen";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "./ui/select";
import { toast } from "sonner";

interface CalculationModeProps {
    calculationMode: string;
    propertySets: PropertySet[];
    nodeID: number;
}

export const CalculationMode = ({ calculationMode, propertySets, nodeID }: CalculationModeProps) => {
    const [updateNode] = useNodesPartialUpdateMutation();

    const handleUpdateCalculationMode = (value: string) => {
        updateNode({
            id: nodeID,
            patchedNode: { calculation_mode: value }
        })
            .unwrap()
            .then(() => toast.success("Updated Calculation Mode"))
    }

    return (
        <Select
            value={calculationMode}
            onValueChange={handleUpdateCalculationMode}
        >
            <SelectTrigger>
                <SelectValue placeholder="Select Calculation Mode" />
            </SelectTrigger>
            <SelectContent>
                {propertySets
                    .filter((set) => set.name !== "Outputs" && set.name !== "Advanced")
                    .map((set) => (
                        <SelectItem key={set.name} value={set.name!}>
                            {set.name}
                        </SelectItem>
                    ))}
            </SelectContent>
        </Select>
    )
}
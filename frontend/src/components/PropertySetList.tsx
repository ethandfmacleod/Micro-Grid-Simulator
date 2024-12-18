import { PropertyInfoRead } from "@/api/apiStore.gen";
import { Label } from "./ui/label";
import { Input } from "./ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "./ui/select";
import { Checkbox } from "./ui/checkbox";

interface PropertySetListProps {
    properties: PropertyInfoRead[];
}

export function PropertySetList({ properties }: PropertySetListProps) {
    return (
        <div className="flex flex-col gap-2">
            {properties.map((property: PropertyInfoRead) => {
                return (
                    <PropertyInfoInput key={property.key} property={property} />
                )
            })}
        </div>
    )
}

const PropertyInfoInput = ({ property }: { property: PropertyInfoRead }) => {
    const renderInput = () => {
        switch (property.display_type) {
            case "numeric":
                return <Input type="number" defaultValue={property.value} />;
            case "dropdown":
                return (
                    <Select>
                        <SelectTrigger>
                            <SelectValue placeholder="Select an option" />
                        </SelectTrigger>
                        <SelectContent>
                            {/* Assuming property.value is an array of dropdown options */}
                            {property.value?.split(",").map((option: string, idx: number) => (
                                <SelectItem key={idx} value={option}>
                                    {option}
                                </SelectItem>
                            ))}
                        </SelectContent>
                    </Select>
                );
            case "checkbox":
                return (
                    <Checkbox defaultChecked={property.value === "true"} />
                );
            default:
                return <Input type="text" defaultValue={property.value} />;
        }
    };

    return (
        <div>
            <Label>{property.display_name}</Label>
            {renderInput()}
        </div>
    );
};
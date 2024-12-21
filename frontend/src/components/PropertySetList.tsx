import { PropertyInfoRead, PropertySetRead } from "@/api/apiStore.gen";
import { Label } from "./ui/label";
import { Input } from "./ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "./ui/select";
import { Checkbox } from "./ui/checkbox";

interface PropertySetListProps {
    propertySet: PropertySetRead | undefined;
    handleUpdateProperty: (property: PropertyInfoRead, value: any) => void;
}

export function PropertySetList({ propertySet, handleUpdateProperty }: PropertySetListProps) {
    const properties: PropertyInfoRead[] = propertySet ? propertySet.properties : []

    return (
        <div className="flex flex-col gap-2">
            {properties.map((property: PropertyInfoRead) => {
                return (
                    <PropertyInfoInput
                        key={property.key}
                        property={property}
                        handleUpdateProperty={handleUpdateProperty}
                    />
                );
            })}
        </div>
    );
}

interface PropertyInfoInputProps {
    property: PropertyInfoRead;
    handleUpdateProperty: (property: PropertyInfoRead, value: any) => void;
}

const PropertyInfoInput = ({ property, handleUpdateProperty }: PropertyInfoInputProps) => {
    const renderInput = () => {
        switch (property.display_type) {
            case "numeric":
                return (
                    <Input
                        type="number"
                        defaultValue={property.value}
                        onBlur={(e) => handleUpdateProperty(property, e.target.value)}
                    />
                );
            case "dropdown":
                return (
                    <Select
                        value={property.value}
                        onValueChange={(value) => handleUpdateProperty(property, value)}
                    >
                        <SelectTrigger>
                            <SelectValue placeholder="Select an option" />
                        </SelectTrigger>
                        <SelectContent>
                            {/* Assuming property.value contains comma-separated dropdown options */}
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
                    <Checkbox
                        defaultChecked={property.value === "true"}
                        onCheckedChange={(checked) =>
                            handleUpdateProperty(property, checked.toString())
                        }
                    />
                );
            default:
                return (
                    <Input
                        type="text"
                        defaultValue={property.value}
                        onBlur={(e) => handleUpdateProperty(property, e.target.value)}
                    />
                );
        }
    };

    return (
        <div>
            <Label>{property.display_name}</Label>
            {renderInput()}
        </div>
    );
};

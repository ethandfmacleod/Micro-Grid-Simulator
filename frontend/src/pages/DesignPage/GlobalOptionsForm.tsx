import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useController, useWeatherData } from "@/hooks/design"
import { Panel } from "@xyflow/react"
import { useHandleUpdateController, useHandleUpdateWeatherData } from "./FlowFunctions";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { ControllerRead, WeatherDataRead } from "@/api/apiStore.gen";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

export const FlowsheetOptionsForm = () => {
    const controller = useController();
    const weatherData = useWeatherData();

    if (!controller || !weatherData) {
        return (
            <Panel className="bg-background shadow-lg rounded-md px-4 text-semibold" position="top-left">
                <div>Loading...</div>
            </Panel>
        );
    }

    return (
        <Panel className="bg-background shadow-lg rounded-md p-4 text-semibold" position="top-left">
            <Tabs defaultValue="global">
                <TabsList className="grid w-full grid-cols-2">
                    <TabsTrigger value="global">Global</TabsTrigger>
                    <TabsTrigger value="weather">Weather</TabsTrigger>
                </TabsList>
                <GlobalOptionsForm controller={controller}/>
                <WeatherOptionsForm weatherData={weatherData}/>
            </Tabs>
        </Panel>
    )
}

const GlobalOptionsForm = ({controller}: {controller: ControllerRead}) => {
    const handleUpdateController = useHandleUpdateController();
    return (
        <TabsContent value="global">
            <Label className=" text-xs font-semibold">Total Energy (kWh)</Label>
            <Input
                type="number"
                defaultValue={controller.total_energy || ''}
                disabled={true}
                className={"border-gray-500"}
            />
            <Label className=" text-xs font-semibold">Co2 Offset (kgCO₂e / year)</Label>
            <Input
                type="number"
                defaultValue={controller.total_emissions || ''}
                disabled={true}
                className={"border-gray-500"}
            />
            <Label className=" text-xs font-semibold">Grid Emissions Factor (kgCO2e/kWh)</Label>
            <Input
                type="number"
                onBlur={(e) => handleUpdateController(controller.id, "grid_emission_factor", e.target.value)}
                defaultValue={controller.grid_emission_factor || ''}
                className={"border-green-500"}
            />
            <Label className=" text-xs font-semibold">Latitiude</Label>
            <Input
                type="number"
                onBlur={(e) => handleUpdateController(controller.id, "latitude", e.target.value)}
                defaultValue={controller.latitude || ''}
                className={controller.latitude ? "border-green-500" : "border-red-500"}
            />
            <Label className=" text-xs font-semibold">Longitude</Label>
            <Input
                type="number"
                onBlur={(e) => handleUpdateController(controller.id, "longitude", e.target.value)}
                defaultValue={controller.longitude || ''}
                className={controller.longitude ? "border-green-500" : "border-red-500"}
            />
        </TabsContent>

    )
}

const WeatherOptionsForm = ({weatherData}: {weatherData: WeatherDataRead}) => {
    const handleUpdateWeatherData = useHandleUpdateWeatherData();
    return (
        <TabsContent value="weather">
            <Label className=" text-xs font-semibold">Temperature (°C)</Label>
            <Input
                type="number"
                defaultValue={weatherData.temperature || ''}
                disabled={true}
                className={"border-gray-500"}
            />
            <Label className=" text-xs font-semibold">Wind Speed (m/s)</Label>
            <Input
                type="number"
                defaultValue={weatherData.wind_speed || ''}
                disabled={true}
                className={"border-gray-500"}
            />
            <Label className=" text-xs font-semibold">Humidity (g/kg)</Label>
            <Input
                type="number"
                defaultValue={weatherData.humidity || ''}
                disabled={true}
                className={"border-gray-500"}
            />
            <Label className=" text-xs font-semibold">Timeframe</Label>
            <Select
                value={weatherData.timeframe}
                onValueChange={(value) => handleUpdateWeatherData(weatherData.id, "timeframe", value)}
            >
                <SelectTrigger>
                    <SelectValue placeholder="Select an option" />
                </SelectTrigger>
                <SelectContent>
                    <SelectItem value="current">Current</SelectItem>
                    <SelectItem value="minutely">Minutely</SelectItem>
                    <SelectItem value="hourly">Hourly</SelectItem>
                    <SelectItem value="daily">Daily</SelectItem>
                </SelectContent>
            </Select>
            <Label className=" text-xs font-semibold">Sky</Label>
            <Select
                value={weatherData.sky}
                onValueChange={(value) => handleUpdateWeatherData(weatherData.id, "sky", value)}
            >
                <SelectTrigger>
                    <SelectValue placeholder="Select an option" />
                </SelectTrigger>
                <SelectContent>
                    <SelectItem value="cloudy_sky">Cloudy</SelectItem>
                    <SelectItem value="clear_sky">Clear</SelectItem>
                </SelectContent>
            </Select>
            <Label className=" text-xs font-semibold">Irradiance (W/m2)</Label>
            <Input
                type="number"
                onBlur={(e) => handleUpdateWeatherData(weatherData.id, "irradiance", e.target.value)}
                defaultValue={weatherData.irradiance || ''}
                className={weatherData.irradiance ? "border-green-500" : "border-red-500"}
            />
        </TabsContent>
    )
}
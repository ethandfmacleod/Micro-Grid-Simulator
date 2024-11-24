import { emptySplitApi as api } from "./emptyApi";
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    readEnergyInsModelsEnergyInsGet: build.query<
      ReadEnergyInsModelsEnergyInsGetApiResponse,
      ReadEnergyInsModelsEnergyInsGetApiArg
    >({
      query: () => ({ url: `/models/energy_ins/` }),
    }),
    createEnergyInModelsEnergyInsPost: build.mutation<
      CreateEnergyInModelsEnergyInsPostApiResponse,
      CreateEnergyInModelsEnergyInsPostApiArg
    >({
      query: (queryArg) => ({
        url: `/models/energy_ins/`,
        method: "POST",
        body: queryArg.energyInCreate,
      }),
    }),
    readEnergyInModelsEnergyInsIdGet: build.query<
      ReadEnergyInModelsEnergyInsIdGetApiResponse,
      ReadEnergyInModelsEnergyInsIdGetApiArg
    >({
      query: (queryArg) => ({ url: `/models/energy_ins/${queryArg.id}` }),
    }),
    updateEnergyInModelsEnergyInsIdPut: build.mutation<
      UpdateEnergyInModelsEnergyInsIdPutApiResponse,
      UpdateEnergyInModelsEnergyInsIdPutApiArg
    >({
      query: (queryArg) => ({
        url: `/models/energy_ins/${queryArg.id}`,
        method: "PUT",
        body: queryArg.energyInUpdate,
      }),
    }),
    deleteEnergyInModelsEnergyInsIdDelete: build.mutation<
      DeleteEnergyInModelsEnergyInsIdDeleteApiResponse,
      DeleteEnergyInModelsEnergyInsIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/models/energy_ins/${queryArg.id}`,
        method: "DELETE",
      }),
    }),
    readSolarPanelsModelsSolarPanelsGet: build.query<
      ReadSolarPanelsModelsSolarPanelsGetApiResponse,
      ReadSolarPanelsModelsSolarPanelsGetApiArg
    >({
      query: () => ({ url: `/models/solar_panels/` }),
    }),
    createSolarPanelModelsSolarPanelsPost: build.mutation<
      CreateSolarPanelModelsSolarPanelsPostApiResponse,
      CreateSolarPanelModelsSolarPanelsPostApiArg
    >({
      query: (queryArg) => ({
        url: `/models/solar_panels/`,
        method: "POST",
        body: queryArg.solarPanelCreate,
      }),
    }),
    readSolarPanelModelsSolarPanelsIdGet: build.query<
      ReadSolarPanelModelsSolarPanelsIdGetApiResponse,
      ReadSolarPanelModelsSolarPanelsIdGetApiArg
    >({
      query: (queryArg) => ({ url: `/models/solar_panels/${queryArg.id}` }),
    }),
    updateSolarPanelModelsSolarPanelsIdPut: build.mutation<
      UpdateSolarPanelModelsSolarPanelsIdPutApiResponse,
      UpdateSolarPanelModelsSolarPanelsIdPutApiArg
    >({
      query: (queryArg) => ({
        url: `/models/solar_panels/${queryArg.id}`,
        method: "PUT",
        body: queryArg.solarPanelUpdate,
      }),
    }),
    deleteSolarPanelModelsSolarPanelsIdDelete: build.mutation<
      DeleteSolarPanelModelsSolarPanelsIdDeleteApiResponse,
      DeleteSolarPanelModelsSolarPanelsIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/models/solar_panels/${queryArg.id}`,
        method: "DELETE",
      }),
    }),
    readWindTurbinesModelsWindTurbinesGet: build.query<
      ReadWindTurbinesModelsWindTurbinesGetApiResponse,
      ReadWindTurbinesModelsWindTurbinesGetApiArg
    >({
      query: () => ({ url: `/models/wind_turbines/` }),
    }),
    createWindTurbineModelsWindTurbinesPost: build.mutation<
      CreateWindTurbineModelsWindTurbinesPostApiResponse,
      CreateWindTurbineModelsWindTurbinesPostApiArg
    >({
      query: (queryArg) => ({
        url: `/models/wind_turbines/`,
        method: "POST",
        body: queryArg.windTurbineCreate,
      }),
    }),
    readWindTurbineModelsWindTurbinesIdGet: build.query<
      ReadWindTurbineModelsWindTurbinesIdGetApiResponse,
      ReadWindTurbineModelsWindTurbinesIdGetApiArg
    >({
      query: (queryArg) => ({ url: `/models/wind_turbines/${queryArg.id}` }),
    }),
    updateWindTurbineModelsWindTurbinesIdPut: build.mutation<
      UpdateWindTurbineModelsWindTurbinesIdPutApiResponse,
      UpdateWindTurbineModelsWindTurbinesIdPutApiArg
    >({
      query: (queryArg) => ({
        url: `/models/wind_turbines/${queryArg.id}`,
        method: "PUT",
        body: queryArg.windTurbineUpdate,
      }),
    }),
    deleteWindTurbineModelsWindTurbinesIdDelete: build.mutation<
      DeleteWindTurbineModelsWindTurbinesIdDeleteApiResponse,
      DeleteWindTurbineModelsWindTurbinesIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/models/wind_turbines/${queryArg.id}`,
        method: "DELETE",
      }),
    }),
    readEnergyOutsModelsEnergyOutsGet: build.query<
      ReadEnergyOutsModelsEnergyOutsGetApiResponse,
      ReadEnergyOutsModelsEnergyOutsGetApiArg
    >({
      query: () => ({ url: `/models/energy_outs/` }),
    }),
    createEnergyOutModelsEnergyOutsPost: build.mutation<
      CreateEnergyOutModelsEnergyOutsPostApiResponse,
      CreateEnergyOutModelsEnergyOutsPostApiArg
    >({
      query: (queryArg) => ({
        url: `/models/energy_outs/`,
        method: "POST",
        body: queryArg.energyOutCreate,
      }),
    }),
    readEnergyOutModelsEnergyOutsIdGet: build.query<
      ReadEnergyOutModelsEnergyOutsIdGetApiResponse,
      ReadEnergyOutModelsEnergyOutsIdGetApiArg
    >({
      query: (queryArg) => ({ url: `/models/energy_outs/${queryArg.id}` }),
    }),
    updateEnergyOutModelsEnergyOutsIdPut: build.mutation<
      UpdateEnergyOutModelsEnergyOutsIdPutApiResponse,
      UpdateEnergyOutModelsEnergyOutsIdPutApiArg
    >({
      query: (queryArg) => ({
        url: `/models/energy_outs/${queryArg.id}`,
        method: "PUT",
        body: queryArg.energyOutUpdate,
      }),
    }),
    deleteEnergyOutModelsEnergyOutsIdDelete: build.mutation<
      DeleteEnergyOutModelsEnergyOutsIdDeleteApiResponse,
      DeleteEnergyOutModelsEnergyOutsIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/models/energy_outs/${queryArg.id}`,
        method: "DELETE",
      }),
    }),
    readProjectsProjectsGet: build.query<
      ReadProjectsProjectsGetApiResponse,
      ReadProjectsProjectsGetApiArg
    >({
      query: () => ({ url: `/projects/` }),
    }),
    createProjectProjectsPost: build.mutation<
      CreateProjectProjectsPostApiResponse,
      CreateProjectProjectsPostApiArg
    >({
      query: (queryArg) => ({
        url: `/projects/`,
        method: "POST",
        body: queryArg.projectCreate,
      }),
    }),
    readProjectProjectsIdGet: build.query<
      ReadProjectProjectsIdGetApiResponse,
      ReadProjectProjectsIdGetApiArg
    >({
      query: (queryArg) => ({ url: `/projects/${queryArg.id}` }),
    }),
    updateProjectProjectsIdPut: build.mutation<
      UpdateProjectProjectsIdPutApiResponse,
      UpdateProjectProjectsIdPutApiArg
    >({
      query: (queryArg) => ({
        url: `/projects/${queryArg.id}`,
        method: "PUT",
        body: queryArg.projectUpdate,
      }),
    }),
    deleteProjectProjectsIdDelete: build.mutation<
      DeleteProjectProjectsIdDeleteApiResponse,
      DeleteProjectProjectsIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/projects/${queryArg.id}`,
        method: "DELETE",
      }),
    }),
    readEnergyStoragesModelsEnergyStoragesGet: build.query<
      ReadEnergyStoragesModelsEnergyStoragesGetApiResponse,
      ReadEnergyStoragesModelsEnergyStoragesGetApiArg
    >({
      query: () => ({ url: `/models/energy_storages/` }),
    }),
    createEnergyStorageModelsEnergyStoragesPost: build.mutation<
      CreateEnergyStorageModelsEnergyStoragesPostApiResponse,
      CreateEnergyStorageModelsEnergyStoragesPostApiArg
    >({
      query: (queryArg) => ({
        url: `/models/energy_storages/`,
        method: "POST",
        body: queryArg.energyStorageUnitCreate,
      }),
    }),
    readEnergyStorageModelsEnergyStoragesIdGet: build.query<
      ReadEnergyStorageModelsEnergyStoragesIdGetApiResponse,
      ReadEnergyStorageModelsEnergyStoragesIdGetApiArg
    >({
      query: (queryArg) => ({ url: `/models/energy_storages/${queryArg.id}` }),
    }),
    updateEnergyStorageModelsEnergyStoragesIdPut: build.mutation<
      UpdateEnergyStorageModelsEnergyStoragesIdPutApiResponse,
      UpdateEnergyStorageModelsEnergyStoragesIdPutApiArg
    >({
      query: (queryArg) => ({
        url: `/models/energy_storages/${queryArg.id}`,
        method: "PUT",
        body: queryArg.energyStorageUnitUpdate,
      }),
    }),
    deleteEnergyStorageModelsEnergyStoragesIdDelete: build.mutation<
      DeleteEnergyStorageModelsEnergyStoragesIdDeleteApiResponse,
      DeleteEnergyStorageModelsEnergyStoragesIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/models/energy_storages/${queryArg.id}`,
        method: "DELETE",
      }),
    }),
    readLithiumIonsModelsLithiumIonsGet: build.query<
      ReadLithiumIonsModelsLithiumIonsGetApiResponse,
      ReadLithiumIonsModelsLithiumIonsGetApiArg
    >({
      query: () => ({ url: `/models/lithium_ions/` }),
    }),
    createLithiumIonModelsLithiumIonsPost: build.mutation<
      CreateLithiumIonModelsLithiumIonsPostApiResponse,
      CreateLithiumIonModelsLithiumIonsPostApiArg
    >({
      query: (queryArg) => ({
        url: `/models/lithium_ions/`,
        method: "POST",
        body: queryArg.lithiumIonBatteryCreate,
      }),
    }),
    readLithiumIonModelsLithiumIonsIdGet: build.query<
      ReadLithiumIonModelsLithiumIonsIdGetApiResponse,
      ReadLithiumIonModelsLithiumIonsIdGetApiArg
    >({
      query: (queryArg) => ({ url: `/models/lithium_ions/${queryArg.id}` }),
    }),
    updateLithiumIonModelsLithiumIonsIdPut: build.mutation<
      UpdateLithiumIonModelsLithiumIonsIdPutApiResponse,
      UpdateLithiumIonModelsLithiumIonsIdPutApiArg
    >({
      query: (queryArg) => ({
        url: `/models/lithium_ions/${queryArg.id}`,
        method: "PUT",
        body: queryArg.lithiumIonBatteryUpdate,
      }),
    }),
    deleteLithiumIonModelsLithiumIonsIdDelete: build.mutation<
      DeleteLithiumIonModelsLithiumIonsIdDeleteApiResponse,
      DeleteLithiumIonModelsLithiumIonsIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/models/lithium_ions/${queryArg.id}`,
        method: "DELETE",
      }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as api };
export type ReadEnergyInsModelsEnergyInsGetApiResponse =
  /** status 200 Successful Response */ EnergyInSchema[];
export type ReadEnergyInsModelsEnergyInsGetApiArg = void;
export type CreateEnergyInModelsEnergyInsPostApiResponse =
  /** status 201 Successful Response */ EnergyInSchema;
export type CreateEnergyInModelsEnergyInsPostApiArg = {
  energyInCreate: EnergyInCreate;
};
export type ReadEnergyInModelsEnergyInsIdGetApiResponse =
  /** status 200 Successful Response */ EnergyInSchema;
export type ReadEnergyInModelsEnergyInsIdGetApiArg = {
  id: number;
};
export type UpdateEnergyInModelsEnergyInsIdPutApiResponse =
  /** status 200 Successful Response */ EnergyInSchema;
export type UpdateEnergyInModelsEnergyInsIdPutApiArg = {
  id: number;
  energyInUpdate: EnergyInUpdate;
};
export type DeleteEnergyInModelsEnergyInsIdDeleteApiResponse =
  /** status 200 Successful Response */ EnergyInSchema;
export type DeleteEnergyInModelsEnergyInsIdDeleteApiArg = {
  id: number;
};
export type ReadSolarPanelsModelsSolarPanelsGetApiResponse =
  /** status 200 Successful Response */ SolarPanelSchema[];
export type ReadSolarPanelsModelsSolarPanelsGetApiArg = void;
export type CreateSolarPanelModelsSolarPanelsPostApiResponse =
  /** status 201 Successful Response */ SolarPanelSchema;
export type CreateSolarPanelModelsSolarPanelsPostApiArg = {
  solarPanelCreate: SolarPanelCreate;
};
export type ReadSolarPanelModelsSolarPanelsIdGetApiResponse =
  /** status 200 Successful Response */ SolarPanelSchema;
export type ReadSolarPanelModelsSolarPanelsIdGetApiArg = {
  id: number;
};
export type UpdateSolarPanelModelsSolarPanelsIdPutApiResponse =
  /** status 200 Successful Response */ SolarPanelSchema;
export type UpdateSolarPanelModelsSolarPanelsIdPutApiArg = {
  id: number;
  solarPanelUpdate: SolarPanelUpdate;
};
export type DeleteSolarPanelModelsSolarPanelsIdDeleteApiResponse =
  /** status 200 Successful Response */ SolarPanelSchema;
export type DeleteSolarPanelModelsSolarPanelsIdDeleteApiArg = {
  id: number;
};
export type ReadWindTurbinesModelsWindTurbinesGetApiResponse =
  /** status 200 Successful Response */ WindTurbineSchema[];
export type ReadWindTurbinesModelsWindTurbinesGetApiArg = void;
export type CreateWindTurbineModelsWindTurbinesPostApiResponse =
  /** status 201 Successful Response */ WindTurbineSchema;
export type CreateWindTurbineModelsWindTurbinesPostApiArg = {
  windTurbineCreate: WindTurbineCreate;
};
export type ReadWindTurbineModelsWindTurbinesIdGetApiResponse =
  /** status 200 Successful Response */ WindTurbineSchema;
export type ReadWindTurbineModelsWindTurbinesIdGetApiArg = {
  id: number;
};
export type UpdateWindTurbineModelsWindTurbinesIdPutApiResponse =
  /** status 200 Successful Response */ WindTurbineSchema;
export type UpdateWindTurbineModelsWindTurbinesIdPutApiArg = {
  id: number;
  windTurbineUpdate: WindTurbineUpdate;
};
export type DeleteWindTurbineModelsWindTurbinesIdDeleteApiResponse =
  /** status 200 Successful Response */ WindTurbineSchema;
export type DeleteWindTurbineModelsWindTurbinesIdDeleteApiArg = {
  id: number;
};
export type ReadEnergyOutsModelsEnergyOutsGetApiResponse =
  /** status 200 Successful Response */ EnergyOutSchema[];
export type ReadEnergyOutsModelsEnergyOutsGetApiArg = void;
export type CreateEnergyOutModelsEnergyOutsPostApiResponse =
  /** status 201 Successful Response */ EnergyOutSchema;
export type CreateEnergyOutModelsEnergyOutsPostApiArg = {
  energyOutCreate: EnergyOutCreate;
};
export type ReadEnergyOutModelsEnergyOutsIdGetApiResponse =
  /** status 200 Successful Response */ EnergyOutSchema;
export type ReadEnergyOutModelsEnergyOutsIdGetApiArg = {
  id: number;
};
export type UpdateEnergyOutModelsEnergyOutsIdPutApiResponse =
  /** status 200 Successful Response */ EnergyOutSchema;
export type UpdateEnergyOutModelsEnergyOutsIdPutApiArg = {
  id: number;
  energyOutUpdate: EnergyOutUpdate;
};
export type DeleteEnergyOutModelsEnergyOutsIdDeleteApiResponse =
  /** status 200 Successful Response */ EnergyOutSchema;
export type DeleteEnergyOutModelsEnergyOutsIdDeleteApiArg = {
  id: number;
};
export type ReadProjectsProjectsGetApiResponse =
  /** status 200 Successful Response */ ProjectSchema[];
export type ReadProjectsProjectsGetApiArg = void;
export type CreateProjectProjectsPostApiResponse =
  /** status 201 Successful Response */ ProjectSchema;
export type CreateProjectProjectsPostApiArg = {
  projectCreate: ProjectCreate;
};
export type ReadProjectProjectsIdGetApiResponse =
  /** status 200 Successful Response */ ProjectSchema;
export type ReadProjectProjectsIdGetApiArg = {
  id: number;
};
export type UpdateProjectProjectsIdPutApiResponse =
  /** status 200 Successful Response */ ProjectSchema;
export type UpdateProjectProjectsIdPutApiArg = {
  id: number;
  projectUpdate: ProjectUpdate;
};
export type DeleteProjectProjectsIdDeleteApiResponse =
  /** status 200 Successful Response */ ProjectSchema;
export type DeleteProjectProjectsIdDeleteApiArg = {
  id: number;
};
export type ReadEnergyStoragesModelsEnergyStoragesGetApiResponse =
  /** status 200 Successful Response */ EnergyStorageUnitSchema[];
export type ReadEnergyStoragesModelsEnergyStoragesGetApiArg = void;
export type CreateEnergyStorageModelsEnergyStoragesPostApiResponse =
  /** status 201 Successful Response */ EnergyStorageUnitSchema;
export type CreateEnergyStorageModelsEnergyStoragesPostApiArg = {
  energyStorageUnitCreate: EnergyStorageUnitCreate;
};
export type ReadEnergyStorageModelsEnergyStoragesIdGetApiResponse =
  /** status 200 Successful Response */ EnergyStorageUnitSchema;
export type ReadEnergyStorageModelsEnergyStoragesIdGetApiArg = {
  id: number;
};
export type UpdateEnergyStorageModelsEnergyStoragesIdPutApiResponse =
  /** status 200 Successful Response */ EnergyStorageUnitSchema;
export type UpdateEnergyStorageModelsEnergyStoragesIdPutApiArg = {
  id: number;
  energyStorageUnitUpdate: EnergyStorageUnitUpdate;
};
export type DeleteEnergyStorageModelsEnergyStoragesIdDeleteApiResponse =
  /** status 200 Successful Response */ EnergyStorageUnitSchema;
export type DeleteEnergyStorageModelsEnergyStoragesIdDeleteApiArg = {
  id: number;
};
export type ReadLithiumIonsModelsLithiumIonsGetApiResponse =
  /** status 200 Successful Response */ LithiumIonBatterySchema[];
export type ReadLithiumIonsModelsLithiumIonsGetApiArg = void;
export type CreateLithiumIonModelsLithiumIonsPostApiResponse =
  /** status 201 Successful Response */ LithiumIonBatterySchema;
export type CreateLithiumIonModelsLithiumIonsPostApiArg = {
  lithiumIonBatteryCreate: LithiumIonBatteryCreate;
};
export type ReadLithiumIonModelsLithiumIonsIdGetApiResponse =
  /** status 200 Successful Response */ LithiumIonBatterySchema;
export type ReadLithiumIonModelsLithiumIonsIdGetApiArg = {
  id: number;
};
export type UpdateLithiumIonModelsLithiumIonsIdPutApiResponse =
  /** status 200 Successful Response */ LithiumIonBatterySchema;
export type UpdateLithiumIonModelsLithiumIonsIdPutApiArg = {
  id: number;
  lithiumIonBatteryUpdate: LithiumIonBatteryUpdate;
};
export type DeleteLithiumIonModelsLithiumIonsIdDeleteApiResponse =
  /** status 200 Successful Response */ LithiumIonBatterySchema;
export type DeleteLithiumIonModelsLithiumIonsIdDeleteApiArg = {
  id: number;
};
export type EnergyInSchema = {
  watts: number;
  price: number;
  daily_emissions: number;
  type: EnergyInType;
  id: number;
};
export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
export type HttpValidationError = {
  detail?: ValidationError[];
};
export type EnergyInCreate = {
  watts: number;
  price: number;
  daily_emissions: number;
  type: EnergyInType;
};
export type EnergyInUpdate = {
  watts: number | null;
  price: number | null;
  daily_emissions: number | null;
};
export type SolarPanelSchema = {
  watts: number;
  price: number;
  daily_emissions: number;
  type: EnergyInType;
  name: string;
  panel_type: SolarPanelType;
  width: number;
  length: number;
  cells: number;
  material: SolarPanelMaterial;
  id: number;
};
export type SolarPanelCreate = {
  watts: number;
  price: number;
  daily_emissions: number;
  type: EnergyInType;
  name: string;
  panel_type: SolarPanelType;
  width: number;
  length: number;
  cells: number;
  material: SolarPanelMaterial;
};
export type SolarPanelUpdate = {
  watts: number | null;
  price: number | null;
  daily_emissions: number | null;
  name: string | null;
  panel_type: SolarPanelType | null;
  width: number | null;
  length: number | null;
  cells: number | null;
  material: SolarPanelMaterial | null;
};
export type WindTurbineSchema = {
  watts: number;
  price: number;
  daily_emissions: number;
  type: EnergyInType;
  name: string;
  rotor_diameter: number;
  rotation: number;
  cut_in_speed: number;
  rated_speed: number;
  cut_off_speed: number;
  id: number;
};
export type WindTurbineCreate = {
  watts: number;
  price: number;
  daily_emissions: number;
  type: EnergyInType;
  name: string;
  rotor_diameter: number;
  rotation: number;
  cut_in_speed: number;
  rated_speed: number;
  cut_off_speed: number;
};
export type WindTurbineUpdate = {
  watts: number | null;
  price: number | null;
  daily_emissions: number | null;
  name: string | null;
  rotor_diameter: number | null;
  rotation: number | null;
  cut_in_speed: number | null;
  rated_speed: number | null;
  cut_off_speed: number | null;
};
export type EnergyOutSchema = {
  watts: number;
  daily_emissions: number;
  type: EnergyOutType;
  id: number;
};
export type EnergyOutCreate = {
  watts: number;
  daily_emissions: number;
  type: EnergyOutType;
};
export type EnergyOutUpdate = {
  watts: number | null;
  daily_emissions: number | null;
};
export type ProjectSchema = {
  id: number;
  name: string;
};
export type ProjectCreate = {
  id: number;
  name: string;
};
export type ProjectUpdate = {
  name: string | null;
};
export type EnergyStorageUnitSchema = {
  capacity: number;
  charge_level: number;
  price: number;
  type: EnergyStorageType;
  id: number;
};
export type EnergyStorageUnitCreate = {
  capacity: number;
  charge_level: number;
  price: number;
  type: EnergyStorageType;
};
export type EnergyStorageUnitUpdate = {
  capacity: number | null;
  charge_level: number | null;
  price: number | null;
};
export type LithiumIonBatterySchema = {
  max_charge_rate: number;
  name: string;
  efficiency: number;
  current: number;
  voltage: number;
  id: number;
};
export type LithiumIonBatteryCreate = {
  max_charge_rate: number;
  name: string;
  efficiency: number;
  current: number;
  voltage: number;
};
export type LithiumIonBatteryUpdate = {
  max_charge_rate: number | null;
  name: string | null;
  efficiency: number | null;
  current: number | null;
  voltage: number | null;
};
export enum EnergyInType {
  Default = "default",
  SolarPanel = "solar_panel",
  WindTurbine = "wind_turbine",
}
export enum SolarPanelType {
  Default = "default",
}
export enum SolarPanelMaterial {
  Default = "default",
}
export enum EnergyOutType {
  Default = "default",
  FactoryModel = "factory_model",
  ComplexHome = "complex_home",
  GeneralConsumer = "general_consumer",
}
export enum EnergyStorageType {
  Default = "default",
  LithiumIon = "lithium_ion",
}
export const {
  useReadEnergyInsModelsEnergyInsGetQuery,
  useCreateEnergyInModelsEnergyInsPostMutation,
  useReadEnergyInModelsEnergyInsIdGetQuery,
  useUpdateEnergyInModelsEnergyInsIdPutMutation,
  useDeleteEnergyInModelsEnergyInsIdDeleteMutation,
  useReadSolarPanelsModelsSolarPanelsGetQuery,
  useCreateSolarPanelModelsSolarPanelsPostMutation,
  useReadSolarPanelModelsSolarPanelsIdGetQuery,
  useUpdateSolarPanelModelsSolarPanelsIdPutMutation,
  useDeleteSolarPanelModelsSolarPanelsIdDeleteMutation,
  useReadWindTurbinesModelsWindTurbinesGetQuery,
  useCreateWindTurbineModelsWindTurbinesPostMutation,
  useReadWindTurbineModelsWindTurbinesIdGetQuery,
  useUpdateWindTurbineModelsWindTurbinesIdPutMutation,
  useDeleteWindTurbineModelsWindTurbinesIdDeleteMutation,
  useReadEnergyOutsModelsEnergyOutsGetQuery,
  useCreateEnergyOutModelsEnergyOutsPostMutation,
  useReadEnergyOutModelsEnergyOutsIdGetQuery,
  useUpdateEnergyOutModelsEnergyOutsIdPutMutation,
  useDeleteEnergyOutModelsEnergyOutsIdDeleteMutation,
  useReadProjectsProjectsGetQuery,
  useCreateProjectProjectsPostMutation,
  useReadProjectProjectsIdGetQuery,
  useUpdateProjectProjectsIdPutMutation,
  useDeleteProjectProjectsIdDeleteMutation,
  useReadEnergyStoragesModelsEnergyStoragesGetQuery,
  useCreateEnergyStorageModelsEnergyStoragesPostMutation,
  useReadEnergyStorageModelsEnergyStoragesIdGetQuery,
  useUpdateEnergyStorageModelsEnergyStoragesIdPutMutation,
  useDeleteEnergyStorageModelsEnergyStoragesIdDeleteMutation,
  useReadLithiumIonsModelsLithiumIonsGetQuery,
  useCreateLithiumIonModelsLithiumIonsPostMutation,
  useReadLithiumIonModelsLithiumIonsIdGetQuery,
  useUpdateLithiumIonModelsLithiumIonsIdPutMutation,
  useDeleteLithiumIonModelsLithiumIonsIdDeleteMutation,
} = injectedRtkApi;

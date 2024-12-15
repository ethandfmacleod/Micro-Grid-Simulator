import { emptySplitApi as api } from "./emptyApi";
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    objectsList: build.query<ObjectsListApiResponse, ObjectsListApiArg>({
      query: (queryArg) => ({
        url: `/api/objects/`,
        params: {
          projectID: queryArg.projectId,
        },
      }),
    }),
    objectsCreate: build.mutation<
      ObjectsCreateApiResponse,
      ObjectsCreateApiArg
    >({
      query: (queryArg) => ({
        url: `/api/objects/`,
        method: "POST",
        body: queryArg.objectBase,
      }),
    }),
    objectsRetrieve: build.query<
      ObjectsRetrieveApiResponse,
      ObjectsRetrieveApiArg
    >({
      query: (queryArg) => ({ url: `/api/objects/${queryArg.id}/` }),
    }),
    objectsUpdate: build.mutation<
      ObjectsUpdateApiResponse,
      ObjectsUpdateApiArg
    >({
      query: (queryArg) => ({
        url: `/api/objects/${queryArg.id}/`,
        method: "PUT",
        body: queryArg.objectBase,
      }),
    }),
    objectsPartialUpdate: build.mutation<
      ObjectsPartialUpdateApiResponse,
      ObjectsPartialUpdateApiArg
    >({
      query: (queryArg) => ({
        url: `/api/objects/${queryArg.id}/`,
        method: "PATCH",
        body: queryArg.patchedObjectBase,
      }),
    }),
    objectsDestroy: build.mutation<
      ObjectsDestroyApiResponse,
      ObjectsDestroyApiArg
    >({
      query: (queryArg) => ({
        url: `/api/objects/${queryArg.id}/`,
        method: "DELETE",
      }),
    }),
    projectsList: build.query<ProjectsListApiResponse, ProjectsListApiArg>({
      query: () => ({ url: `/api/projects/` }),
    }),
    projectsCreate: build.mutation<
      ProjectsCreateApiResponse,
      ProjectsCreateApiArg
    >({
      query: (queryArg) => ({
        url: `/api/projects/`,
        method: "POST",
        body: queryArg.project,
      }),
    }),
    projectsRetrieve: build.query<
      ProjectsRetrieveApiResponse,
      ProjectsRetrieveApiArg
    >({
      query: (queryArg) => ({ url: `/api/projects/${queryArg.id}/` }),
    }),
    projectsUpdate: build.mutation<
      ProjectsUpdateApiResponse,
      ProjectsUpdateApiArg
    >({
      query: (queryArg) => ({
        url: `/api/projects/${queryArg.id}/`,
        method: "PUT",
        body: queryArg.project,
      }),
    }),
    projectsPartialUpdate: build.mutation<
      ProjectsPartialUpdateApiResponse,
      ProjectsPartialUpdateApiArg
    >({
      query: (queryArg) => ({
        url: `/api/projects/${queryArg.id}/`,
        method: "PATCH",
        body: queryArg.patchedProject,
      }),
    }),
    projectsDestroy: build.mutation<
      ProjectsDestroyApiResponse,
      ProjectsDestroyApiArg
    >({
      query: (queryArg) => ({
        url: `/api/projects/${queryArg.id}/`,
        method: "DELETE",
      }),
    }),
    schemaRetrieve: build.query<
      SchemaRetrieveApiResponse,
      SchemaRetrieveApiArg
    >({
      query: (queryArg) => ({
        url: `/api/schema/`,
        params: {
          format: queryArg.format,
          lang: queryArg.lang,
        },
      }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as api };
export type ObjectsListApiResponse = /** status 200  */ ObjectBaseRead[];
export type ObjectsListApiArg = {
  projectId: number;
};
export type ObjectsCreateApiResponse = /** status 201  */ ObjectBaseRead;
export type ObjectsCreateApiArg = {
  objectBase: ObjectBase;
};
export type ObjectsRetrieveApiResponse = /** status 200  */ ObjectBaseRead;
export type ObjectsRetrieveApiArg = {
  /** A unique integer value identifying this object base. */
  id: number;
};
export type ObjectsUpdateApiResponse = /** status 200  */ ObjectBaseRead;
export type ObjectsUpdateApiArg = {
  /** A unique integer value identifying this object base. */
  id: number;
  objectBase: ObjectBase;
};
export type ObjectsPartialUpdateApiResponse = /** status 200  */ ObjectBaseRead;
export type ObjectsPartialUpdateApiArg = {
  /** A unique integer value identifying this object base. */
  id: number;
  patchedObjectBase: PatchedObjectBase;
};
export type ObjectsDestroyApiResponse = unknown;
export type ObjectsDestroyApiArg = {
  /** A unique integer value identifying this object base. */
  id: number;
};
export type ProjectsListApiResponse = /** status 200  */ ProjectRead[];
export type ProjectsListApiArg = void;
export type ProjectsCreateApiResponse = /** status 201  */ ProjectRead;
export type ProjectsCreateApiArg = {
  project: Project;
};
export type ProjectsRetrieveApiResponse = /** status 200  */ ProjectRead;
export type ProjectsRetrieveApiArg = {
  /** A unique integer value identifying this project. */
  id: number;
};
export type ProjectsUpdateApiResponse = /** status 200  */ ProjectRead;
export type ProjectsUpdateApiArg = {
  /** A unique integer value identifying this project. */
  id: number;
  project: Project;
};
export type ProjectsPartialUpdateApiResponse = /** status 200  */ ProjectRead;
export type ProjectsPartialUpdateApiArg = {
  /** A unique integer value identifying this project. */
  id: number;
  patchedProject: PatchedProject;
};
export type ProjectsDestroyApiResponse = unknown;
export type ProjectsDestroyApiArg = {
  /** A unique integer value identifying this project. */
  id: number;
};
export type SchemaRetrieveApiResponse = /** status 200  */ {
  [key: string]: any;
};
export type SchemaRetrieveApiArg = {
  format?: "json" | "yaml";
  lang?:
    | "af"
    | "ar"
    | "ar-dz"
    | "ast"
    | "az"
    | "be"
    | "bg"
    | "bn"
    | "br"
    | "bs"
    | "ca"
    | "ckb"
    | "cs"
    | "cy"
    | "da"
    | "de"
    | "dsb"
    | "el"
    | "en"
    | "en-au"
    | "en-gb"
    | "eo"
    | "es"
    | "es-ar"
    | "es-co"
    | "es-mx"
    | "es-ni"
    | "es-ve"
    | "et"
    | "eu"
    | "fa"
    | "fi"
    | "fr"
    | "fy"
    | "ga"
    | "gd"
    | "gl"
    | "he"
    | "hi"
    | "hr"
    | "hsb"
    | "hu"
    | "hy"
    | "ia"
    | "id"
    | "ig"
    | "io"
    | "is"
    | "it"
    | "ja"
    | "ka"
    | "kab"
    | "kk"
    | "km"
    | "kn"
    | "ko"
    | "ky"
    | "lb"
    | "lt"
    | "lv"
    | "mk"
    | "ml"
    | "mn"
    | "mr"
    | "ms"
    | "my"
    | "nb"
    | "ne"
    | "nl"
    | "nn"
    | "os"
    | "pa"
    | "pl"
    | "pt"
    | "pt-br"
    | "ro"
    | "ru"
    | "sk"
    | "sl"
    | "sq"
    | "sr"
    | "sr-latn"
    | "sv"
    | "sw"
    | "ta"
    | "te"
    | "tg"
    | "th"
    | "tk"
    | "tr"
    | "tt"
    | "udm"
    | "ug"
    | "uk"
    | "ur"
    | "uz"
    | "vi"
    | "zh-hans"
    | "zh-hant";
};
export type ObjectBase = {
  name?: string;
  object_type?: ObjectTypeEnum;
  project: number;
  property_set?: number | null;
};
export type ObjectBaseRead = {
  id: number;
  name?: string;
  object_type?: ObjectTypeEnum;
  project: number;
  property_set?: number | null;
};
export type PatchedObjectBase = {
  name?: string;
  object_type?: ObjectTypeEnum;
  project?: number;
  property_set?: number | null;
};
export type PatchedObjectBaseRead = {
  id?: number;
  name?: string;
  object_type?: ObjectTypeEnum;
  project?: number;
  property_set?: number | null;
};
export type Project = {
  name?: string;
  date?: string | null;
};
export type ProjectRead = {
  id: number;
  name?: string;
  date?: string | null;
};
export type PatchedProject = {
  name?: string;
  date?: string | null;
};
export type PatchedProjectRead = {
  id?: number;
  name?: string;
  date?: string | null;
};
export enum ObjectTypeEnum {
  SolarPanel = "solar_panel",
  WindTurbine = "wind_turbine",
  FactoryModel = "factory_model",
  ComplexHome = "complex_home",
  GeneralConsumer = "general_consumer",
  LithiumIon = "lithium_ion",
}
export const {
  useObjectsListQuery,
  useObjectsCreateMutation,
  useObjectsRetrieveQuery,
  useObjectsUpdateMutation,
  useObjectsPartialUpdateMutation,
  useObjectsDestroyMutation,
  useProjectsListQuery,
  useProjectsCreateMutation,
  useProjectsRetrieveQuery,
  useProjectsUpdateMutation,
  useProjectsPartialUpdateMutation,
  useProjectsDestroyMutation,
  useSchemaRetrieveQuery,
} = injectedRtkApi;

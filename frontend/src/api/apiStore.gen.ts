import { emptySplitApi as api } from "./emptyApi";
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    edgesList: build.query<EdgesListApiResponse, EdgesListApiArg>({
      query: (queryArg) => ({
        url: `/api/edges/`,
        params: {
          projectID: queryArg.projectId,
        },
      }),
    }),
    edgesCreate: build.mutation<EdgesCreateApiResponse, EdgesCreateApiArg>({
      query: (queryArg) => ({
        url: `/api/edges/`,
        method: "POST",
        body: queryArg.edge,
      }),
    }),
    edgesRetrieve: build.query<EdgesRetrieveApiResponse, EdgesRetrieveApiArg>({
      query: (queryArg) => ({ url: `/api/edges/${queryArg.id}/` }),
    }),
    edgesUpdate: build.mutation<EdgesUpdateApiResponse, EdgesUpdateApiArg>({
      query: (queryArg) => ({
        url: `/api/edges/${queryArg.id}/`,
        method: "PUT",
        body: queryArg.edge,
      }),
    }),
    edgesPartialUpdate: build.mutation<
      EdgesPartialUpdateApiResponse,
      EdgesPartialUpdateApiArg
    >({
      query: (queryArg) => ({
        url: `/api/edges/${queryArg.id}/`,
        method: "PATCH",
        body: queryArg.patchedEdge,
      }),
    }),
    edgesDestroy: build.mutation<EdgesDestroyApiResponse, EdgesDestroyApiArg>({
      query: (queryArg) => ({
        url: `/api/edges/${queryArg.id}/`,
        method: "DELETE",
      }),
    }),
    nodesList: build.query<NodesListApiResponse, NodesListApiArg>({
      query: (queryArg) => ({
        url: `/api/nodes/`,
        params: {
          projectID: queryArg.projectId,
        },
      }),
    }),
    nodesCreate: build.mutation<NodesCreateApiResponse, NodesCreateApiArg>({
      query: (queryArg) => ({
        url: `/api/nodes/`,
        method: "POST",
        body: queryArg.node,
      }),
    }),
    nodesRetrieve: build.query<NodesRetrieveApiResponse, NodesRetrieveApiArg>({
      query: (queryArg) => ({ url: `/api/nodes/${queryArg.id}/` }),
    }),
    nodesUpdate: build.mutation<NodesUpdateApiResponse, NodesUpdateApiArg>({
      query: (queryArg) => ({
        url: `/api/nodes/${queryArg.id}/`,
        method: "PUT",
        body: queryArg.node,
      }),
    }),
    nodesPartialUpdate: build.mutation<
      NodesPartialUpdateApiResponse,
      NodesPartialUpdateApiArg
    >({
      query: (queryArg) => ({
        url: `/api/nodes/${queryArg.id}/`,
        method: "PATCH",
        body: queryArg.patchedNode,
      }),
    }),
    nodesDestroy: build.mutation<NodesDestroyApiResponse, NodesDestroyApiArg>({
      query: (queryArg) => ({
        url: `/api/nodes/${queryArg.id}/`,
        method: "DELETE",
      }),
    }),
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
    setsList: build.query<SetsListApiResponse, SetsListApiArg>({
      query: (queryArg) => ({
        url: `/api/sets/`,
        params: {
          projectID: queryArg.projectId,
        },
      }),
    }),
    setsCreate: build.mutation<SetsCreateApiResponse, SetsCreateApiArg>({
      query: (queryArg) => ({
        url: `/api/sets/`,
        method: "POST",
        body: queryArg.propertySet,
      }),
    }),
    setsRetrieve: build.query<SetsRetrieveApiResponse, SetsRetrieveApiArg>({
      query: (queryArg) => ({ url: `/api/sets/${queryArg.id}/` }),
    }),
    setsUpdate: build.mutation<SetsUpdateApiResponse, SetsUpdateApiArg>({
      query: (queryArg) => ({
        url: `/api/sets/${queryArg.id}/`,
        method: "PUT",
        body: queryArg.propertySet,
      }),
    }),
    setsPartialUpdate: build.mutation<
      SetsPartialUpdateApiResponse,
      SetsPartialUpdateApiArg
    >({
      query: (queryArg) => ({
        url: `/api/sets/${queryArg.id}/`,
        method: "PATCH",
        body: queryArg.patchedPropertySet,
      }),
    }),
    setsDestroy: build.mutation<SetsDestroyApiResponse, SetsDestroyApiArg>({
      query: (queryArg) => ({
        url: `/api/sets/${queryArg.id}/`,
        method: "DELETE",
      }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as api };
export type EdgesListApiResponse = /** status 200  */ EdgeRead[];
export type EdgesListApiArg = {
  projectId: number;
};
export type EdgesCreateApiResponse = /** status 201  */ EdgeRead;
export type EdgesCreateApiArg = {
  edge: Edge;
};
export type EdgesRetrieveApiResponse = /** status 200  */ EdgeRead;
export type EdgesRetrieveApiArg = {
  /** A unique integer value identifying this edge. */
  id: number;
};
export type EdgesUpdateApiResponse = /** status 200  */ EdgeRead;
export type EdgesUpdateApiArg = {
  /** A unique integer value identifying this edge. */
  id: number;
  edge: Edge;
};
export type EdgesPartialUpdateApiResponse = /** status 200  */ EdgeRead;
export type EdgesPartialUpdateApiArg = {
  /** A unique integer value identifying this edge. */
  id: number;
  patchedEdge: PatchedEdge;
};
export type EdgesDestroyApiResponse = unknown;
export type EdgesDestroyApiArg = {
  /** A unique integer value identifying this edge. */
  id: number;
};
export type NodesListApiResponse = /** status 200  */ NodeRead[];
export type NodesListApiArg = {
  projectId: number;
};
export type NodesCreateApiResponse = /** status 201  */ NodeRead;
export type NodesCreateApiArg = {
  node: Node;
};
export type NodesRetrieveApiResponse = /** status 200  */ NodeRead;
export type NodesRetrieveApiArg = {
  /** A unique integer value identifying this node. */
  id: number;
};
export type NodesUpdateApiResponse = /** status 200  */ NodeRead;
export type NodesUpdateApiArg = {
  /** A unique integer value identifying this node. */
  id: number;
  node: Node;
};
export type NodesPartialUpdateApiResponse = /** status 200  */ NodeRead;
export type NodesPartialUpdateApiArg = {
  /** A unique integer value identifying this node. */
  id: number;
  patchedNode: PatchedNode;
};
export type NodesDestroyApiResponse = unknown;
export type NodesDestroyApiArg = {
  /** A unique integer value identifying this node. */
  id: number;
};
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
export type SetsListApiResponse = /** status 200  */ PropertySetRead[];
export type SetsListApiArg = {
  projectId: number;
};
export type SetsCreateApiResponse = /** status 201  */ PropertySetRead;
export type SetsCreateApiArg = {
  propertySet: PropertySet;
};
export type SetsRetrieveApiResponse = /** status 200  */ PropertySetRead;
export type SetsRetrieveApiArg = {
  /** A unique integer value identifying this property set. */
  id: number;
};
export type SetsUpdateApiResponse = /** status 200  */ PropertySetRead;
export type SetsUpdateApiArg = {
  /** A unique integer value identifying this property set. */
  id: number;
  propertySet: PropertySet;
};
export type SetsPartialUpdateApiResponse = /** status 200  */ PropertySetRead;
export type SetsPartialUpdateApiArg = {
  /** A unique integer value identifying this property set. */
  id: number;
  patchedPropertySet: PatchedPropertySet;
};
export type SetsDestroyApiResponse = unknown;
export type SetsDestroyApiArg = {
  /** A unique integer value identifying this property set. */
  id: number;
};
export type Edge = {
  project: number;
};
export type EdgeRead = {
  id: string;
  source: string;
  target: string;
  project: number;
};
export type PatchedEdge = {
  project?: number;
};
export type PatchedEdgeRead = {
  id?: string;
  source?: string;
  target?: string;
  project?: number;
};
export type NodePosition = {
  x: number;
  y: number;
};
export type Node = {
  position: NodePosition;
  type?: TypeEnum;
};
export type NodeRead = {
  id: string;
  position: NodePosition;
  data: {
    [key: string]: any;
  };
  type?: TypeEnum;
};
export type PatchedNode = {
  position?: NodePosition;
  type?: TypeEnum;
};
export type PatchedNodeRead = {
  id?: string;
  position?: NodePosition;
  data?: {
    [key: string]: any;
  };
  type?: TypeEnum;
};
export type ObjectBase = {
  name?: string;
  type?: TypeEnum;
  project: number;
  property_set?: number | null;
};
export type ObjectBaseRead = {
  id: number;
  name?: string;
  type?: TypeEnum;
  project: number;
  property_set?: number | null;
};
export type PatchedObjectBase = {
  name?: string;
  type?: TypeEnum;
  project?: number;
  property_set?: number | null;
};
export type PatchedObjectBaseRead = {
  id?: number;
  name?: string;
  type?: TypeEnum;
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
export type PropertySet = {
  name?: string;
};
export type PropertyInfo = {
  display_type?: DisplayTypeEnum;
  value?: any | null;
  key: string;
  display_name: string;
  set: number;
};
export type PropertyInfoRead = {
  id: number;
  display_type?: DisplayTypeEnum;
  value?: any | null;
  key: string;
  display_name: string;
  set: number;
};
export type PropertySetRead = {
  id: number;
  properties: PropertyInfoRead[];
  name?: string;
};
export type PatchedPropertySet = {
  name?: string;
};
export type PatchedPropertySetRead = {
  id?: number;
  properties?: PropertyInfoRead[];
  name?: string;
};
export enum TypeEnum {
  SolarPanel = "solar_panel",
  WindTurbine = "wind_turbine",
  FactoryModel = "factory_model",
  ComplexHome = "complex_home",
  GeneralConsumer = "general_consumer",
  LithiumIon = "lithium_ion",
}
export enum DisplayTypeEnum {
  Numeric = "numeric",
  Dropdown = "dropdown",
  Checkbox = "checkbox",
  Segmented = "segmented",
  Text = "text",
}
export const {
  useEdgesListQuery,
  useEdgesCreateMutation,
  useEdgesRetrieveQuery,
  useEdgesUpdateMutation,
  useEdgesPartialUpdateMutation,
  useEdgesDestroyMutation,
  useNodesListQuery,
  useNodesCreateMutation,
  useNodesRetrieveQuery,
  useNodesUpdateMutation,
  useNodesPartialUpdateMutation,
  useNodesDestroyMutation,
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
  useSetsListQuery,
  useSetsCreateMutation,
  useSetsRetrieveQuery,
  useSetsUpdateMutation,
  useSetsPartialUpdateMutation,
  useSetsDestroyMutation,
} = injectedRtkApi;

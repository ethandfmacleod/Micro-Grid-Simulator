import { useUrlParam } from "./params";

export function useProjectId() {
  return +useUrlParam("projectId")!;
}
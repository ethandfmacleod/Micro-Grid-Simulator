import { ProjectRead, useProjectsListQuery } from "@/api/apiStore.gen";
import { useUrlParam } from "./params";

// Retrieves current project from url param
export function useProjectId(): number {
  return +useUrlParam("projectId")!;
}

// Returns all project objects
export function useProjects(): ProjectRead[] {
  const { data: projects } = useProjectsListQuery();
  return projects ?? [];
}

// Returns the current project object
export function useCurrentProject(): ProjectRead | undefined {
  const projects: ProjectRead[] = useProjects();
  const projectID: number = useProjectId();
  return projects.find(p => p.id === projectID);
}
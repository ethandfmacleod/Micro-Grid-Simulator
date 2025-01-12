import { ScrollArea } from "@/components/ui/scroll-area";
import { ProjectCard } from "./ProjectCard";
import { useHandleDeleteProject, useProjects } from "@/hooks/project";
import { ProjectRead } from "@/api/apiStore.gen";

export const ProjectList = () => {
    const projects: ProjectRead[] = useProjects();
    const handleDeleteProject = useHandleDeleteProject();
    
    return (
        <ScrollArea className="h-screen w-full">
            <div className="grid grid-cols-[repeat(auto-fit,minmax(300px,1fr))] gap-6">
                {
                    projects?.map((project, index) => {
                        return (
                            <ProjectCard
                                title={project.name!}
                                date={project.date!}
                                projectId={project.id!}
                                key={index}
                                deleteProject={handleDeleteProject}
                            />
                        )
                    })
                }
            </div>
        </ScrollArea>
    );
}
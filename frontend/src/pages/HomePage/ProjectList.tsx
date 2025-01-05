import { ProjectCard } from "./ProjectCard";
import { useProjects } from "@/hooks/project";

export const ProjectList = () => {
    const projects = useProjects();
    return (
        <div className="grid grid-cols-[repeat(auto-fit,minmax(300px,1fr))] gap-6">
            {
                projects?.map((project, index) => {
                    return (
                        <ProjectCard
                            title={project.name!}
                            date={project.date!}
                            projectId={project.id!}
                            key={index}
                        />
                    )
                })
            }
        </div>
    );
}
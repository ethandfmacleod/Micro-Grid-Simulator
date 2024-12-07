import { useReadProjectsProjectsGetQuery } from "@/api/apiStore.gen";
import { ProjectCard } from "./ProjectCard";

export const ProjectList = () => {
    const { data: projects } = useReadProjectsProjectsGetQuery();
    return (
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-6">
        {
            projects?.map((project, index) => {
                return (
                    <ProjectCard
                        title={project.name!} 
                        date={project.created_at!}
                        projectId={project.id!}
                        key={index} 
                    />
                )
            })
        }
    </div>
    );
}
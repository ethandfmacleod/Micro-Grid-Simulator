import { useReadProjectsProjectsGetQuery } from "@/api/apiStore.gen";
import { Button } from "@/components/ui/button";
import { useNavigate } from "react-router-dom";
import { ProjectCard } from "./ProjectCard";

const SelectProject = () => {
    const navigate = useNavigate();
    const {data: projects} = useReadProjectsProjectsGetQuery();
    const onCreateClick = () => {

    };

    return (
        <div className="px-12">
            <div className="flex flex-row my-12">
                <Button variant="primary">
                    Create New Project
                </Button>
            </div>
            <div className="grid sm:grid-cols-2 md:grid-cols-3 grid-cols-5 gap-6">
                {
                    projects?.map((project, index) => {
                        return(
                            <ProjectCard title={project.name} key={index}/>
                        )
                    })
                }
            </div>
        </div>
    );
}

export default SelectProject;
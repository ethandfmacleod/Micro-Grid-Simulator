import { ProjectSchema, useCreateProjectProjectsPostMutation } from "@/api/apiStore.gen";
import { Button } from "@/components/ui/button";
import { useNavigate } from "react-router-dom";
import { ProjectList } from "./ProjectList";

const SelectProject = () => {
    const navigate = useNavigate();
    const [createProject] = useCreateProjectProjectsPostMutation();

    const handleCreate = async () => {
        await createProject({ projectCreate: {} })
            .unwrap()
            .then((project: ProjectSchema) => {
                navigate(`/project/${project.id}/design`);
            })
    };

    return (
        <div className="px-12">
            <div className="flex flex-row my-12">
                <Button variant="primary" onClick={handleCreate}>
                    Create New Project
                </Button>
            </div>
            <ProjectList/>
        </div>
    );
}

export default SelectProject;
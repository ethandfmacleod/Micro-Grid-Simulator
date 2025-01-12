import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Trash2 } from "lucide-react";
import { Link } from "react-router-dom";

interface ProjectCardProps {
    title: string;
    date?: string;
    projectId: number;
    deleteProject: (project: number) => void;
}

// A single project display for the home page
export const ProjectCard = ({ title, date, projectId, deleteProject }: ProjectCardProps) => {
    return (
        <Link to={`/project/${projectId}/design`} className="block">
            <Card className="w-[350px]">
                <CardHeader>
                    <CardTitle>{title}</CardTitle>
                    <CardDescription>No description provided</CardDescription>
                </CardHeader>
                <CardFooter className="flex justify-between">
                    <p>{date}</p>
                    <Button 
                        size={"icon"} 
                        onClick={(e) => {e.preventDefault(), deleteProject(projectId)}} 
                        variant={"ghost"}
                        className="hover:bg-red-500 hover:text-white"
                    >
                        <Trash2/>
                    </Button>
                </CardFooter>
            </Card>
        </Link>
    );
}

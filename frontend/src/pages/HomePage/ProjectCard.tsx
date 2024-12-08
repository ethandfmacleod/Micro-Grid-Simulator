import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Link } from "react-router-dom";

interface ProjectCardProps {
    title: string;
    date?: string;
    projectId: number;
}

// A single project display for the home page
export const ProjectCard = ({ title, date, projectId }: ProjectCardProps) => {
    return (
        <Link to={`/project/${projectId}/design`} className="block">
            <Card className="w-[350px]">
                <CardHeader>
                    <CardTitle>{title}</CardTitle>
                    <CardDescription>Some Project Description</CardDescription>
                </CardHeader>
                <CardContent>
                    <h2>Image here lol</h2>
                </CardContent>
                <CardFooter className="flex justify-between">
                    <p>{date}</p>
                    <p>User Name</p>
                </CardFooter>
            </Card>
        </Link>
    );
}

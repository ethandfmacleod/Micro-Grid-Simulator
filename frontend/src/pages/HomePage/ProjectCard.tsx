import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"

interface ProjectCardProps {
    title: string,
    date?: string,
}

export const ProjectCard = ({title, date}: ProjectCardProps) => {
    return(
        <Card className="w-[350px]">
            <CardHeader>
                <CardTitle>{title}</CardTitle>
                <CardDescription>Some Project Description</CardDescription>
            </CardHeader>
            <CardContent>
                <h2>Image here lol</h2>
            </CardContent>
            <CardFooter className="flex justify-between">
                <p>{date || "Some Date"}</p>
                <p>User Name</p>
            </CardFooter>
        </Card>
    );
}
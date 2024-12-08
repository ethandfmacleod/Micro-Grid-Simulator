import NavBar from "../NavBar";

const StartPage = ({ children }: { children: React.ReactNode }) => {
    return (
        <div className="flex flex-col w-screen h-screen overflow-hidden bg-background text-foreground">
            <NavBar />
            {children}
        </div>
    );
};

export default StartPage;
import { Link } from "react-router-dom";
import { ModeToggle } from "./ModeToggle";

function NavBar() {
    return (
        <header className="shadow-md shadow-accent px-6">
            <nav className="flex items-center justify-between py-2">
                {/* Logo */}
                <div className="text-xl font-semibold">
                    <a href="/">Microgrid Simulator</a>
                </div>

                {/* Navigation Links */}
                <ul className="hidden md:flex">
                    <Link to="/">Github</Link>
                </ul>

                {/* Call to Action */}
                <div className="hidden md:block">
                    <ModeToggle/>
                </div>
            </nav>
        </header>
    );
};

export default NavBar
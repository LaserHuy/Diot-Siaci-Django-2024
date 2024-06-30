import { Link } from "react-router-dom";

const Header = () => {
    return (
        <header className="w-[90%] flex justify-between items-center sm:px-8 px-4 py-4 fixed top-0 z-10">
            <Link to="/" className="flex text-white items-center text-2xl font-bold">
                <img src="./logo.svg" alt="logo" />
                <h2 className="ml-5">Blog Multi-lang</h2>
            </Link>
            <nav>
                <ul className="flex space-x-4">
                    <li>
                        <Link to="/" className="text-white">Home</Link>
                    </li>
                    <li>
                        <Link to="/chatbot" className="text-white">Create Post</Link>
                    </li>
                    <li>
                        <Link to="/" className="font-inter bg-transparent border text-white px-8 py-2 rounded-lg hover:bg-gradient-to-r from-purple-500 via-blue-500 to-blue-700">FR</Link>
                    </li>
                    <li>
                        <Link to="/" className="font-inter border text-white px-8 py-2 rounded-lg bg-gradient-to-r from-purple-500 via-blue-500 to-blue-700">EN</Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
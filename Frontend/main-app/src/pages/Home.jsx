import Footer from "../components/Footer";

const Home = () => {
    return (
        <div className="landingpage">
            <main className="sm:p-8 px-4 py-8 w-full min-h-[calc(100vh-73px)]">
                <h1 className="text-white text-3xl font-bold text-center">Welcome to the Main App</h1>
            </main>
            <Footer />
        </div>
    );
};

export default Home;
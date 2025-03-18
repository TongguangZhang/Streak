"use client"

import { useRouter } from "next/navigation"

const Navbar = () => {
    const router = useRouter()
    return (
        <header className="bg-[#121212] text-white p-4 fixed top-0 left-0 w-full z-50">
            <div className="flex justify-between items-center">
                {/* Logo Section */}
                <div className="flex items-center space-x-4">
                    <button
                        onClick={() => router.push("/")}
                        className="hover:text-[#1DB954] transition duration-200"
                    >
                        Streak
                    </button>
                </div>

                {/* Center Navigation Links */}
                <nav className="hidden md:flex space-x-6">
                    <button
                        onClick={() => router.push("/home")}
                        className="hover:text-[#1DB954] transition duration-200"
                    >
                        Dashboard
                    </button>
                    <button
                        onClick={() => router.push("/weeks")}
                        className="hover:text-[#1DB954] transition duration-200"
                    >
                        Past Weeks
                    </button>
                </nav>

                {/* User Profile and Hamburger */}
                <div className="flex items-center space-x-4">
                    <div className="hidden md:block">
                        <button className="hover:text-[#1DB954] transition duration-200">
                            Log in
                        </button>
                    </div>
                </div>
            </div>
        </header>
    )
}

export default Navbar


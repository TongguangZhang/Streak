import { useState } from "react"
import api from "@/api"

const GoalForm = () => {
    const [formData, setFormData] = useState({
        name: "",
        count: "",
    })

    const [loading, setLoading] = useState(false) // Loading state
    const [error, setError] = useState<string | null>(null) // Error state
    const [success, setSuccess] = useState<string | null>(null) // Success message

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target
        setFormData((prev) => ({
            ...prev,
            [name]: value,
        }))
    }

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        setLoading(true)
        setError(null)
        setSuccess(null)
        try {
            const create_goal_response = await api.post("goal_crud", {
                name: formData.name,
                count: parseInt(formData.count),
            })
            const week = await api.get("checklist/latest_week")
            const weekly_goal_response = await api.post("weekly_goal_crud", {
                week_id: week.data.id,
                goal_id: create_goal_response.data.id,
            })
            setSuccess("Goal added successfully!")
            setFormData({ name: "", count: "" }) // Clear the form on success
        } catch (error: any) {
            console.error("Error adding goal:", error)
            setError("Failed to add goal. Please try again.")
        } finally {
            setLoading(false)
        }
    }

    return (
        <form
            onSubmit={handleSubmit}
            className="bg-white p-6 rounded-lg shadow-md max-w-md mx-auto space-y-4"
        >
            <h2 className="text-xl font-semibold text-center mb-4">Add a New Goal</h2>

            <div>
                <label htmlFor="name" className="block text-gray-700 mb-1">
                    Goal Name
                </label>
                <input
                    type="text"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                    placeholder="Enter goal name"
                    className="block text-gray-700 mb-1 w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
                />
            </div>

            <div>
                <label htmlFor="count" className="block text-gray-700 mb-1">
                    Goal Count
                </label>
                <input
                    type="number"
                    id="count"
                    name="count"
                    value={formData.count}
                    onChange={handleChange}
                    required
                    placeholder="Enter count"
                    className="block text-gray-700 mb-1 w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
                />
            </div>

            <button
                type="submit"
                disabled={loading}
                className={`w-full py-2 text-white font-semibold rounded-lg shadow-md transition duration-200 ${
                    loading ? "bg-gray-400" : "bg-blue-600 hover:bg-blue-700"
                }`}
            >
                {loading ? "Adding..." : "+ Add Goal"}
            </button>

            {error && <p className="text-red-500 text-center mt-2">{error}</p>}
            {success && <p className="text-green-500 text-center mt-2">{success}</p>}
        </form>
    )
}

export default GoalForm


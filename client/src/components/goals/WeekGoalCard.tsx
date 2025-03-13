import { useState } from "react"
import { motion } from "framer-motion"
import { CombinedGoal } from "@/types/week_admin_responses"
import api from "@/api"
import { Trophy } from "lucide-react"

const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

const WeekGoalCard = (combinedGoal: CombinedGoal) => {
    const checkData = days.map((day) => !!combinedGoal[day.toLowerCase() as keyof CombinedGoal])
    const [checked, setChecked] = useState<boolean[]>(checkData)

    const todayIndex = new Date().getDay() - 1 // Adjusting for zero-based Sunday start
    const adjustedTodayIndex = todayIndex === -1 ? 6 : todayIndex

    const handleCheck = async (index: number) => {
        const newChecked = [...checked]
        newChecked[index] = !newChecked[index]
        setChecked(newChecked)

        try {
            if (newChecked[index]) {
                await api.patch(
                    `check/${combinedGoal.id}/check_day?day=${days[index].toLowerCase()}`
                )
            } else {
                await api.patch(
                    `check/${combinedGoal.id}/uncheck_day?day=${days[index].toLowerCase()}`
                )
            }
        } catch (error) {
            console.error("Error updating check status:", error)
        }
    }

    const completedCount = checked.reduce((sum, val) => sum + (val ? 1 : 0), 0)
    const isCompleted = completedCount >= combinedGoal.count

    return (
        <motion.div
            className={`p-6 rounded-2xl shadow-lg max-w-lg mx-auto mb-6 transition-all transform duration-300 relative overflow-hidden 
                ${isCompleted ? "bg-green-500 text-white" : "bg-gray-50 text-gray-900"}`}
            whileHover={{ scale: 1.05 }}
        >
            <div className="flex justify-between items-center mb-4">
                <h2 className="text-lg font-bold">{combinedGoal.name}</h2>
                <span className="flex items-center gap-2 bg-blue-600 text-white text-xs px-3 py-1 rounded-full font-semibold">
                    {isCompleted && <Trophy size={14} />} {completedCount} / {combinedGoal.count}{" "}
                    Completed
                </span>
            </div>

            <div className="flex flex-col items-center">
                <div className="grid grid-cols-7 gap-3 mb-3 text-sm font-medium text-gray-500">
                    {days.map((day, index) => (
                        <span
                            key={index}
                            className={`text-center w-10 p-1 rounded-md ${
                                index === adjustedTodayIndex ? "bg-blue-500 text-white" : ""
                            }`}
                        >
                            {day}
                        </span>
                    ))}
                </div>
                <div className="grid grid-cols-7 gap-3">
                    {Array.from({ length: 7 }).map((_, index) => (
                        <motion.button
                            key={index}
                            onClick={() => handleCheck(index)}
                            className={`h-10 w-10 flex items-center justify-center rounded-lg transition-all border 
                                ${
                                    checked[index]
                                        ? "bg-green-500 text-white border-green-600"
                                        : "bg-gray-200 border-gray-300"
                                }`}
                            whileTap={{ scale: 0.9 }}
                        >
                            {checked[index] && "✔"}
                        </motion.button>
                    ))}
                </div>
            </div>
        </motion.div>
    )
}

export default WeekGoalCard


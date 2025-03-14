import { useState } from "react"
import { motion } from "framer-motion"
import "react-circular-progressbar/dist/styles.css"
import { CombinedGoal } from "@/types/week_admin_responses"
import api from "@/api"
import ProgressCircle from "../generic/ProgressCircle"

const days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

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

    return (
        <motion.div
            className="p-6 rounded-2xl shadow-lg w-full max-w-screen-lg mx-auto mb-6 transition-all transform duration-300 relative overflow-hidden flex items-center justify-between bg-gray-50 text-gray-900"
            whileHover={{ scale: 1.02 }}
        >
            <div className="w-1/4 flex justify-start pl-6">
                <h2 className="text-xl font-semibold">{combinedGoal.name}</h2>
            </div>

            <div className="w-2/4 flex flex-col items-center">
                <div className="grid grid-cols-7 gap-3 mb-3 text-sm font-semibold text-gray-600">
                    {days.map((day, index) => (
                        <div key={index} className="flex flex-col items-center space-y-2">
                            <span
                                className={`text-center w-10 p-1 rounded-lg ${
                                    index === adjustedTodayIndex ? "bg-blue-600 text-white" : ""
                                }`}
                            >
                                {day}
                            </span>
                            <motion.button
                                onClick={() => handleCheck(index)}
                                className={`h-12 w-12 flex items-center justify-center rounded-xl transition-all border 
                                    ${
                                        checked[index]
                                            ? "bg-green-500 text-white border-green-600 shadow-md"
                                            : "bg-gray-200 border-gray-300"
                                    }`}
                                whileTap={{ scale: 0.9 }}
                            >
                                {checked[index] && "✔"}
                            </motion.button>
                        </div>
                    ))}
                </div>
            </div>

            <ProgressCircle progress={completedCount} total={combinedGoal.count} />
        </motion.div>
    )
}

export default WeekGoalCard


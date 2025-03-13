import { useState } from "react"
import { motion } from "framer-motion"
import { CombinedGoal } from "@/types/week_admin_responses"
import api from "@/api"

type WeekGoalCardProps = CombinedGoal

const WeekGoalCard = (combinedGoal: WeekGoalCardProps) => {
    const [checked, setChecked] = useState(() => Array(7).fill(false))

    const handleCheck = async (index: number) => {
        const newChecked = [...checked]
        newChecked[index] = !newChecked[index]
        setChecked(newChecked)

        try {
            if (newChecked[index]) {
                await api.patch(`checklist/${combinedGoal.id}/check`)
            } else {
                await api.patch(`checklist/${combinedGoal.id}/uncheck`)
            }
        } catch (error) {
            console.error("Error updating check status:", error)
        }
    }

    return (
        <motion.div
            className="p-5 rounded-2xl shadow-lg max-w-lg mx-auto mb-6 transition-all transform duration-300 bg-white text-gray-800"
            whileHover={{ scale: 1.05 }}
        >
            <div className="flex justify-between items-center mb-3">
                <h2 className="text-lg font-bold">{combinedGoal.name}</h2>
                <span className="bg-blue-500 text-white text-xs px-3 py-1 rounded-full font-semibold">
                    {combinedGoal.progress} / {combinedGoal.count} Completed
                </span>
            </div>

            <div className="flex items-center justify-between my-3">
                {Array.from({ length: 7 }).map((_, index) => (
                    <motion.button
                        key={index}
                        onClick={() => handleCheck(index)}
                        className={`h-9 w-9 flex items-center justify-center rounded-full transition-all 
                            ${checked[index] ? "bg-green-500 text-white" : "bg-gray-300"}`}
                        whileTap={{ scale: 0.9 }}
                    >
                        {checked[index] && "✔"}
                    </motion.button>
                ))}
            </div>
        </motion.div>
    )
}

export default WeekGoalCard


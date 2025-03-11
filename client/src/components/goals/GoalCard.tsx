import { useState, useEffect } from "react"
import { motion } from "framer-motion"
import { CheckCircle, Trophy } from "lucide-react"
import { CombinedGoal } from "@/types/checklist_response"
import api from "@/api"

type GoalCardProps = CombinedGoal

const GoalCard = (combinedGoal: GoalCardProps) => {
    const [checked, setChecked] = useState(() => {
        return Array(combinedGoal.count)
            .fill(false)
            .map((_, i) => i < combinedGoal.progress)
    })
    const [check, setCheck] = useState(0)

    useEffect(() => {
        const updateData = async () => {
            try {
                if (check === 1) {
                    const week = await api.patch(`checklist/${combinedGoal.id}/check`)
                } else if (check === 2) {
                    const week = await api.patch(`checklist/${combinedGoal.id}/uncheck`)
                }
            } catch (error) {
                console.error("Error fetching goals:", error)
            }
        }

        updateData()
    }, [check])

    const handleProgress = (index: number) => {
        const newChecked = [...checked]
        if (newChecked[index]) {
            if (index === checked.lastIndexOf(true)) {
                newChecked[index] = false
            }
            setCheck(2)
        } else if (index === 0 || newChecked[index - 1]) {
            newChecked[index] = true
            setCheck(1)
        }
        setChecked(newChecked)
    }

    const latestCheckedIndex = checked.lastIndexOf(true)
    const allChecked = checked.every((val) => val)
    const today = new Date().toISOString().split("T")[0]
    const checkedToday = combinedGoal?.check_history[-1]
        ? combinedGoal.check_history[-1]?.toISOString().split("T")[0] === today
        : false

    return (
        <motion.div
            className={`p-5 rounded-2xl shadow-lg max-w-lg mx-auto mb-6 transition-all transform duration-300 
                ${allChecked ? "bg-green-500 text-white" : "bg-gray-100 text-gray-800"} `}
            whileHover={{ scale: 1.05 }}
        >
            <div className="flex justify-between items-center mb-3">
                <h2 className="text-lg font-bold">{combinedGoal.name}</h2>
                {allChecked && (
                    <span className="flex items-center gap-1 bg-white text-green-600 text-xs px-3 py-1 rounded-full font-semibold">
                        <Trophy size={14} /> Completed
                    </span>
                )}
            </div>

            <div className="flex items-center gap-2 my-3">
                {Array.from({ length: combinedGoal.count }).map((_, index) => {
                    const isChecked = checked[index]
                    const isLatestChecked = index === latestCheckedIndex
                    const nextToCheck = index === latestCheckedIndex + 1
                    return (
                        <motion.button
                            key={index}
                            onClick={() => handleProgress(index)}
                            className={`h-9 w-9 flex items-center justify-center rounded-full transition-all 
                                ${
                                    isChecked
                                        ? isLatestChecked
                                            ? "bg-green-400"
                                            : "bg-green-600"
                                        : "bg-gray-300"
                                }`}
                            whileTap={{ scale: 0.9 }}
                        >
                            {isChecked && "✔"}
                            {nextToCheck && "➕"}
                        </motion.button>
                    )
                })}
            </div>

            {checkedToday && !allChecked && (
                <div className="flex items-center justify-center gap-1 text-sm text-green-600 font-semibold mt-2">
                    <CheckCircle size={14} /> Checked Today
                </div>
            )}
        </motion.div>
    )
}

export default GoalCard


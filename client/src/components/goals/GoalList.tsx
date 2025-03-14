import api from "@/api"
import { useEffect, useState } from "react"
import WeekGoalCard from "./WeekGoalCard"

const GoalList = () => {
    const [goalAndProgress, setGoalAndProgress] = useState<any[]>([])

    useEffect(() => {
        const fetchData = async () => {
            try {
                const week = await api.get("week_admin/latest_week")
                const weeklyGoals = await api.get(`week_admin/${week.data.id}`)
                setGoalAndProgress(weeklyGoals.data)
            } catch (error) {
                console.error("Error fetching goals:", error)
            }
        }

        fetchData()
    }, [])

    return (
        <div>
            <ul>
                {goalAndProgress.map((goal: any) => (
                    <li key={goal.id}>
                        <WeekGoalCard {...goal} />
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default GoalList


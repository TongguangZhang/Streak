import api from "@/api"
import { useEffect, useState } from "react"
import WeekGoalCard from "./WeekGoalCard"

type GoalListProps = {
    week_id: string | null
}

const GoalList = ({ week_id }: GoalListProps) => {
    const [goalAndProgress, setGoalAndProgress] = useState<any[]>([])

    useEffect(() => {
        const fetchData = async () => {
            let week
            try {
                if (week_id === null) {
                    week = await api.get("week_admin/latest_week")
                } else {
                    week = await api.get(`week_crud/${week_id}`)
                }
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


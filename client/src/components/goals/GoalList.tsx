import api from "@/api"
import GoalCard from "./GoalCard"
import { useEffect, useState } from "react"

const GoalList = () => {
    const [goalAndProgress, setGoalAndProgress] = useState<any[]>([])

    useEffect(() => {
        const fetchData = async () => {
            try {
                const week = await api.post("week/latest_week")
                const weeklyGoals = await api.post(`weekly_goal/${week.data.id}`)

                const goalPromises = weeklyGoals.data.map(async (goal: any) => {
                    const goalInDb = await api.get(`goal/${goal.goal_id}`)
                    goal.count = goalInDb.data.count
                    goal.name = goalInDb.data.name
                    return goal
                })

                const resolvedGoals = await Promise.all(goalPromises)
                setGoalAndProgress(resolvedGoals)
            } catch (error) {
                console.error("Error fetching goals:", error)
            }
        }

        fetchData()
    }, [])

    return (
        <div>
            <h1>Goals</h1>
            <ul>
                {goalAndProgress.map((goal: any) => (
                    <li key={goal.id}>
                        <GoalCard name={goal.name} count={goal.count} progress={goal.checks} />
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default GoalList


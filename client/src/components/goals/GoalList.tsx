import api from "@/api"
import WeekGoalCard from "./WeekGoalCard"

type GoalListProps = {
    week_id: string | null
}

const GoalList = async ({ week_id }: GoalListProps) => {
    let weeklyGoals: any[] = []
    let week
    try {
        if (week_id === null) {
            week = await api.get("week_admin/latest_week")
        } else {
            week = await api.get(`week_crud/${week_id}`)
        }
        const res = await api.get(`week_admin/${week.data.id}`)
        weeklyGoals = res.data
    } catch (error) {
        console.error("Error fetching goals:", error)
    }

    return (
        <div>
            <ul>
                {weeklyGoals.map((goal: any) => (
                    <li key={goal.id}>
                        <WeekGoalCard {...goal} />
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default GoalList


"use client"

import GoalList from "@/components/goals/GoalList"
import { useParams } from "next/navigation"

const WeekPage = () => {
    const params = useParams()
    const week_id = params?.week_id as string // Ensure correct type

    return (
        <div>
            <GoalList week_id={week_id} />
        </div>
    )
}

export default WeekPage


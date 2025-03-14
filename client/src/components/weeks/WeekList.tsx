import api from "@/api"
import { useEffect, useState } from "react"
import WeekCard from "./WeekCard"

const WeekList = () => {
    const [weeks, setWeeks] = useState<any[]>([])

    useEffect(() => {
        const fetchData = async () => {
            try {
                const weeks = await api.get("week_admin")
                setWeeks(weeks.data)
            } catch (error) {
                console.error("Error fetching goals:", error)
            }
        }

        fetchData()
    }, [])

    return (
        <div>
            <ul>
                {weeks.map((week: any) => (
                    <li key={week.id}>
                        <WeekCard {...week} />
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default WeekList


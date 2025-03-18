import api from "@/api"
import WeekCard from "./WeekCard"

const WeekList = async () => {
    let weeks: any[] = []
    try {
        const res = await api.get("week_admin")
        weeks = res.data
    } catch (error) {
        console.error("Error fetching goals:", error)
    }

    return (
        <div className="mt-20 space-y-4">
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


import GoalList from "@/components/goals/GoalList"

type WeekPageParams = {
    week_id: string
}

const WeekPage = async ({ params }: { params: WeekPageParams }) => {
    const week_id = (await params?.week_id) as string

    return (
        <div>
            <GoalList week_id={week_id} />
        </div>
    )
}

export default WeekPage


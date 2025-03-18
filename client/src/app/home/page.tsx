import GoalForm from "@/components/goals/GoalForm"
import GoalList from "@/components/goals/GoalList"

const GoalPage = () => {
    return (
        <div>
            <GoalList week_id={null} />
            <GoalForm />
        </div>
    )
}

export default GoalPage


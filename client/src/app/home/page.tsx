import GoalForm from "@/components/goals/GoalForm"
import GoalList from "@/components/goals/GoalList"
import Navbar from "@/components/navbar/Navbar"

const GoalPage = () => {
    return (
        <div>
            <Navbar />
            <GoalList week_id={null} />
            <GoalForm />
        </div>
    )
}

export default GoalPage


import { GoalInDB } from "./goal"
import { WeekInDB } from "./week"
import { WeeklyGoalInDB } from "./weekly_goal"

export type CombinedGoal = GoalInDB & WeeklyGoalInDB

export type WeekData = WeekInDB & {
    total_set: number
    total_achieved: number
}


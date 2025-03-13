import { Goal, GoalInDB } from "./goal"
import { WeeklyGoalInDB } from "./weekly_goal"

export type CombinedGoal = GoalInDB & WeeklyGoalInDB

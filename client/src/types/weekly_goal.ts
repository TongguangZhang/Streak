export type WeeklyGoal = {
    goal_id: string
    week_id: string
    progress: number
    check_history: Date[]
}

export type WeeklyGoalInDB = WeeklyGoal & {
    id: string
    updated_at: Date
}

export type OptionalWeeklyGoal = Partial<WeeklyGoal>


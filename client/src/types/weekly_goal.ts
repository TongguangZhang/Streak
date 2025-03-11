export type WeeklyGoal = {
    goal_id: string
    week_id: string
    progress: number
    last_check: Date
}

export type WeeklyGoalInDB = WeeklyGoal & {
    id: string
    updated_at: Date
}

export type OptionalWeeklyGoal = Partial<WeeklyGoal>

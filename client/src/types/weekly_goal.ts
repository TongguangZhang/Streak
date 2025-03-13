export type WeeklyGoal = {
    goal_id: string
    week_id: string
    progress: number
    check_history: string[]
    mon: boolean
    tue: boolean
    wed: boolean
    thu: boolean
    fri: boolean
    sat: boolean
    sun: boolean
}

export type WeeklyGoalInDB = WeeklyGoal & {
    id: string
    updated_at: Date
}

export type OptionalWeeklyGoal = Partial<WeeklyGoal>


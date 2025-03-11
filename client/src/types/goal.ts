type GoalHistory = {
    start: Date
    end: Date
    count: number
}

export type Goal = {
    active: boolean
    name: string
    description: string
    count: number
    history: GoalHistory[]
}

export type GoalInDB = Goal & {
    id: string
    created_at: Date
    updated_at: Date
}

export type OptionalGoal = Partial<Goal>


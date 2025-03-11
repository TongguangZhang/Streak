export type Week = {
    start_date: Date
}

export type WeekInDB = Week & {
    id: string
    updated_at: Date
}

export type OptionalWeek = Partial<Week>


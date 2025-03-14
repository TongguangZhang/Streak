export type Week = {
    start_date: Date | string
}

export type WeekInDB = Week & {
    id: string
    updated_at: Date
}

export type OptionalWeek = Partial<Week>


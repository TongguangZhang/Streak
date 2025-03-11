import { useState } from "react"

type GoalCardProps = {
    name: string
    count: number
    progress: number
}

const GoalCard = ({ name, count, progress }: GoalCardProps) => {
    const [checked, setChecked] = useState<boolean[]>(Array(count).fill(false))

    for (let i = 0; i < count; i++) {
        if (i < progress) {
            checked[i] = true
        }
    }

    const handleCheckboxChange = (index: number) => {
        const newChecked = [...checked]
        newChecked[index] = !newChecked[index]
        setChecked(newChecked)
    }

    return (
        <div className="flex flex-row gap-5 bg-white p-4 rounded-lg shadow-md max-w-md mx-auto mb-4 transition-transform transform hover:scale-105 duration-200">
            <h2 className="text-xl font-semibold mb-2 text-center text-blue-700">{name}</h2>
            <div className="flex items-center justify-center gap-2 mb-2">
                {Array.from({ length: count }).map((_, index) => (
                    <input
                        key={index}
                        type="checkbox"
                        checked={checked[index]}
                        onChange={() => handleCheckboxChange(index)}
                        className="form-checkbox text-blue-600 h-5 w-5 rounded-md transition-colors duration-150 focus:ring-2 focus:ring-blue-500"
                    />
                ))}
            </div>
        </div>
    )
}

export default GoalCard


import { buildStyles, CircularProgressbar } from "react-circular-progressbar"

type ProgressProps = {
    progress: number
    total: number
}

const ProgressCircle = ({ progress, total }: ProgressProps) => {
    return (
        <div className="w-1/4 flex justify-end pr-6">
            {/* Wrapper to allow absolute positioning of the text */}
            <div className="relative w-16 h-16">
                {/* Circular Progress Bar */}
                <CircularProgressbar
                    value={(progress / total) * 100}
                    styles={buildStyles({
                        pathColor: progress === total ? "#22C55E" : "#2563EB",
                        trailColor: "#E5E7EB",
                        strokeLinecap: "round",
                    })}
                />
                {/* Centered Text */}
                <div
                    className={`absolute inset-0 flex items-center justify-center text-xs font-semibold ${
                        progress === total ? "text-green-600" : "text-blue-600"
                    }`}
                >
                    {progress}/{total}
                </div>
            </div>
        </div>
    )
}

export default ProgressCircle


import { WeekData } from "@/types/week_admin_responses"
import { motion } from "framer-motion"
import ProgressCircle from "../generic/ProgressCircle"

const WeekCard = (weekData: WeekData) => {
    return (
        <motion.div
            className="p-6 rounded-2xl shadow-lg w-full max-w-screen-lg mx-auto mb-6 transition-all transform duration-300 relative overflow-hidden flex items-center justify-between bg-gray-50 text-gray-900"
            whileHover={{ scale: 1.02 }}
        >
            <div className="w-1/4 flex justify-start pl-6">
                <h2 className="text-xl font-semibold">{weekData.start_date.toString()}</h2>
            </div>

            <div>
                {weekData.total_achieved === weekData.total_set
                    ? "Week Completed"
                    : "Week Incomplete"}
            </div>

            <ProgressCircle progress={weekData.total_achieved} total={weekData.total_set} />
        </motion.div>
    )
}

export default WeekCard


"use client"

import { motion } from "framer-motion"

export default function BackgroundBeams() {
  return (
    <div className="absolute inset-0 overflow-hidden pointer-events-none">
      <svg
        className="absolute w-full h-full opacity-[0.03]"
        viewBox="0 0 800 600"
        xmlns="http://www.w3.org/2000/svg"
      >
        {[...Array(8)].map((_, i) => (
          <motion.line
            key={i}
            x1={100 * i}
            y1="0"
            x2={800 - 100 * i}
            y2="600"
            stroke="#6366f1"
            strokeWidth="1"
            initial={{ pathLength: 0, opacity: 0 }}
            animate={{ pathLength: 1, opacity: 1 }}
            transition={{ duration: 2, delay: i * 0.2, ease: "easeInOut" }}
          />
        ))}
      </svg>
    </div>
  )
}

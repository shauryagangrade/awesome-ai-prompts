"use client"

import { motion } from "framer-motion"

interface SpotlightProps {
  children: React.ReactNode
  className?: string
}

export default function Spotlight({ children, className }: SpotlightProps) {
  return (
    <motion.div
      className={`relative ${className || ""}`}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.8 }}
    >
      <div className="absolute inset-0 bg-gradient-to-r from-[#6366f1]/20 via-[#6366f1]/10 to-transparent rounded-lg blur-xl" />
      <div className="relative">{children}</div>
    </motion.div>
  )
}

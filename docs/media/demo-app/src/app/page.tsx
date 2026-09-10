"use client"

import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import BrowserScene from "@/components/BrowserScene"
import TerminalScene from "@/components/TerminalScene"
import BackgroundBeams from "@/components/BackgroundBeams"

export default function Home() {
  const [scene, setScene] = useState<"browser" | "terminal">("browser")
  const [scene1Done, setScene1Done] = useState(false)

  useEffect(() => {
    if (scene1Done) {
      const timer = setTimeout(() => setScene("terminal"), 800)
      return () => clearTimeout(timer)
    }
  }, [scene1Done])

  return (
    <div className="relative w-screen h-screen bg-[#0a0a0b] overflow-hidden">
      <BackgroundBeams />

      <AnimatePresence mode="wait">
        {scene === "browser" && (
          <motion.div
            key="browser"
            initial={{ opacity: 1 }}
            exit={{ opacity: 0, x: -50 }}
            transition={{ duration: 0.6 }}
            className="absolute inset-0 flex items-center justify-center p-8"
          >
            <BrowserScene onComplete={() => setScene1Done(true)} />
          </motion.div>
        )}

        {scene === "terminal" && (
          <motion.div
            key="terminal"
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            className="absolute inset-0 flex items-center justify-center p-8"
          >
            <TerminalScene />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

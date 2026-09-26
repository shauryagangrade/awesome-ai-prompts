"use client"

import { useEffect, useRef, useState } from "react"
import { motion } from "framer-motion"
import Typewriter from "@/components/Typewriter"

interface ChatSceneProps {
  onComplete: () => void
}

// Beats, in ms from mount. Timings mirror the beats of the README GIF this
// scene feeds, so the splice in front of the real recording lines up.
const SHOW_USER_AT = 400
const SHOW_SHRUG_AT = 3600
const SHOW_CARD_AT = 5600
const DONE_AT = 8400

type Beat = "idle" | "typing" | "shrug" | "card"

export default function ChatScene({ onComplete }: ChatSceneProps) {
  const [beat, setBeat] = useState<Beat>("idle")

  // One-shot timers: keep onComplete in a ref so the effect can run once on
  // mount. An inline arrow in the dep list would restart these timers on
  // every render, stretching the whole scene.
  const onCompleteRef = useRef(onComplete)
  useEffect(() => {
    onCompleteRef.current = onComplete
  }, [onComplete])

  useEffect(() => {
    const timers = [
      setTimeout(() => setBeat("typing"), SHOW_USER_AT),
      setTimeout(() => setBeat("shrug"), SHOW_SHRUG_AT),
      setTimeout(() => setBeat("card"), SHOW_CARD_AT),
      setTimeout(() => onCompleteRef.current?.(), DONE_AT),
    ]
    return () => timers.forEach(clearTimeout)
  }, [])

  const bubble = "max-w-xs rounded-lg px-4 py-3 text-sm"

  return (
    <div className="w-full max-w-2xl h-full flex flex-col justify-end">
      {beat === "card" ? (
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.45 }}
          className="flex h-full flex-col items-center justify-center text-center"
        >
          <p className="text-[44px] leading-[1.7] text-[#e4e4e7]">
            Same agent. Same request.
            <br />
            Now paste a prompt from
            <br />
            awesome-ai-prompts
          </p>
        </motion.div>
      ) : (
        <div className="rounded-xl bg-[#18181b] border border-[#27272a] p-6 space-y-4">
          <div className="text-xs font-medium uppercase tracking-widest text-[#71717a]">
            AI coding agent
          </div>

          {(beat === "typing" || beat === "shrug") && (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.3 }}
              className="flex justify-end"
            >
              <div className={`${bubble} bg-[#3b82f6] text-white`}>
                <Typewriter text="Explain this repo to me" speed={50} />
              </div>
            </motion.div>
          )}

          {beat === "shrug" && (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.3 }}
              className="flex justify-start"
            >
              <div className={`${bubble} bg-[#27272a] text-[#a1a1aa]`}>
                quit prompting bro
              </div>
            </motion.div>
          )}
        </div>
      )}
    </div>
  )
}

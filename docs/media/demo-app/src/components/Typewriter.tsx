"use client"

import { useEffect, useRef, useState } from "react"
import { motion } from "framer-motion"

interface TypewriterProps {
  text: string
  speed?: number
  onComplete?: () => void
  className?: string
}

export default function Typewriter({ text, speed = 30, onComplete, className }: TypewriterProps) {
  const [displayed, setDisplayed] = useState("")

  // Keep the callback in a ref. Putting it in the effect deps restarts the
  // interval on every parent render (callers pass inline arrows), which
  // restarts the animation from the first character each time.
  const onCompleteRef = useRef(onComplete)
  useEffect(() => {
    onCompleteRef.current = onComplete
  }, [onComplete])

  useEffect(() => {
    let i = 0
    const interval = setInterval(() => {
      if (i <= text.length) {
        setDisplayed(text.slice(0, i))
        i++
      } else {
        clearInterval(interval)
        onCompleteRef.current?.()
      }
    }, speed)
    return () => clearInterval(interval)
  }, [text, speed])

  return (
    <motion.span
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className={className}
    >
      {displayed}
      <span className="inline-block w-[2px] h-[1em] bg-[#6366f1] animate-pulse ml-0.5 align-text-bottom" />
    </motion.span>
  )
}

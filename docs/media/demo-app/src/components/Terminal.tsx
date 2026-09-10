"use client"

import { useEffect, useState, useRef } from "react"
import { motion } from "framer-motion"

interface TerminalProps {
  commands: Array<{ type: "input" | "output"; text: string; delay?: number }>
  onComplete?: () => void
}

export default function Terminal({ commands, onComplete }: TerminalProps) {
  const [visibleLines, setVisibleLines] = useState<number>(0)
  const [currentInput, setCurrentInput] = useState("")
  const [isTyping, setIsTyping] = useState(false)
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    let lineIndex = 0
    let timeout: NodeJS.Timeout

    const showNextLine = () => {
      if (lineIndex >= commands.length) {
        onComplete?.()
        return
      }

      const cmd = commands[lineIndex]
      if (cmd.type === "input") {
        setIsTyping(true)
        let charIndex = 0
        const typeChar = () => {
          if (charIndex <= cmd.text.length) {
            setCurrentInput(cmd.text.slice(0, charIndex))
            charIndex++
            timeout = setTimeout(typeChar, 30 + Math.random() * 20)
          } else {
            setIsTyping(false)
            timeout = setTimeout(() => {
              setVisibleLines((v) => v + 1)
              setCurrentInput("")
              lineIndex++
              timeout = setTimeout(showNextLine, cmd.delay || 200)
            }, 300)
          }
        }
        typeChar()
      } else {
        setVisibleLines((v) => v + 1)
        lineIndex++
        timeout = setTimeout(showNextLine, cmd.delay || 100)
      }
    }

    timeout = setTimeout(showNextLine, 500)
    return () => clearTimeout(timeout)
  }, [commands, onComplete])

  useEffect(() => {
    if (containerRef.current) {
      containerRef.current.scrollTop = containerRef.current.scrollHeight
    }
  }, [visibleLines, currentInput])

  const inputLines = commands.filter((c) => c.type === "input")
  const outputLines = commands.filter((c) => c.type === "output")

  let inputIdx = 0
  let outputIdx = 0

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="rounded-xl overflow-hidden shadow-2xl border border-[#27272a]"
      style={{ background: "#0c0c0d" }}
    >
      {/* Title bar */}
      <div className="flex items-center gap-2 px-4 py-3 bg-[#18181b] border-b border-[#27272a]">
        <div className="flex gap-1.5">
          <div className="w-3 h-3 rounded-full bg-[#ef4444]" />
          <div className="w-3 h-3 rounded-full bg-[#eab308]" />
          <div className="w-3 h-3 rounded-full bg-[#22c55e]" />
        </div>
        <div className="flex-1 text-center text-xs text-[#71717a] font-mono">
          Terminal - zsh
        </div>
      </div>

      {/* Terminal body */}
      <div
        ref={containerRef}
        className="p-4 font-mono text-sm leading-relaxed h-[500px] overflow-y-auto"
      >
        {commands.slice(0, visibleLines).map((cmd, i) => {
          if (cmd.type === "input") {
            inputIdx++
            return (
              <div key={i} className="flex gap-2">
                <span className="text-[#22c55e] select-none">$</span>
                <span className="text-[#fafafa]">{cmd.text}</span>
              </div>
            )
          } else {
            outputIdx++
            return (
              <div key={i} className="text-[#a1a1aa] whitespace-pre-wrap">
                {cmd.text}
              </div>
            )
          }
        })}

        {isTyping && (
          <div className="flex gap-2">
            <span className="text-[#22c55e] select-none">$</span>
            <span className="text-[#fafafa]">{currentInput}</span>
            <span className="inline-block w-2 h-4 bg-[#fafafa] animate-pulse ml-0.5" />
          </div>
        )}

        {!isTyping && visibleLines > 0 && visibleLines >= commands.length && (
          <div className="flex gap-2 mt-1">
            <span className="text-[#22c55e] select-none">$</span>
            <span className="inline-block w-2 h-4 bg-[#fafafa] animate-pulse" />
          </div>
        )}
      </div>
    </motion.div>
  )
}

"use client"

import { useState, useEffect, useRef } from "react"
import { motion } from "framer-motion"

type Line = { type: "cmd" | "tool" | "output" | "heading"; text: string; color?: string }

const REAL_OUTPUT: Line[] = [
  { type: "cmd", text: 'opencode run "Build a detailed understanding of this repo..."' },
  { type: "output", text: "" },
  { type: "output", text: "> build - big-pickle", color: "#6366f1" },
  { type: "output", text: "" },
  { type: "tool", text: "Read .", color: "#eab308" },
  { type: "tool", text: "Read README.md", color: "#eab308" },
  { type: "output", text: "I'll start by exploring the repository structure and key", color: "#a1a1aa" },
  { type: "output", text: "configuration files in parallel.", color: "#a1a1aa" },
  { type: "output", text: "" },
  { type: "tool", text: "$ rtk git log --oneline -20", color: "#22c55e" },
  { type: "output", text: "4e80bfc fix: satisfy markdown lint (no inline HTML)", color: "#71717a" },
  { type: "output", text: "97ecac1 chore: release v0.3.0", color: "#71717a" },
  { type: "output", text: "75ee063 docs: add above-the-fold demo GIF", color: "#71717a" },
  { type: "output", text: "0193887 docs: add bug-finder and bug-finder-with-docs prompts", color: "#71717a" },
  { type: "output", text: "" },
  { type: "tool", text: "Read CONTRIBUTING.md", color: "#eab308" },
  { type: "tool", text: "Read CHANGELOG.md", color: "#eab308" },
  { type: "tool", text: "Read .editorconfig", color: "#eab308" },
  { type: "tool", text: "Read scripts/check-consistency.sh", color: "#eab308" },
  { type: "tool", text: "Read scripts/check-links.sh", color: "#eab308" },
  { type: "tool", text: "Read .github/workflows/ci.yml", color: "#eab308" },
  { type: "output", text: "" },
  { type: "heading", text: "# Scope: full repo overview, quick orientation depth", color: "#6366f1" },
  { type: "output", text: "" },
  { type: "heading", text: "## 1. What it is", color: "#fafafa" },
  { type: "output", text: "awesome-ai-prompts is a curated list of 78 copy-paste AI", color: "#a1a1aa" },
  { type: "output", text: "prompts for student developers who use AI coding agents.", color: "#a1a1aa" },
  { type: "output", text: "Evidence: README.md:7-12", color: "#71717a" },
  { type: "output", text: "" },
  { type: "heading", text: "## 2. Tech stack, verified", color: "#fafafa" },
  { type: "output", text: "No runtime. Markdown content library. CI tooling:", color: "#a1a1aa" },
  { type: "output", text: "  - Node 20 (markdownlint-cli2 v0.17.2)", color: "#a1a1aa" },
  { type: "output", text: "  - Bash (check-consistency.sh, check-links.sh)", color: "#a1a1aa" },
  { type: "output", text: "  - Python 3 (em-dash enforcement)", color: "#a1a1aa" },
  { type: "output", text: "Evidence: .github/workflows/ci.yml:19-36", color: "#71717a" },
  { type: "output", text: "" },
  { type: "heading", text: "## 3. Architecture, with evidence", color: "#fafafa" },
  { type: "output", text: "Flat directory: 11 category folders, each containing", color: "#a1a1aa" },
  { type: "output", text: "*-prompt.md files. No build artifacts, no compiled code.", color: "#a1a1aa" },
  { type: "output", text: "  core-coding/       (11 prompts)", color: "#71717a" },
  { type: "output", text: "  testing-quality/   (9 prompts)", color: "#71717a" },
  { type: "output", text: "  git-github/        (10 prompts)", color: "#71717a" },
  { type: "output", text: "  + 8 more categories", color: "#71717a" },
  { type: "output", text: "Entry point: README.md linked index of all prompts.", color: "#a1a1aa" },
  { type: "output", text: "Evidence: root directory listing", color: "#71717a" },
  { type: "output", text: "" },
  { type: "heading", text: "## 4. Key data flow", color: "#fafafa" },
  { type: "output", text: "Reader -> README.md -> category folder -> *-prompt.md", color: "#a1a1aa" },
  { type: "output", text: "-> copy block after '---' -> paste into AI agent.", color: "#a1a1aa" },
  { type: "output", text: "Agent reads the prompt and the code it targets.", color: "#a1a1aa" },
  { type: "output", text: "Evidence: README.md:33-51 (Quick Start)", color: "#71717a" },
  { type: "output", text: "" },
  { type: "heading", text: "## 5. Conventions and gotchas", color: "#fafafa" },
  { type: "output", text: "  - All prompts follow: H1 title + '---' divider", color: "#a1a1aa" },
  { type: "output", text: "  - No em dashes anywhere (CI enforced)", color: "#a1a1aa" },
  { type: "output", text: "  - Conventional Commits required", color: "#a1a1aa" },
  { type: "output", text: "  - New prompts need CHANGELOG + README entries", color: "#a1a1aa" },
  { type: "output", text: "  - [spec] prompts carry a verification checklist", color: "#a1a1aa" },
  { type: "output", text: "Evidence: scripts/check-consistency.sh, ci.yml:22-29", color: "#71717a" },
  { type: "output", text: "" },
  { type: "heading", text: "## 6. How to run it", color: "#fafafa" },
  { type: "tool", text: "$ bash scripts/check-links.sh", color: "#22c55e" },
  { type: "output", text: "check-links.sh: OK (78 prompts, README links verified)", color: "#22c55e" },
  { type: "tool", text: "$ bash scripts/check-consistency.sh", color: "#22c55e" },
  { type: "tool", text: "$ npx markdownlint-cli2@0.17.2 \"**/*.md\"", color: "#22c55e" },
  { type: "output", text: "Evidence: .github/workflows/ci.yml:19-36", color: "#71717a" },
  { type: "output", text: "" },
  { type: "heading", text: "## 7. Open questions", color: "#fafafa" },
  { type: "output", text: "  - CITATION.cff still says v0.1.0 (repo is at v0.3.0)", color: "#a1a1aa" },
  { type: "output", text: "  - 'instagram post pictures/' is gitignored, unused", color: "#a1a1aa" },
  { type: "output", text: "  - Demo GIF: no automated regen script found", color: "#a1a1aa" },
  { type: "output", text: "" },
  { type: "heading", text: "## Summary", color: "#fafafa" },
  { type: "output", text: "  Type         Static markdown content library", color: "#a1a1aa" },
  { type: "output", text: "  Prompts      78 files, 11 categories", color: "#a1a1aa" },
  { type: "output", text: "  Commits      59", color: "#a1a1aa" },
  { type: "output", text: "  License      MIT", color: "#a1a1aa" },
  { type: "output", text: "  CI           3 GitHub Actions workflows", color: "#a1a1aa" },
  { type: "output", text: "  No runtime   Confirmed (SECURITY.md)", color: "#a1a1aa" },
  { type: "output", text: "" },
  { type: "tool", text: "Report complete. Every claim verified with file:line evidence.", color: "#22c55e" },
]

export default function TerminalScene() {
  const [visibleIdx, setVisibleIdx] = useState(0)
  const [currentInput, setCurrentInput] = useState("")
  const [isTyping, setIsTyping] = useState(false)
  const scrollRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    let lineIdx = 0
    let timeout: NodeJS.Timeout

    const showNext = () => {
      if (lineIdx >= REAL_OUTPUT.length) return
      const line = REAL_OUTPUT[lineIdx]

      if (line.type === "cmd") {
        setIsTyping(true)
        let charIdx = 0
        const typeChar = () => {
          if (charIdx <= line.text.length) {
            setCurrentInput(line.text.slice(0, charIdx))
            charIdx++
            timeout = setTimeout(typeChar, 18 + Math.random() * 10)
          } else {
            setIsTyping(false)
            timeout = setTimeout(() => {
              setVisibleIdx((v) => v + 1)
              setCurrentInput("")
              lineIdx++
              timeout = setTimeout(showNext, 350)
            }, 200)
          }
        }
        typeChar()
      } else if (line.type === "tool") {
        setVisibleIdx((v) => v + 1)
        lineIdx++
        timeout = setTimeout(showNext, 70 + Math.random() * 50)
      } else {
        setVisibleIdx((v) => v + 1)
        lineIdx++
        timeout = setTimeout(showNext, 35 + Math.random() * 25)
      }
    }

    timeout = setTimeout(showNext, 400)
    return () => clearTimeout(timeout)
  }, [])

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight
    }
  }, [visibleIdx, currentInput])

  return (
    <div className="w-full max-w-4xl h-full flex flex-col">
      <motion.div
        initial={{ opacity: 0, y: 20, scale: 0.98 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        transition={{ duration: 0.5 }}
        className="rounded-xl overflow-hidden shadow-2xl border border-[#27272a] flex-1 flex flex-col"
        style={{ background: "#0c0c0d" }}
      >
        {/* Title bar */}
        <div className="flex items-center gap-2 px-4 py-2.5 bg-[#18181b] border-b border-[#27272a] shrink-0">
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
        <div ref={scrollRef} className="p-4 font-mono text-[13px] leading-[20px] flex-1 overflow-y-auto overflow-x-hidden">
          {REAL_OUTPUT.slice(0, visibleIdx).map((line, i) => {
            if (line.type === "cmd") {
              return (
                <div key={i} className="flex gap-2">
                  <span className="text-[#22c55e] select-none">$</span>
                  <span className="text-[#fafafa]">{line.text}</span>
                </div>
              )
            }
            if (line.type === "tool") {
              return (
                <div key={i} className="flex gap-2 items-center">
                  <span className="text-[#eab308] select-none shrink-0">&gt;</span>
                  <span style={{ color: line.color }} className="text-[#eab308]">{line.text}</span>
                </div>
              )
            }
            if (line.type === "heading") {
              return (
                <div key={i} style={{ color: line.color }} className="font-semibold mt-2">
                  {line.text}
                </div>
              )
            }
            return (
              <div key={i} style={{ color: line.color || "#a1a1aa" }} className="whitespace-pre-wrap">
                {line.text || "\u00A0"}
              </div>
            )
          })}

          {isTyping && (
            <div className="flex gap-2">
              <span className="text-[#22c55e] select-none">$</span>
              <span className="text-[#fafafa]">{currentInput}</span>
              <span className="inline-block w-[7px] h-[15px] bg-[#fafafa] animate-pulse ml-0.5" />
            </div>
          )}
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1, duration: 0.5 }}
        className="text-center mt-4 text-[#52525b] text-xs font-mono"
      >
        awesome-ai-prompts - verified, paste-and-go AI prompts
      </motion.div>
    </div>
  )
}
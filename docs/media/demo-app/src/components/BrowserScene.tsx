"use client"

import { useState, useEffect, useRef } from "react"
import { motion, AnimatePresence } from "framer-motion"
import Spotlight from "@/components/Spotlight"

interface BrowserSceneProps {
  onComplete: () => void
}

const README_LINES = [
  "# awesome-ai-prompts",
  "",
  "A curated list of copy-paste AI prompts for student developers",
  "who use AI coding agents. Senior-engineer workflows that verify,",
  "don't guess: read code before editing, small confirmed steps.",
  "",
  "## Contents",
  "",
  "- Core coding (11)",
  "- System design (5)",
  "- Git & GitHub (10)",
  "- Testing & quality (9)",
  "- Docs & delivery (5)",
  "",
  "## Core coding",
  "",
  "- feature-implementation-prompt.md - build a feature end-to-end",
  "",
  "- pair-programming-session-prompt.md - interactive build loop",
  "",
  "- debugging-prompt.md - systematic debugging",
  "",
  "- refactoring-prompt.md - behavior-preserving refactoring",
  "",
  "- codebase-onboarding-prompt.md [spec] - understand an unfamiliar repo",
  "",
  "- api-integration-prompt.md - integrate a REST API",
  "",
  "- api-design-prompt.md - design a well-structured REST API",
  "",
  "- database-design-prompt.md - model a relational schema",
  "",
  "- environment-setup-prompt.md - bootstrap a dev environment",
  "",
  "## System design",
  "",
  "- system-design-prompt.md - design a system from requirements",
  "",
  "- architecture-decision-record-prompt.md - write an ADR",
  "",
  "## Git & GitHub",
  "",
  "- commit-prompt.md - conventional commits",
  "",
  "- pr-description-prompt.md - write PR descriptions",
  "",
  "## Testing & quality",
  "",
  "- bug-finder-prompt.md [spec] - find real bugs in a repo",
  "",
  "- test-generation-prompt.md - write tests that assert behavior",
]

const TARGET_LINE_IDX = 24 // codebase-onboarding-prompt.md (with blank lines between)

const PROMPT_CONTENT = `Build a detailed understanding of this repository. Produce a report that a
new team member could use to navigate the codebase on day one. Verify
everything against the code, lockfiles, and config - do not paraphrase the
README.

## Define the scope first

Before reading code, state:

1. **What you need to understand** - Clarify the focus: full repo overview,
   a particular subsystem, the data flow for a specific feature, or
   something else.
2. **What depth** - Quick orientation or deep dive? State explicitly.
3. **What is out of scope** - Exclude anything not relevant.

## What to produce

1. **What it is** - One or two sentences about the project.
2. **Tech stack, verified** - From lockfiles, not README claims.
3. **Architecture, with evidence** - Cite file, directory, or function.
4. **Key data flow** - Walk user journeys with file:line citations.
5. **Conventions and gotchas** - Unusual patterns, required env vars.
6. **How to run it** - Exact commands verified against actual tooling.
7. **Open questions** - What could not be confirmed.

## Rules

- Read the code. For every claim, point to proof.
- If the README is wrong, say so and rely on the code.
- Be concise and concrete. No filler.`

export default function BrowserScene({ onComplete }: BrowserSceneProps) {
  const [step, setStep] = useState(0)
  const [showPrompt, setShowPrompt] = useState(false)
  const [copied, setCopied] = useState(false)
  const [highlightIdx, setHighlightIdx] = useState(-1)
  const [selectFlash, setSelectFlash] = useState(false)
  const [clickPulse, setClickPulse] = useState(false)
  const scrollRef = useRef<HTMLDivElement>(null)
  const lineRefs = useRef<(HTMLDivElement | null)[]>([])
  const contentRef = useRef<HTMLDivElement>(null)
  const [cursorPos, setCursorPos] = useState({ x: 300, y: 60 })

  useEffect(() => {
    const timers: NodeJS.Timeout[] = []

    // Step 1: Start scrolling down
    timers.push(setTimeout(() => setStep(1), 800))

    // Step 2: Highlight the codebase-onboarding line
    timers.push(setTimeout(() => {
      setStep(2)
      setHighlightIdx(TARGET_LINE_IDX)
    }, 2800))

    // Step 3: Move cursor over the line and click
    timers.push(setTimeout(() => {
      setStep(3)
      setClickPulse(true)
    }, 5200))

    // Step 4: Selection flash, then transition to prompt view
    timers.push(setTimeout(() => {
      setSelectFlash(true)
      setClickPulse(false)
    }, 6200))

    // Step 5: Go to prompt file view
    timers.push(setTimeout(() => {
      setSelectFlash(false)
      setShowPrompt(true)
    }, 7000))

    // Step 6: Show Copy button
    timers.push(setTimeout(() => setStep(4), 8200))

    // Step 7: Click copy
    timers.push(setTimeout(() => {
      setStep(5)
      setCopied(true)
    }, 9800))

    // Step 8: Done
    timers.push(setTimeout(() => onComplete(), 11200))

    return () => timers.forEach(clearTimeout)
  }, [onComplete])

  // Auto-scroll to the highlighted line
  useEffect(() => {
    if (step >= 2 && highlightIdx >= 0 && lineRefs.current[highlightIdx] && scrollRef.current) {
      const el = lineRefs.current[highlightIdx]
      const container = scrollRef.current
      if (!el || !container) return
      const elTop = el.offsetTop - container.offsetTop
      const scrollTo = Math.max(0, elTop - container.clientHeight / 3)
      container.scrollTo({ top: scrollTo, behavior: "smooth" })
    }
  }, [step, highlightIdx])

  // Position the cursor over the highlighted line
  useEffect(() => {
    if (step >= 2 && lineRefs.current[TARGET_LINE_IDX]) {
      const line = lineRefs.current[TARGET_LINE_IDX]
      const content = contentRef.current
      if (!line || !content) return
      const rect = line.getBoundingClientRect()
      const contentRect = content.getBoundingClientRect()
      setCursorPos({
        x: rect.left - contentRect.left + rect.width - 4,
        y: rect.top - contentRect.top + rect.height / 2,
      })
    }
  }, [step, selectFlash, scrollRef, lineRefs])

  return (
    <div className="w-full max-w-5xl h-full flex flex-col">
      {/* Browser chrome */}
      <div className="rounded-t-xl bg-[#18181b] border border-[#27272a] border-b-0 px-4 py-2.5 flex items-center gap-3 shrink-0">
        <div className="flex gap-1.5">
          <div className="w-3 h-3 rounded-full bg-[#ef4444]" />
          <div className="w-3 h-3 rounded-full bg-[#eab308]" />
          <div className="w-3 h-3 rounded-full bg-[#22c55e]" />
        </div>
        <div className="flex-1 bg-[#0c0c0d] rounded-lg px-3 py-1.5 text-xs text-[#71717a] font-mono flex items-center gap-2">
          <svg className="w-3 h-3 text-[#71717a] shrink-0" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
          </svg>
          <span className="truncate">github.com/shauryagangrade/awesome-ai-prompts</span>
        </div>
      </div>

      {/* Content area */}
      <div ref={contentRef} className="relative border border-[#27272a] border-t-0 rounded-b-xl bg-[#0c0c0d] flex-1 min-h-0 overflow-hidden">
        <AnimatePresence mode="wait">
          {!showPrompt ? (
            <motion.div
              key="readme"
              initial={{ opacity: 1 }}
              exit={{ opacity: 0, scale: 0.98 }}
              transition={{ duration: 0.3 }}
              ref={scrollRef}
              className="h-full overflow-y-auto overflow-x-hidden p-6 font-mono text-[13px] leading-[22px]"
            >
              {README_LINES.map((line, i) => {
                const isTarget = i === TARGET_LINE_IDX
                const isHighlighted = highlightIdx === i
                const isFlashing = selectFlash && isHighlighted

                return (
                  <div
                    key={i}
                    ref={(el) => { lineRefs.current[i] = el }}
                    className={`whitespace-pre-wrap transition-all duration-200 rounded-r ${
                      isFlashing
                        ? "bg-[#3b82f6]/25 border-l-2 border-[#3b82f6] pl-3 -ml-1 shadow-[inset_0_0_20px_rgba(59,130,246,0.1)]"
                        : isHighlighted
                        ? "bg-[#6366f1]/15 border-l-2 border-[#6366f1] pl-3 -ml-1"
                        : ""
                    }`}
                  >
                    {isHighlighted ? (
                      <Spotlight>
                        <span>
                          {line.split("codebase-onboarding-prompt.md").map((part, j) =>
                            j === 0 ? (
                              <span key={j}>{part}<span className="text-[#fafafa] font-semibold">codebase-onboarding-prompt.md</span></span>
                            ) : (
                              <span key={j}>{part}</span>
                            )
                          )}
                        </span>
                      </Spotlight>
                    ) : (
                      <span className={
                        line.startsWith("#") ? "text-[#fafafa] font-semibold" :
                        line.startsWith("- ") ? "text-[#a1a1aa]" :
                        "text-[#71717a]"
                      }>
                        {line}
                      </span>
                    )}
                  </div>
                )
              })}
            </motion.div>
          ) : (
            <motion.div
              key="prompt-file"
              initial={{ opacity: 0, scale: 0.97, y: 10 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              transition={{ duration: 0.4, ease: "easeOut" }}
              className="h-full overflow-y-auto p-6 font-mono text-[13px] leading-[22px] relative"
            >
              {/* Breadcrumb */}
              <div className="flex items-center gap-1.5 mb-3 text-xs">
                <span className="text-[#71717a]">shauryagangrade/awesome-ai-prompts</span>
                <span className="text-[#52525b]">/</span>
                <span className="text-[#71717a]">core-coding</span>
                <span className="text-[#52525b]">/</span>
                <span className="text-[#fafafa]">codebase-onboarding-prompt.md</span>
              </div>

              <div className="border-t border-[#27272a] pt-3">
                <pre className="text-[#a1a1aa] whitespace-pre-wrap">{PROMPT_CONTENT}</pre>
              </div>

              {/* Copy button */}
              {step >= 4 && (
                <motion.button
                  initial={{ opacity: 0, scale: 0.8, y: -10 }}
                  animate={{ opacity: 1, scale: 1, y: 0 }}
                  className="sticky top-2 float-right bg-[#22c55e] text-black font-semibold px-4 py-2 rounded-lg text-sm flex items-center gap-2 shadow-lg"
                >
                  {copied ? (
                    <>
                      <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                      Copied!
                    </>
                  ) : (
                    <>
                      <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                      </svg>
                      Copy
                    </>
                  )}
                </motion.button>
              )}
            </motion.div>
          )}
        </AnimatePresence>

        {/* Cursor overlay for clicking the prompt */}
        {!showPrompt && step >= 3 && (
          <motion.div
            className="absolute pointer-events-none z-20"
            style={{ left: cursorPos.x - 8, top: cursorPos.y - 8 }}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.3 }}
          >
            {/* Click ripple */}
            <motion.div
              className="absolute rounded-full border-2 border-[#3b82f6]"
              initial={{ width: 0, height: 0, left: -4, top: -4, opacity: 0.8 }}
              animate={{ width: 64, height: 64, left: -32, top: -32, opacity: 0 }}
              transition={{ duration: 0.8, repeat: clickPulse ? 3 : 0, ease: "easeOut" }}
            />
            {/* Hand cursor */}
            <svg
              viewBox="0 0 24 24"
              fill="white"
              className="w-6 h-6 drop-shadow-lg"
            >
              <path d="M5.5 3.21V20.8c0 .45.54.67.85.35l4.86-4.86a.5.5 0 01.35-.15h6.87c.48 0 .72-.58.38-.92L6.35 2.85a.5.5 0 00-.85.36z"/>
            </svg>
          </motion.div>
        )}
      </div>
    </div>
  )
}

---
title: Lesson 1 — The Paradigm Shift: From Prompting to Loops
created: 2026-06-10
module: Self Improving AI Loops
lesson: 1
tags: [paradigm-shift, context-engineering, feedback-loops, harness-engineering]
---

# Lesson 1: The Paradigm Shift — From Prompting to Loops

## Core Idea

AI engineering is undergoing a fundamental shift: the leverage point is moving from **how you ask the model** (prompting) to **what happens after the model responds** (loops). Models are converging in capability — the harness around the model is becoming the differentiator.

## The Hierarchy of Leverage

Think of AI engineering as four levels, each building on the last:

### Level 1: Prompt Engineering
**Definition:** How you phrase your request to the model. What system prompt to use, whether to say "please" or "this is critical."

**The reality:** Models are now good enough to infer intent from vague prompts. The discourse is stuck here, but the leverage has moved on.

### Level 2: Context Engineering
**Definition:** Giving the model the right information — documentation, schemas, relevant files, carefully selected context.

**Why it matters:** Context engineering gets you much further than prompting alone because the model stops guessing blind. It can fill gaps from existing practice rather than assumptions.

**Example:** Instead of prompting "write a REST API," include the project's `AGENTS.md`, the existing file structure, the database schema, and a sample endpoint. The model has the context to make better decisions.

### Level 3: Feedback Loop Engineering
**Definition:** Building tools and infrastructure so agents can verify their own work — not just "does it compile?" but "does it actually work as part of the system?"

**Why this is the new leverage:** This separates working code from getting lucky. It's the practice of making the agent see hard evidence of how its output behaves in a production-like setup.

**Example:** Instead of asking an agent to "write a feature and hope it works," give it:
- Browser debugging via CLI (Chrome DevTools)
- Database query skills against a dev database
- Log access and crash tracebacks
- OpenTelemetry traces to follow requests across services
- API keys to real development endpoints (not mocks)

### Level 4: Harness Engineering
**Definition:** Everything around the model that governs its behavior. (Birgitta Böckeler: "Agent = Model + Harness")

The harness splits into two halves:
- **Guides (feedforward):** What steers the agent *before* it acts — `CLAUDE.md`, type definitions, linting rules
- **Sensors (feedback):** What lets the agent *observe* consequences after it acts — the loops from Level 3

**Key insight:** Feedback loop engineering is the sensor half of harness engineering, done on purpose.

## Three Failure Modes of Prompt-First Approaches

### 1. Context Rot
In long AI conversations, the context window becomes a junk drawer. Every failed attempt piles up until the sliding window drops the original specification. The model slides into a "dumb zone" where it hallucinates and forgets its goals. Traditional fixes like summarizing break down over dozens of reasoning rounds.

**Analogy:** Like a whiteboard that fills up with scratch work until the original problem statement is covered.

### 2. Premature Exit
AI agents declare victory too early. Anthropic's research notes that agents usually look around, see that progress has been made, and declare the job done. Standard ReAct (Reasoning + Acting) loops inherit this flaw.

**Example:** An agent building a web app implements 3 of 12 features, sees "some progress," and says "done." The feature list never got checked against the original spec.

### 3. Single-Pass Fragility
One prompt, one context, one shot. When it fails, the failure is chaotic. Jumping to multi-agent orchestration introduces distributed systems nightmares.

## The Ralph Loop Pattern

**Named after:** Ralph Wiggum from *The Simpsons* (tries the same thing over and over until it works).

**The pattern:** Make "try again with fresh eyes" the default. Wipe the conversation, reload the full specification fresh each iteration, use the filesystem and git as the memory layer.

```bash
while true; do
  claude "implement the next ticket from doc/tickets using TDD"
done
```

**Why it works better than prompting:**
- Models are stochastic (non-deterministic)
- The first iteration produces good but flawed output
- The second pass spots what was missed
- The third handles cleanup
- Objective verification (tests passing, lint clean) is the only exit gate
- No confirmation bias — each iteration starts clean

**Real result:** Geoffrey Huntley delivered an MVP quoted at $50,000 for just 297 in tokens using a single Ralph loop — a 170x cost reduction over the human estimate.

OpenAI's Codex team shipped **1 million lines of code across 1,500 pull requests with zero human-written code** using what they call a "Ralph Wiggum Loop."

## The Inner Loop / Outer Loop Framework

### Inner Loop (seconds)
The agent runs its code, reads the result, and feeds that straight back into its own context — all within a single session. Tighten that loop and the output gets better.

### Outer Loop (hours/days)
What turns one session's hard-won lesson into something every future session starts with.

**Mozilla AI's `cq`** is the cleanest take on this:
- Agents store discoveries as structured **Knowledge Units** (KUs) — undocumented API quirks, workarounds, fixes
- Query the store before retrying a failure — stop rediscovering the same dead ends independently
- A `/cq:reflect` command mines a finished session for lessons worth keeping, ranks them by generalizability, checks for duplicates, and proposes new units
- The store lives locally in SQLite or syncs across a whole team

> "Today's distilled lesson becomes tomorrow's guide — feedforward, in harness terms — so the outer loop quietly improves the inner one over time."

## When to Invest Where

**Invest time in:**
- Building tools that let agents verify their own work (compilation, tests, browser automation, database queries)
- The outer loop: session-end reflection → shared knowledge → next session starts smarter
- CLI tools that are pipeable and progressively explorable (text-in, text-out)

**Don't invest in:**
- Crafting the perfect prompt
- Multi-agent orchestration when a single loop would work
- If the same task can be done by deterministic code: write it once with an LLM, save the code, execute it repeatedly

## Key Takeaway

The prompts and coding agent harnesses will change as models evolve. The value of a tight feedback loop won't. If the AI bubble pops next month, you're left with easy-to-test codebases. If it doesn't, your agents get a little less forgetful with every session.

## Related Concepts
- [[Feedback Loop Engineering]]
- [[Harness Engineering]]
- [[Ralph Loops]]
- [[Mozilla cq]]

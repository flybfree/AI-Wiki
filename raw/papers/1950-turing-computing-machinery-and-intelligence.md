---
title: "Computing Machinery and Intelligence" (Turing Test)
authors: "Alan Turing"
published: "1950-10-01"
arxiv_id: N/A — published in Mind, 1950. Public domain.
tags: [turing-test, imitation-game, philosophy-of-ai, foundations, classic-paper]
source_pages:
  - "ai-ml-foundations-lesson-01-ai-machine-learning-and-deep-learning.md"
related_papers:
  - "2005.14165-gpt3.md"
  - "2017-attention-is-all-you-need.md"
  - "1991-improving-neural-networks-by-preventing-co-adaptation.md"
---

# Computing Machinery and Intelligence

**Alan Turing, published in Mind (1950)**
Originally published as "The Imitation Game" in Mind, Vol. 59, No. 236, pp. 433-460.
Public domain — the arguments are from the original 1950 text.

## Core Question

Turing begins by asking "Can machines think?" and immediately rejects it as too vague because "think" is poorly defined. Instead of arguing about the definition of thought, he proposes a practical replacement:

**"If a machine can play the imitation game well, we should say it thinks."**

This is the famous **Turing Test**, and it shifted the entire conversation about machine intelligence from philosophy to behavior.

## The Imitation Game

Turing describes a simple setup:

Three people communicate by written message:
- A **human interrogator** asks questions
- A **human** tries to convince the interrogator they are human
- A **machine** tries to convince the interrogator it is human

If the interrogator cannot reliably tell who is the machine, the machine has passed the test.

The crucial insight: **It doesn't matter what the machine "is inside." It only matters how it behaves.** This was revolutionary because it moved AI from "can machines think?" to "can machines act intelligently?"

## Key Arguments

### The Digital Computer
Turing argues that digital computers — operating on discrete symbols with finite precision and universal programmability — are the right kind of entity to attempt this task. A universal computer can simulate any algorithm, and if thinking is algorithmic (even partially), a digital computer should be able to do it.

### Learning Machines (Not Just Programmed Machines)
Crucially, Turing did not think machines would pass the test by being hand-coded with every possible answer. He argued the machine should be a **learning machine** — initialized like a child's brain and trained through experience. This is essentially the concept of "machine learning" 30 years before the field existed.

> "Instead of trying to produce a program to simulate the adult mind, why not rather try to produce one which simulates the child?"

This is exactly the approach that modern LLMs follow: start with a general-purpose architecture, train it (like a very long childhood) on vast amounts of data, and let it develop capabilities it was not explicitly programmed with.

### Objections Turing Addressed
Turing anticipated and argued against several objections:

1. **"Theological objection"** — Only a soul can think
2. **"Heads-in-the-sand"** — Machines would destroy humanity
3. **"Mathematical objection"** — Gödel's incompleteness means machines have hard limits
4. **"Argument from consciousness"** — A machine can't truly "experience" anything
5. **"Arguments from various disabilities"** — Machines will never be creative, kind, or conscious

He did not claim machines would pass immediately. He specifically predicted: "I believe that in about fifty years... the average interrogator will not be able to tell the difference between a machine and a human." (He was off by about 70 years, but the direction was correct.)

## Legacy

Turing's paper is the birth certificate of AI as a field. It established:

- The behavior-based approach: judge intelligence by what a system does, not what it "is"
- The learning machine concept: machines should learn, not just be programmed
- The imitation game as a practical test: replace philosophy with experiment
- That digital computers are the right substrate: discrete, programmable, universal

Every modern AI discussion — from the Turing Test to LLMs to AGI debates — traces back to this paper. When people ask "Does it really think?" about an AI system, they are still asking Turing's question.

## For the Course

### Lesson 1 (AI, ML, and Deep Learning)
This paper is the **PRIMARY foundational paper** for the first lesson because:

- It answers the lesson's core question: what does "AI" even mean?
- Turing's rejection of "can machines think?" in favor of "can machines act intelligently?" establishes the behavioral/functional definition that every AI system in the course follows
- His idea of a "learning machine" initialized like a child is the direct ancestor of how we build ML systems today
- It shows AI is about building systems that perform intelligent tasks — not about replicating human thought exactly

### Teaching Notes
- Use the imitation game setup as the primary explanation of the Turing Test
- The "child as learning machine" idea is the most important concept for connecting to modern ML
- Note that Turing predicted the test would be passable by 2000 — nobody then (2000s) thought it would happen, but LLMs in the 2020s have gotten close on conversation tests
- End by asking students: "If you couldn't tell a chatbot from a human in a text chat, would you say it thinks?" — this brings the lesson full circle

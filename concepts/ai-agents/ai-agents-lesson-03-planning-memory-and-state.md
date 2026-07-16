---
title: "AI Agents Lesson 3 - Planning, Memory, and State"
date: 2026-07-15
status: draft
tags: [lesson, agents, memory, planning]
---

# Lesson 3: Planning, Memory, and State

**Source**: [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · [EurekAgent paper](http://arxiv.org/abs/2606.13662v1) · [LangGraph agents docs](https://docs.langchain.com/oss/python/langchain/agents)

## Lesson goal
Show how agents keep track of what they are doing across multiple steps.

## Why planning matters
A hard task usually cannot be solved in one shot.
Planning breaks a goal into manageable steps so the agent can work in sequence instead of guessing all at once.

A plan is not a promise that every step is fixed forever.
It is a working hypothesis: “This is the order that seems most likely to succeed.”
The agent should be allowed to revise that order if new information changes the task.

## Why memory matters
Memory helps the system avoid starting over every turn.
It can preserve:
- the current goal
- what has already been tried
- user preferences
- useful facts from earlier steps

Memory is only useful if the system knows what should be kept and what should be forgotten.
Too much memory creates noise.
Too little memory creates repetition.

## Why state matters
State is the working record of the current run.
It tells the agent:
- where it is in the task
- what has already happened
- what still needs to happen
- what should be remembered for the next step

State is usually more local and more temporary than memory.
You can think of state as the live notebook for the current job.

## Useful distinctions
- **Plan**: the intended sequence of steps
- **State**: the current working context
- **Short-term memory**: what matters in this run
- **Long-term memory**: what should survive across runs

## Simple mental model
Planning says *what should happen next*.
State says *what has already happened*.
Memory says *what should not be forgotten*.

That distinction sounds small, but it prevents a lot of design mistakes.
If a system does not separate them, it tends to lose track of progress.

## Where state lives
State can live in different places:
- a structured object in the harness
- a scratchpad or scratch file
- the conversation history
- a task tracker or checkpoint store

The point is not the storage medium.
The point is that the agent can recover its current position after each step.

## Why it matters
Multi-step work fails when the agent:
- forgets the objective
- repeats the same action
- loses track of progress
- drifts into irrelevant details
- cannot recover from a partial failure

The harness often matters more than the model here because it manages checkpoints, summaries, and context.

## Concrete example
A research agent may:
1. gather sources
2. summarize each source
3. compare the findings
4. draft a synthesis
5. revise based on feedback

The plan keeps the steps in order.
The state keeps the current position.
Memory keeps the important facts available.

## When memory should be short
Not every fact should be saved forever.
Useful memory is selective:
- preferences worth reusing
- project facts that stay relevant
- task progress that must survive a break

Everything else can stay local to the current run.
If the system stores too much, it makes the next step harder to reason about.

## Long-horizon work
Long-horizon agents are systems that can stay coherent across many steps or even many turns.
That requires more than a big context window.
It needs disciplined state handling, summarization, and error recovery.

A good long-horizon system usually has:
- a way to checkpoint progress
- a way to compress older steps
- a way to revisit failed branches
- a way to keep the goal visible

## Failure modes
- plan is too rigid and cannot adapt
- state is too vague and does not show progress
- memory is too sticky and keeps stale facts
- memory is too thin and forgets important facts
- checkpoints are missing, so recovery is impossible

## Build this
Sketch a state model for a research agent:
- goal
- current step
- completed steps
- saved notes
- stop conditions

Then ask: what belongs in memory, and what should stay temporary?

## Exercises
1. Why do agents need plans?
2. What is the difference between memory and state?
3. Why do multi-step systems fail?
4. Why is the harness important?

## Practical takeaway
If a task has more than one meaningful step, design the state model before you design the prompt.
A good prompt with bad state handling still fails.

## Key takeaways
- Planning breaks work into steps.
- State tracks where the system is.
- Memory preserves what should survive across steps.
- Multi-step agents fail when they lose track of progress.
- The harness is often the real differentiator.

## Review checklist
- Can you explain plan, state, and memory as different things?
- Can you say why long tasks need checkpoints?
- Can you identify what should and should not be saved in memory?
- Can you explain why summary and compaction matter?

## Glossary
- **Plan**: the intended order of steps
- **State**: the current working record
- **Memory**: information preserved across steps or sessions
- **Checkpoint**: a saved point the system can return to
- **Long-horizon agent**: an agent that stays coherent across many steps

## Quick self-check
1. Why do agents need plans?
2. What is the difference between memory and state?
3. Why do multi-step systems fail?
4. Why is the harness important?

## Research slots to add later
- long-horizon agent research
- context engineering and compaction
- environment engineering and permission design

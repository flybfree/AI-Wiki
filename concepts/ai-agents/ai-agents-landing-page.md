---
title: "AI Agents Landing Page"
date: 2026-07-16
status: draft
tags: [ai, agents, landing-page, course]
---

# AI Agents

**Source**: [OpenAI: A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) · [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · [LangGraph agents docs](https://docs.langchain.com/oss/python/langchain/agents)

This page is the entry point for a concept-first lesson series on AI agents.
The goal is to start with the simplest definition, then build up the pieces that make agents useful in practice: harnesses, tools, planning, memory, retrieval, guardrails, and orchestration.

## Course design
- Keep the series concept-first and math-light
- Start with the agent loop before naming frameworks
- Use concrete workflow examples instead of abstract theory
- Add research depth after the framework is stable
- Show the harness as the implementation layer that makes the agent real
- Give every lesson a fuller explanation, a worked example, failure modes, and a build task
- Include review questions, exercises, and a small build task in every lesson
- Keep lessons detailed enough to teach the idea without requiring a second source

## Lesson map
1. [[ai-agents-lesson-01-what-an-ai-agent-is.md|Lesson 1: What an AI Agent Is]]
2. [[ai-agents-lesson-02-harness-implementing-an-agent.md|Lesson 2: The Harness: Implementing an Agent]]
3. [[ai-agents-lesson-02-tools-actions-and-observation-loops.md|Lesson 3: Tools, Actions, and Observation Loops]]
4. [[ai-agents-lesson-03-planning-memory-and-state.md|Lesson 4: Planning, Memory, and State]]
5. [[ai-agents-lesson-04-retrieval-context-and-long-context-work.md|Lesson 5: Retrieval, Context, and Long-Context Work]]
6. [[ai-agents-lesson-05-guardrails-evaluation-and-reliability.md|Lesson 6: Guardrails, Evaluation, and Reliability]]
7. [[ai-agents-lesson-06-single-agent-and-multi-agent-architectures.md|Lesson 7: Single-Agent and Multi-Agent Architectures]]

## How to read the series
- Read lessons in order the first time
- Revisit lessons 2 through 6 when you start building or reviewing an agent
- Use lesson 7 to decide whether a simple agent, router, or multi-agent design fits the task

## Framework summary
- **Agent**: a system that tries to achieve a goal by taking actions
- **Harness**: the control layer that turns model output into a real loop
- **Tool use**: the agent can call external functions or systems
- **State**: the agent keeps track of what happened so far
- **Retrieval**: the agent can pull in outside knowledge when needed
- **Guardrails**: the agent is constrained so action stays safe and useful
- **Orchestration**: the harness manages the loop, retries, approvals, and logging

## Next research pass
The next pass should expand each lesson with:
- current product patterns from OpenAI, Anthropic, and LangGraph
- practical examples of single-agent vs multi-agent design
- evaluation and safety patterns from recent agent research
- current papers on environment engineering, trust, and long-horizon control

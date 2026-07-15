---
title: "AI Agents Lesson 6 - Single-Agent and Multi-Agent Architectures"
date: 2026-07-15
status: draft
tags: [lesson, agents, architecture, multi-agent]
---

# Lesson 6: Single-Agent and Multi-Agent Architectures

**Source**: [LangGraph](https://www.langchain.com/langgraph) · [OpenAI Agent Builder](https://developers.openai.com/api/docs/guides/agent-builder) · [TrustedARI: Towards Trust-Native Agentic Routing Infrastructure for Agentic AI](https://arxiv.org/abs/2606.15822)

## Lesson goal
Show how to choose between one agent, a routed system, or many cooperating agents.

## Start simple
Not every problem needs a swarm.
Often the best design is one agent with a few strong tools.

Multi-agent systems are useful, but they add coordination cost.
If the task is narrow, a single agent is usually easier to build, test, and trust.

## Core patterns
### Single agent
One loop, one decision-maker, one harness.
This is the simplest useful agent design.

### Router
A dispatcher sends work to the right path or specialist.
This works well when tasks have clear categories.

### Hierarchical agent
A manager agent delegates to specialist agents.
This is useful when work can be split into subtasks with different skills.

### Multi-agent team
Several agents cooperate on different parts of a larger task.
This can help when the task is naturally parallel or strongly specialized.

## How to choose
Choose simple if the task is:
- narrow
- well-bounded
- low variance
- easy to verify

Choose routed if the task:
- falls into distinct categories
- benefits from specialization
- needs different tool sets

Choose multi-agent if the task:
- has truly separate subtasks
- benefits from parallel work
- requires distinct roles like planner, researcher, reviewer, or executor

## The tradeoff
More agents can mean more capability.
They also mean:
- more coordination
- more failure modes
- more logging burden
- more cost
- more debugging complexity

The architecture should match the problem, not the hype.

## Concrete examples
### Example 1: single agent coding helper
One agent reads the repo, edits files, and runs tests.

### Example 2: routed support system
One route handles billing, one handles technical issues, one handles account changes.

### Example 3: research team
One agent gathers sources, one summarizes them, one checks claims, and one composes the final draft.

## Why routing and trust matter
Trusted routing is important when the system needs to send sensitive or high-stakes work through controlled paths.
That is one reason trust-native agent routing research matters.

## Build this
Choose an architecture for each of these:
- email triage assistant
- coding review assistant
- research brief generator

For each, say whether you would use a single agent, router, or multi-agent team, and why.

## Exercises
1. When is a single agent enough?
2. Why do multi-agent systems add overhead?
3. What is the difference between a router and a hierarchical agent?
4. When does specialization help?

## Practical takeaway
Start with one agent.
Add routing when categories emerge.
Add multiple agents only when the task really benefits from specialization or parallelism.

## Key takeaways
- Simple beats complex when the task allows it.
- Router and hierarchy patterns reduce unnecessary complexity.
- Multi-agent systems add coordination overhead.
- Choose architecture based on task shape, not novelty.
- Trust and routing become important as the system grows.

## Review checklist
- Can you explain each of the core patterns?
- Can you say when a router is better than a swarm?
- Can you name the main overheads of multi-agent systems?
- Can you justify a design choice for a real task?

## Glossary
- **Single agent**: one agent loop handling the task end to end
- **Router**: a dispatcher that chooses the right path or specialist
- **Hierarchical agent**: a manager agent delegating to subagents
- **Multi-agent system**: multiple agents cooperating on a task
- **Coordination cost**: the overhead of keeping multiple agents aligned

## Quick self-check
1. When is a single agent enough?
2. Why do multi-agent systems add overhead?
3. What is the difference between a router and a hierarchical agent?
4. When does specialization help?

## Research slots to add later
- current framework comparisons
- hierarchical routing patterns
- trust and governance research for multi-agent systems

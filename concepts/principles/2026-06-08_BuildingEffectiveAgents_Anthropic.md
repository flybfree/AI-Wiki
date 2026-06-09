---
title: Building Effective Agents (Anthropic)
date: 2026-06-08
type: article-summary
tags: [agent-design, principles, workflows, agents, harness, ACI]
sources:
  - https://www.anthropic.com/research/building-effective-agents
---

# Building Effective Agents (Anthropic)

## Summary

Anthropic's engineering team shares lessons from working with dozens of teams building LLM agents. The core thesis: **simple, composable patterns beat complex frameworks**. The most successful implementations use basic building blocks rather than specialized libraries.

## Key Principles

1. **Start simple** -- optimize single LLM calls with retrieval and in-context examples before adding multi-step agentic systems
2. **Workflows vs Agents** -- workflows use predefined code paths; agents let the LLM dynamically direct its own process
3. **Frameworks are optional** -- Claude Agent SDK, Strands SDK, Rivet, Vellum make it easy to start, but add abstraction layers that obscure debugging
4. **The augmented LLM is the building block** -- LLM + retrieval + tools + memory
5. **Measure performance and iterate** -- add complexity only when it demonstrably improves outcomes

## Five Workflow Patterns

1. **Prompt Chaining** -- decompose into fixed sequence; trade latency for accuracy
2. **Routing** -- classify input, direct to specialized followup; separate concerns
3. **Parallelization** -- section (independent subtasks) or voting (multiple attempts); speed or confidence
4. **Orchestrator-Workers** -- central LLM dynamically breaks down tasks, delegates, synthesizes; flexibility over pre-defined paths
5. **Evaluator-Optimizer** -- generate + evaluate in loop; clear criteria + measurable improvement

## Agent Design

- Agents = LLM using tools based on environmental feedback in a loop
- Start with user command or interactive discussion, then operate independently
- Gain "ground truth" from environment at each step
- Pause for human feedback at checkpoints
- Include stopping conditions (max iterations) for control

## Three Core Principles for Implementation

1. **Maintain simplicity** in agent design
2. **Prioritize transparency** -- explicitly show planning steps
3. **Craft the agent-computer interface (ACI)** -- tool documentation and testing

## Agent-Computer Interface (ACI)

Tools deserve as much prompt engineering attention as overall prompts. Guidelines:

- Give the model tokens to "think" before writing
- Keep formats close to naturally occurring text
- No formatting overhead (e.g., counting lines, string escaping)
- Put yourself in the model's shoes -- is it obvious how to use this tool?
- Test how the model uses tools; iterate on mistakes
- Poka-yoke your tools -- make it harder to make mistakes
- Use absolute filepaths over relative paths

## Best Application Domains

- **Customer support** -- conversation flow + external data + programmatic actions
- **Coding agents** -- verifiable through tests, iterative feedback, well-defined problem space

## Key Insight

> "Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."

## Cross-References

- Lesson 13: Agents and Agentic Workflows
- Autonomous Agent Frameworks
- Agent Architecture Evolution
- Code as Agent Harness paper

---
title: "AI Agents Syllabus"
date: 2026-07-16
status: draft
tags: [ai, agents, syllabus, course]
---

# AI Agents Syllabus

**Source**: [OpenAI: Building agents](https://developers.openai.com/tracks/building-agents) · [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) · [OpenAI Agent Builder](https://developers.openai.com/api/docs/guides/agent-builder)

This syllabus defines the teaching shape for the AI Agents lesson set.
It is intentionally practical: the point is to understand when an agent helps, what can go wrong, and how the surrounding harness makes the system reliable.

## Teaching principles
- Start from the user task, not the model internals
- Separate the model from the harness around it
- Show one concrete workflow per concept
- Prefer plain-language definitions on first use
- Add research detail only after the framework is clear
- Make the explanation detailed enough that each lesson can stand on its own

## What the series covers
- What an agent is and what it is not
- Tool calling and environment interaction
- Planning, memory, and state management
- Retrieval and long-context workflows
- Guardrails, approvals, and evaluation
- Single-agent, router, and multi-agent designs

## What the series does not try to do yet
- Full code implementation tutorials
- Vendor-specific product docs as the main structure
- Deep math or training theory
- Overly abstract agent taxonomy without examples

## Pacing
- Each lesson should fit in a focused 30 to 60 minute read
- The first pass should be readable without code
- Code examples can be added later as a second layer
- The lesson text should be detailed enough that a reader can understand the idea without having to infer the missing steps

## Success criteria
A reader should be able to:
- explain an AI agent in one sentence
- identify the main parts of an agent loop
- tell when a workflow needs tools, memory, or retrieval
- recognize the main reliability risks
- choose between a simple agent and a more complex architecture

## Research notes to add later
- current best practices for tool design
- current agent evaluation and benchmark patterns
- environment engineering and permission models
- long-horizon and multi-agent coordination research

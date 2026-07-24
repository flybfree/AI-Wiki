---
title: AnovaX: A Local, Multi-Agent Voice Assistant with LLM Planning, Typed Executors, and Adaptive Recovery
url: http://arxiv.org/abs/2607.15367v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_18-09-36Z_AnovaX_ALocal_Multi_AgentVoiceAssistantwithLLMPlan.md
generated_at: 2026-07-23 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
AnovaX is a local, multi‑agent voice assistant that runs entirely on the user’s computer, handling wake detection, speech processing, and task execution without sending data to the cloud. The system uses an LLM planner (Gemini) to generate JSON plans, which are translated into typed child agents running on a bounded thread pool, with an adaptive recovery loop that restarts failed steps using ReAct‑style prompts.

## Key Takeaways
- AnovaX replaces cloud pipelines with a local workflow where raw audio is processed in a single Python process and all actions occur inside the desktop environment.  
- The planner can delegate sub‑goals to itself at most two levels deep, enabling recursive task composition while keeping nesting limited.  
- A Flask server mirrors each agent’s lifecycle event to a phone over WiFi, streams screen activity via MJPEG, and streams audio back, allowing remote control without exposing the LLM to the keyboard.

## Context
Desktop voice assistants have traditionally relied on cloud‑based skill sets that expose fixed functions, limiting personalization and privacy. AnovaX demonstrates that a compact, few‑thousand line local assistant can perform complex coordination tasks such as opening apps, typing, searching, and handling concurrent actions without requiring an LLM to touch the keyboard.

## Implications
This work shows that local AI assistants can achieve legible user interaction with minimal infrastructure, reducing latency and data exposure. For developers and researchers, AnovaX provides a template for building privacy‑preserving, offline agents that can be extended with new tools while maintaining robust recovery mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15367v1)

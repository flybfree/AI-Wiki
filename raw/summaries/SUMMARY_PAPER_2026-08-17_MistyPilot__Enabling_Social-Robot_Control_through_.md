---
title: MistyPilot: Enabling Social-Robot Control through Multi-Agent LLM Skill Orchestration
url: http://arxiv.org/abs/2608.15549v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_05-45-16Z_MistyPilot_EnablingSocial_RobotControlthroughMulti.md
generated_at: 2026-08-17 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MistyPilot, a multi‑agent language model framework that translates natural‑language commands into actions on the social robot Misty. By separating physical control and social interaction into two specialized agents, MistyPilot achieves high routing accuracy and lower variance than a single‑agent baseline while users report positive usability.

## Key Takeaways
- The Task Router efficiently assigns instructions to either a Physically Interactive Agent that triggers sensor events or a Social Interaction Agent that manages dialogue state, demonstrating robust skill dispatch up to 100 skills.  
- Skill extension is supported through result reuse and full generation, allowing the system to handle both incremental updates and new tasks without re‑binding sensors.  
- User studies with twelve participants show positive perceptions of usability and interaction quality, confirming that multi‑agent orchestration improves perceived performance.

## Context
Current social robot development struggles with integrating reactive physical behaviors and stateful conversational flows within a single programming pipeline. Existing solutions often require manual API composition and runtime state management, limiting rapid iteration and user experience. MistyPilot addresses this gap by automating the integration of multiple skill types through an LLM‑driven orchestration model.

## Implications
For robotics engineers, MistyPilot reduces development time and complexity by abstracting sensor‑skill binding into a language model’s routing logic. In industry, it enables scalable deployment of diverse social robots without extensive manual configuration. Practitioners can leverage the framework to prototype complex human‑robot interactions that combine precise physical actions with natural conversational responses.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15549v1)

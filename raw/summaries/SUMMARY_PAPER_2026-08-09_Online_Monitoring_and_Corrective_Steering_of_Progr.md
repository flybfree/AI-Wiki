---
title: Online Monitoring and Corrective Steering of Programming Agents
url: http://arxiv.org/abs/2608.06701v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_01-54-52Z_OnlineMonitoringandCorrectiveSteeringofProgramming.md
generated_at: 2026-08-09 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LivePlan, a system that monitors and corrects inefficient or erroneous behavior of programming agents during GitHub issue resolution. By separating judgment from advice, LivePlan detects issues early with a rule‑based monitor and only invokes an LLM advisor when needed, improving resolution rates by up to 15.2% while adding minimal cost.

## Key Takeaways
- LivePlan uses a deterministic rule‑based monitor that watches general signals over the agent’s trajectory to identify inefficiencies without relying on large language models for judgment.  
- When an issue is detected, the system consults an LLM advisor only for high‑level correction steps, preventing costly re‑planning and repeated failed actions.  
- Evaluation across SWE‑bench Verified and Pro shows consistent gains of 9.9% on average, with additional successes on medium and hard instances, while incurring just $0.08 per instance.

## Context
This work addresses a longstanding challenge in automated software engineering: the inefficiency and error prone nature of large‑scale issue fixing where agents drift from their goals or repeat actions. The approach of decoupling monitoring from advisory reasoning aligns with broader efforts to make AI systems more reliable and cost effective, especially as LLM usage expands.

## Implications
For practitioners, LivePlan demonstrates that lightweight monitoring can yield significant performance improvements without heavy computational overhead, encouraging adoption in real‑world code review pipelines. In the field, it sets a precedent for integrating rule‑based detectors with LLM advisors to balance speed, accuracy, and resource use.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06701v1)

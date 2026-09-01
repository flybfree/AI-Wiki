---
title: SIR: Self-improving Red-teaming for Compute Use Agents
url: http://arxiv.org/abs/2608.30207v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_03-39-43Z_SIR_Self_improvingRed_teamingforComputeUseAgents.md
generated_at: 2026-08-31 21:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SIR, a black‑box red‑team framework that attacks computer‑use agents (CUAs) at the operating system level to uncover indirect prompt injection vulnerabilities. By composing stealthy injections from reusable plain‑language principles and iteratively refining them based on diagnostic feedback, SIR achieves higher success rates than manually written attacks while leaving benign tasks unaffected.

## Key Takeaways
- SIR composes attacks from a small library of language‑based principles that are applied across multiple tasks without needing additional feedback.  
- The iterative loop diagnoses failed trajectories and distills new strategies, raising attack success rates from 4% to 24% on Claude Opus 4.8 and from 0% to 28% on Gemini 3.5 Flash while still completing the benign task.  
- Principles discovered against one model transfer to a different architecture without further adaptation, indicating broad vulnerability.

## Context
Computer‑use agents are rapidly integrated into everyday workflows, making them attractive targets for adversarial manipulation. Existing safety benchmarks rely on static, handcrafted injections that do not reflect adaptive threats. This research bridges the gap by providing an automated, OS‑level red‑team approach that evaluates real vulnerability surfaces.

## Implications
For practitioners, SIR highlights the need to monitor filesystem, service, and permission states rather than relying solely on LLM judgments for safety testing. The findings urge developers to adopt iterative adversarial feedback loops in CUA design to prevent undetected exploitation across diverse models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30207v1)

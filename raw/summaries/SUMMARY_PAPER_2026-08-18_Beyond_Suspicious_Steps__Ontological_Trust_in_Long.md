---
title: Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents
url: http://arxiv.org/abs/2608.17718v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_12-44-43Z_BeyondSuspiciousSteps_OntologicalTrustinLong_Horiz.md
generated_at: 2026-08-18 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ontological trust as a task‑conditioned property that measures how well an agent’s trajectory prefixes align with the user‑authorized role and goal, especially in long‑horizon settings where drift can accumulate over many steps. It presents RGE, an online monitor that decomposes trust into Role, Goal, and Evidence components using LLMs only for structured representations while keeping updates deterministic. On a cross‑domain corpus, RGE outperforms rule‑based, judge‑style, and shield baselines on detecting prefix‑paired drift, achieving high detection rates with minimal false positives.

## Key Takeaways
- Ontological trust is defined as the alignment of trajectory prefixes with the authorized task role and goal, not just local step validity.  
- RGE uses LLMs solely to generate structured representations; all trust updates are deterministic, producing an auditable replayable trust trajectory.  
- The method achieves over 93% drift F1 on all benchmarks while maintaining benign coverage above 95.8%, showing strong performance even for pseudo‑consistency failures.

## Context
Long‑horizon agents often operate across multiple tools and observations, making oversight challenging because local compliance does not guarantee overall task fidelity. Existing monitors either focus on final outcomes or provide generic risk scores, leaving the prefix‑level trust gap unaddressed. This work fills that gap by introducing a principled measure of trust that can be monitored continuously.

## Implications
For practitioners developing autonomous agents, ontological trust offers a transparent way to detect unauthorized role shifts early in execution. Industry adoption could improve safety and accountability in high‑stakes domains such as finance or healthcare where subtle drifts may have serious consequences. The deterministic nature of RGE also enables regulatory compliance through reproducible audit trails.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17718v1)

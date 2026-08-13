---
title: Language-Structured Relational Q-Learning for Threat-Aware Control in Safety-Critical Driving
url: http://arxiv.org/abs/2608.11498v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_23-24-01Z_Language_StructuredRelationalQ_LearningforThreat_A.md
generated_at: 2026-08-12 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Language-Structured Relational Q-Learning to train driving policies from natural‑language scenario descriptions in safety‑critical driving. It shows that training with language data improves threat detection but does not lead to better control performance, revealing a recognition‑control gap. Across 2500 scenarios the success rate rises modestly while adversary attention doubles.

## Key Takeaways
- Language descriptions improve threat relevance inference from kinematics alone, increasing adversary‑focused attention from 1.2x to 2.1x.
- The model’s test success improves only slightly from 49–52% to 55–58%, suggesting limited control gains.
- Despite richer representation, simple policies solve 76% of scenarios, indicating policy collapse after reward reweighting.

## Context
Natural‑language scenario generation is a promising way to encode rare driving interactions without large datasets. This work tests whether such textual cues can be leveraged for adaptive safety‑critical control within reinforcement learning frameworks.

## Implications
The findings caution that richer representations do not automatically translate into safer policies, urging researchers to align recognition and control objectives more tightly. For industry practitioners, the gap highlights a need for hybrid approaches that combine threat awareness with robust action selection in autonomous driving systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11498v1)

---
title: Staying on the Attack Path: Structured State for Long-Horizon Automated Penetration Testing
url: http://arxiv.org/abs/2609.07344v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_11-09-01Z_StayingontheAttackPath_StructuredStateforLong_Hori.md
generated_at: 2026-09-08 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Intentest, a system that keeps long‑horizon penetration testing agents focused by externalizing state onto an intent‑graph DAG. It reduces invalid transitions and improves success rates on real CTF challenges. The benchmark shows overall 88.2% success with 75% on hard tasks, beating baselines by 44–50 points.

## Key Takeaways
- Intentest stores verified network states as immutable fact nodes in a persistent DAG to prevent context forgetting.
- Exploration directions are limited by intent edges that depend on those facts, avoiding aimless repetition.
- The system’s three‑layer architecture and five‑stage filtering cut average rounds for medium and hard tasks by 33% and 48%.

## Context
LLM agents struggle with long‑term reasoning because their context windows expire, causing loss of critical facts. This work addresses that limitation by moving state outside the model.

## Implications
For cybersecurity practitioners, Intentest offers a reliable framework for automated testing across varied difficulty levels. It can be integrated into larger orchestration pipelines to maintain consistent progress over extended tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07344v1)

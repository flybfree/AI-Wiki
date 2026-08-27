---
title: LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents
url: http://arxiv.org/abs/2608.25777v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_13-20-27Z_LocalLSTC_ALongShort_TermControlArchitectureforLoc.md
generated_at: 2026-08-26 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LocalLSTC, a training-free architecture that organizes control information temporally for locally deployed GUI agents. By separating long‑term control from short‑term execution, the method improves performance on benchmark suites such as OSWorld and WindowsAgentArena compared to prior local approaches.

## Key Takeaways
- Replacing GPT‑5 with Qwen3.5‑9B drops OSWorld SR‑100 from 60.9 % to 37.7 %, highlighting the impact of control information loss in trajectory reconstruction.  
- Annotation of failed trajectories shows at least one control failure occurs in 91.6 % of cases, underscoring the need for persistent state management.  
- LocalLSTC reaches 64.7 % SR‑100 on OSWorld and 65.3 % on WindowsAgentArena, outperforming the strongest prior local results.

## Context
GUI‑agent frameworks increasingly rely on frontier API models to perform complex desktop tasks, but they often lack mechanisms to retain control information across steps. This creates a gap where short‑term reasoning is insufficient for long‑running interactions, limiting reliable automation capabilities.

## Implications
The temporal organization of control information identified by LocalLSTC offers a scalable pattern for future locally deployed agents, enabling more robust and efficient desktop automation without retraining models. Practitioners can adopt this architecture to improve reliability in real‑world GUI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25777v1)

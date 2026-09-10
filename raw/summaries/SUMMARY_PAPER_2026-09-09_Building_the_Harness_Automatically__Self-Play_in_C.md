---
title: Building the Harness Automatically: Self-Play in Code Distills a Text Harness for Black-Box Optimization
url: http://arxiv.org/abs/2609.09468v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-08_21-33-55Z_BuildingtheHarnessAutomatically_Self_PlayinCodeDis.md
generated_at: 2026-09-09 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether an agent can learn a numerical search strategy through executable practice and then translate that strategy into a concise textual harness for black‑box optimization. The distilled harness A reduces Gemini Flash regret by 48 % in an independent study, matches the performance of state‑of‑the‑art optimizers on the practice family, and improves all three BBOB landscapes. Moreover, the same text deploys to Claude Sonnet with comparable gains and achieves the lowest regret on a sealed YouTube reward‑tuning benchmark.

## Key Takeaways
- Harness A cuts Gemini Flash regret by 48 % (p<.001) while entering the GP‑BO performance range, demonstrating that a compact text can match strong optimizers.  
- The same harness improves every tested Gemini executor and transfers to Claude Sonnet, lowering regret by 43 % and 49 % respectively (p≤.005).  
- An independent end‑to‑end replication produces Harness B, a different program with identical performance, confirming the robustness of the distillation process.

## Context
The work addresses low‑budget black‑box optimization where language models underperform classical methods despite their expressive power. By treating optimizer programs as executable code and distilling them into human‑readable text, the study bridges the gap between algorithmic discovery and practical deployment. This approach aligns with broader trends toward interpretable AI and automated tool generation.

## Implications
For researchers, the findings suggest that language can serve as a portable medium for deploying learned search policies without retraining models. For industry practitioners, harnesses enable rapid integration of optimized strategies across different execution environments, reducing development time and cost. The ability to produce reproducible, low‑budget optimizers could democratize high‑performance black‑box solutions in diverse domains such as reinforcement learning, resource allocation, and production tuning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09468v1)

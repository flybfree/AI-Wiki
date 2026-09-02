---
title: Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs
url: http://arxiv.org/abs/2609.01573v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_17-39-55Z_ScalingNear_OptimalSFT_RLAnnotationBudgetAllocatio.md
generated_at: 2026-09-01 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the challenge of allocating a fixed annotation budget between supervised fine‑tuning and reinforcement learning during large language model post‑training. It shows that the near‑optimal allocation region is surprisingly wide even for small tolerances, widens as models grow larger, and reliably transfers from small proxy experiments to full‑scale training.

## Key Takeaways
- The near‑optimal SFT‑RL ratio forms a broad region rather than a single point, persisting within 2–10% of peak performance.  
- This region expands with model scale, making allocation easier for larger LLMs.  
- Small proxy‑model experiments can identify a transferable allocation that works across tasks and RL methods.

## Context
Current LLM fine‑tuning pipelines often rely on heuristic splits that ignore the trade‑off between annotation cost and performance gain. The lack of principled, scalable guidance hampers efficient deployment as models become more complex.

## Implications
Practitioners can focus limited resources on a narrow set of experiments rather than exhaustive searches, accelerating model rollout. This insight reduces development time and costs while maintaining high quality across diverse applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01573v1)

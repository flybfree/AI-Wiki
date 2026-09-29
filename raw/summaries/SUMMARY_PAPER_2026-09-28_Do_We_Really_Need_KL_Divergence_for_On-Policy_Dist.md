---
title: Do We Really Need KL Divergence for On-Policy Distillation of Large Language Models?
url: http://arxiv.org/abs/2609.33791v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_17-40-33Z_DoWeReallyNeedKLDivergenceforOn_PolicyDistillation.md
generated_at: 2026-09-28 22:02
model: qwen3.6-35b-a3b
---

## Summary
This paper challenges the reliance on KL divergence as the standard loss in On-Policy Distillation (OPD) for large language models, demonstrating that preserving the update direction toward the teacher is sufficient for effective distillation. The authors reveal that only a small subset of tokens with strong teacher-student disagreement requires directional alignment, while other tokens can diverge without harming performance. Leveraging these insights, they propose Consensus Multi-Teacher On-Policy Distillation (C-MOPD), which supervises samples using

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33791v1)

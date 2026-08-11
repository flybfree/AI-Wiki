---
title: MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models
url: http://arxiv.org/abs/2608.08503v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_05-50-30Z_MathShikkha_AControlledStudyofAnswer_OnlyandChain_.md
generated_at: 2026-08-10 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether teacher‑generated Bangla chain‑of‑thought (CoT) supervision yields benefits beyond standard answer‑only fine‑tuning for small language models. We find that CoT improves the weak 4B model by 18.6 points on an in‑domain task but does not significantly affect three stronger backbones, while it reverses this pattern on a larger benchmark and preserves out‑of‑domain performance.

## Key Takeaways
- CoT supervision generates 15–52× more tokens than answer‑only training but shows no statistically significant in‑domain gain for three stronger models (p ≥ 0.17).  
- On the contamination‑audited BanglaMATH benchmark, CoT outperforms answer‑only by 20–28 points across all four models with p < 0.0001.  
- Human evaluation shows no increase in reasoning validity but higher target‑language adherence and inspectable reasoning, measured by κ = 0.76–1.00.

## Context
This work addresses the challenge of transferring math reasoning to low‑resource languages where large models may be impractical. It demonstrates that CoT can enhance language alignment without requiring massive model sizes.

## Implications
For practitioners, it suggests that CoT can be a useful tool for improving language alignment and auditability without boosting in‑domain scores when backbones are weak. It also highlights the importance of benchmark selection to avoid overfitting to noisy data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08503v1)

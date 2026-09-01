---
title: Manacá-1B: An Open, Reproducible Brazilian-Portuguese Language Model and a Tokenizer-Aware, Paired Evaluation
url: http://arxiv.org/abs/2608.30114v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_01-00-14Z_Manacá_1B_AnOpen_ReproducibleBrazilian_PortugueseL.md
generated_at: 2026-08-31 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces Manacá-1B, an open decoder‑only Brazilian Portuguese language model trained from scratch with a fully containerized pipeline that is stable and reproducible. It evaluates the model against nine existing baselines on four Portuguese benchmarks using a single harness that reports standard errors and paired significance tests. The results show the model outperforms several smaller models on last‑word prediction while performing near chance on reasoning tasks.

## Key Takeaways  
- The training pipeline never skips steps or produces NaN loss, and all logs are released for full reproducibility.  
- Manacá-1B exceeds Tucano‑1b1 and Tucano‑2b4 on LAMBADA‑PT with large paired margins, confirming its strength below the 7 B scale.  
- A tokenizer conversion pitfall drops capitalized tokens to a byte fallback, lowering LAMBADA‑PT accuracy from 45.3 to 25.0; a one‑line fix restores the original normalizer.

## Context  
Brazilian Portuguese suffers from limited open language model support, and many released models lack transparent training procedures or uncertainty measures. This work addresses those gaps by providing a complete, reproducible dataset and evaluation framework that can be benchmarked against state‑of‑the‑art baselines.

## Implications  
For researchers, the release of raw logs and corrected tokenizer enables independent verification of reported numbers, fostering trust in model claims. For practitioners, the toolkit demonstrates how small but critical implementation details affect performance, guiding robust deployment practices for under‑served languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30114v1)

---
title: On-Policy Self-Distillation without Any Supervision
url: http://arxiv.org/abs/2608.06296v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_17-18-23Z_On_PolicySelf_DistillationwithoutAnySupervision.md
generated_at: 2026-08-06 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Unsupervised On‑Policy Self‑Distillation (U‑OPSD), a method that enables large language models to improve their performance using only their own generated outputs. By enforcing internal consistency and conditioning on the shortest pseudo‑solution, U‑OPSD distills corrections into prefixes of longest incorrect completions, achieving gains comparable to or exceeding supervised approaches across multiple benchmarks.

## Key Takeaways
- U‑OPSD relies solely on a model’s own rollouts to build a pseudo‑solution via majority vote under a self‑consistency threshold.  
- The teacher distribution is conditioned on the shortest pseudo‑solution, and distills it into prefixes of the longest incorrect completion, allowing precise correction where confidence is high.  
- Across AIME24, AIME25, HMMT25, MATH500, AMC23, U‑OPSD improves base models by 8.5%–10.7% on Qwen3 non‑thinking mode and outperforms OPSD by an average of 3.2%–2.3%, while matching or exceeding supervised methods like GRPO.

## Context
Self‑distillation aims to let large language models learn from their own outputs without external supervision, reducing reliance on costly human labels or ground truth. This work demonstrates that internal consistency can serve as a robust signal for model refinement, aligning with broader trends toward efficient and scalable training pipelines in AI research.

## Implications
U‑OPSD offers a practical pathway to enhance existing LLMs with minimal additional data, lowering the barrier to high performance for industry practitioners. By enabling continuous self‑improvement, it could streamline deployment cycles and support more reliable reasoning capabilities across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06296v1)

---
title: RecurTrace: Adaptive Latent Reasoning with Loop-Time Memory
url: http://arxiv.org/abs/2609.03379v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_05-29-24Z_RecurTrace_AdaptiveLatentReasoningwithLoop_TimeMem.md
generated_at: 2026-09-03 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RecurTrace, an adaptive looping mechanism that lets language models reuse intermediate computations across iterations without adding parameters or tokens. By letting each looped layer attend to its own past states and using a halting head guided by an oracle, the model can decide when extra depth is beneficial. On MathQA with matched compute, RecurTrace reaches 56.9% accuracy at two loops, surpassing fixed‑depth baselines by two points.

## Key Takeaways
- Loop Memory Attention enables each looped layer to reference its own states from earlier iterations along the loop‑time axis instead of only the latest output.
- A halting head predicts whether additional depth still reduces loss using supervision from an oracle that identifies optimal stopping points.
- RecurTrace outperforms fixed‑depth baselines on MathQA, achieving higher accuracy with fewer loops and improving generation accuracy across model sizes.

## Context
Adaptive looping has become a promising way to extend inference depth for large language models while keeping compute efficient. This work demonstrates how memory‑aware recurrence can outperform static loop designs in reasoning tasks, filling a gap between parameter‑efficient methods and full‑parameter deepening.

## Implications
For practitioners, RecurTrace offers a framework that can be integrated into existing transformer backbones without architectural changes, enabling smarter use of limited compute. The ability to stop early on easy inputs while extending depth for hard ones could reduce latency and energy costs in real‑time applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03379v1)

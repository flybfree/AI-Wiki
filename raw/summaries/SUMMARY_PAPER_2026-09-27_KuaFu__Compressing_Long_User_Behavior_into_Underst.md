---
title: KuaFu: Compressing Long User Behavior into Understanding at Billion Scale
url: http://arxiv.org/abs/2609.31045v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-25_09-39-39Z_KuaFu_CompressingLongUserBehaviorintoUnderstanding.md
generated_at: 2026-09-27 21:21
model: qwen3.6-35b-a3b
---

## Summary
KuaFu presents a unified behavior-compression layer that condenses raw user interaction histories into compact token representations to overcome scalability bottlenecks in industrial personalization systems. By projecting each behavior item into 2-4 tokens with reduced width, the method achieves significant compression ratios while preserving fidelity through a specialized four-stage training regimen, ultimately matching or exceeding uncompressed baselines across production metrics and public benchmarks.

## Key Takeaways
- KuaFu addresses critical throughput constraints by compressing individual behavior items into 2-4 tokens of width 128-256, yielding approximately 10x compression along the token axis and 20x along width; this reduces per-item cache requirements from 10 KB to 0.5 KB, enabling massive efficiency gains without sacrificing profile quality.
- The framework mitigates silent degradation in compressed representations by implementing fidelity-oriented training with layered intermediate evaluation, specifically targeting four hallucination types: fabrication, omission, date misattribution, and broken logic that often emerge when truncating long user sequences.
- Real-world deployment on Tencent's advertising and recommendation platforms for ten months resulted in a 1.37% GMV lift, while production benchmarks show per-GPU throughput increases of 37%-350%, a saving of 190 GPUs, and performance that matches or surpasses uncompressed single-task models across all headline metrics.

## Context
Large-scale recommender systems and generative advertising face an inherent tension between the need for rich user context from extensive behavior histories and strict latency constraints imposed by fixed GPU budgets. As user profiles expand to tens of thousands of tokens, traditional truncation methods fail to preserve necessary semantic information, necessitating advanced compression techniques that can operate at billion-user scale while maintaining high-fidelity understanding for downstream tasks.

## Implications
The success of KuaFu demonstrates that unified compression layers can deliver substantial infrastructure savings and performance improvements simultaneously, allowing organizations to reallocate compute resources or

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.31045v1)

---
title: Selective Regenerative Decoding: Trajectory-Level Intervention for Inference-Time Reasoning
published: 2026-08-25T10:01:56Z
authors: Sophia Xiao Pu, Yumo Xu, Sailik Sengupta, Millennium Bismay, Ruixue Lian, James Gung, Yi-an Lai, Arshit Gupta
url: http://arxiv.org/abs/2608.24338v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Selective Regenerative Decoding: Trajectory-Level Intervention for Inference-Time Reasoning

## Abstract
Inference-time decoding methods improve LLM reasoning by exploring multiple candidate trajectories, yet treat each trajectory as atomic: either retaining it whole or discarding it irreversibly. This wastes computation on partially promising candidates whose high-quality prefixes are abandoned alongside degraded suffixes. We introduce Selective Regenerative Decoding (SRD), which routes each candidate to discard, keep, or refine only the degraded portion of the suffix while preserving the useful prefix of borderline candidates, without requiring a larger target model. Under mild assumptions, SRD achieves a provable 1.28-to-1.36-fold gain in sample efficiency over rejection sampling with strictly higher expected trajectory quality, with the gain growing as the candidate pool grows. Across MATH500, GPQA Diamond, HotpotQA, and AlpacaEval with multiple generation-reward model pairs, SRD matches Best-of-N accuracy with substantially fewer generated tokens and outperforms speculative rejection in low-compute regimes. By enabling segment-level intervention rather than whole-trajectory selection, SRD opens a previously underexplored region of the accuracy-compute tradeoff for inference-time reasoning.

## Metadata
- **Published**: 2026-08-25T10:01:56Z
- **Authors**: Sophia Xiao Pu, Yumo Xu, Sailik Sengupta, Millennium Bismay, Ruixue Lian, James Gung, Yi-an Lai, Arshit Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24338v1)
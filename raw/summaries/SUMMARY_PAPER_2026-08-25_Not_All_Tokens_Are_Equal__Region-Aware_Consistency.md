---
title: Not All Tokens Are Equal: Region-Aware Consistency Repair of Backdoors in MLLMs
url: http://arxiv.org/abs/2608.24354v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_10-10-01Z_NotAllTokensAreEqual_Region_AwareConsistencyRepair.md
generated_at: 2026-08-25 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces RACER, a model‑level repair framework for eliminating latent backdoors in multimodal language models (MLLMs). By exploiting the observation that backdoor triggers create modality‑dependent layer‑wise inconsistencies, RACER normalizes visual and textual token regions separately, recomposes them with adaptive weights, and uses min‑max optimization to suppress representational shifts. Experiments on three MLLMs across 36 backdoor settings achieve an average ASR of 1.1% (down to 0%) while preserving clean‑task performance.

## Key Takeaways
- RACER identifies a layer‑wise inconsistency anomaly that is concentrated in the token region encoding trigger features, distinguishing visual from textual triggers.
- The repair uses modality‑aware weights over a deep‑layer window to recombine normalized regions, achieving a region‑aware objective that targets only the backdoor‑induced shifts.
- RACER requires only 100 clean samples and no prior knowledge of the attack, making it practical for deployment without trigger detection.

## Context
MLLMs are widely used in user‑facing systems but inherit backdoor vulnerabilities from construction pipelines. Traditional defenses operate at inference time or rely on model‑level methods ineffective for multimodal triggers. This work bridges that gap by providing a source‑based repair that operates directly on the model’s internal representations.

## Implications
Practitioners can integrate RACER into training pipelines to safeguard deployed MLLMs against hidden backdoors, reducing risk without sacrificing performance. The method sets a new standard for model‑level backdoor removal in multimodal AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24354v1)

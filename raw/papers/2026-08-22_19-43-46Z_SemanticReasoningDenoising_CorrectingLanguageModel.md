---
title: Semantic Reasoning Denoising: Correcting Language Model Reasoning with Semantic Operators
published: 2026-08-22T19:43:46Z
authors: Yujiao Yang
url: http://arxiv.org/abs/2608.22090v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Semantic Reasoning Denoising: Correcting Language Model Reasoning with Semantic Operators

## Abstract
Large language models can produce fluent reasoning traces whose local semantic errors propagate to an incorrect conclusion, while unconstrained self-correction may preserve, amplify, or introduce errors. Existing diffusion language models provide iterative refinement, but usually define noise as token masking or replacement rather than as errors in the reasoning process. We present Semantic Reasoning Denoising (SRD), an operatorized Markov denoising method for natural-language reasoning trajectories. SRD represents semantic noise with executable error operators that describe the error type, its location, and the corrupted and repaired propositions. Composing these operators constructs progressively noisier states. During training, the model learns to identify the semantic noise active in the current trajectory and to reconstruct the paired adjacent lower-noise state. During inference, noise-level-aware denoising repeatedly predicts an inverse operator and checks whether it is applicable, so each executed update makes a localized move toward a stable trajectory. Across six in-domain benchmarks spanning mathematics, code, knowledge, and commonsense, SRD improves the strongest same backbone baseline by 3.2 points on average. On seven cross-dataset transfer targets, it remains competitive with Llama-3-8B-Instruct and improves the strongest Qwen3-8B baseline average by 2.9 points. Analyses of noise sources, objectives, and denoising depth further show that structured semantic-noise prediction and iterative operator execution are central to the improvement.

## Metadata
- **Published**: 2026-08-22T19:43:46Z
- **Authors**: Yujiao Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22090v1)
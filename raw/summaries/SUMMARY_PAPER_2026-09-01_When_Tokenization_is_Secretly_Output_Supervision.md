---
title: When Tokenization is Secretly Output Supervision
url: http://arxiv.org/abs/2609.01386v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-16-19Z_WhenTokenizationisSecretlyOutputSupervision.md
generated_at: 2026-09-01 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper argues that tokenization should be viewed as output supervision rather than merely an input preprocessing step. Experiments on numeric reasoning show that changing the tokenization of model outputs creates distinct training dynamics and performance differences that are largely independent of how inputs are tokenized. This reveals a hidden source of variation in model capabilities.

## Key Takeaways
- The granularity of output tokens directly shapes what the model must resolve during forward passes, influencing both task difficulty and internal representations.  
- Output tokenization can produce performance gaps that persist even when input tokenization is held constant, indicating it is a separate supervision regime.  
- Most recent CL papers on numeric reasoning compare models under different tokenizations without reporting this fact, leading to misleading comparisons.

## Context
Tokenization decisions are often treated as neutral preprocessing choices, but they affect the learning signal and model architecture. This paper provides a principled framework that explains why such differences matter in AI research and practice.

## Implications
Researchers may need to standardize tokenization practices when benchmarking models, otherwise results could reflect task definitions rather than true ability. Practitioners should be aware that tokenization can alter training dynamics, affecting real‑world deployment outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01386v1)

---
title: Unlearning Is Not Just Erasing: Temporal Decoupling via Generation Inequality
url: http://arxiv.org/abs/2608.23020v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_09-22-05Z_UnlearningIsNotJustErasing_TemporalDecouplingviaGe.md
generated_at: 2026-08-24 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ADU, a training‑based unlearning framework that decouples attention pathways instead of erasing tokens. It achieves high forget quality on TOFU while preserving model utility.

## Key Takeaways
- ADU shifts unlearning from token erasure to contextual attention‑pathway decoupling, identifying preplan positions that retrieve persistent sensitive anchors and fixing their candidate paths under the original model.
- The method trains attention‑projection adapters to suppress attention mass along these paths while preserving local‑attention structure and retain‑set language modeling.
- ADU attains a Forget Quality of 0.93 on TOFU, improves utility from 81.9% (baselines) to 92.9% average, and reduces side effects in benign contexts.

## Context
Unlearning is essential for privacy‑preserving AI as models must forget sensitive data without harming general performance. Current token‑level approaches often disrupt linguistic structure or suppress harmless knowledge, limiting applicability.

## Implications
Practitioners can adopt ADU to implement compliant model updates with minimal utility loss, supporting regulatory compliance and safer deployment of LLMs in real‑world settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23020v1)

---
title: Lost in Reordering: Structural Sensitivity of Multilingual LLMs under Semantics-Preserving Perturbations
url: http://arxiv.org/abs/2609.03511v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_08-10-43Z_LostinReordering_StructuralSensitivityofMultilingu.md
generated_at: 2026-09-03 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates structural sensitivity of multilingual LLMs under semantics-preserving perturbations in Hindi and Malayalam, introducing the IndicReStruct benchmark with two variants—GSM8K-Reordered and GSM8K-Voice—that retain original meaning. Across six state-of-the-art models and prompting strategies, it finds a consistent and significant drop in mathematical reasoning performance when surface syntax changes.

## Key Takeaways
- Reasoning scores fall noticeably even though the underlying math is unchanged because word order or voice form alters syntactic structure.
- The failures are traced to misalignment between entities and quantities, suggesting that semantic content alone cannot compensate for structural mismatches.
- Residual-stream patching shows that intermediate transformer layers are the primary sites where reasoning can be restored, indicating their importance in compositional processing.

## Context
This work extends prior research on LLM robustness to include multilingual and syntactic variation, highlighting a gap in current evaluation frameworks. It underscores that standard benchmarks often ignore surface changes that do not affect meaning but still impact performance.

## Implications
For practitioners, it calls for designing models that are invariant to surface syntactic changes or incorporating architectural mechanisms to preserve reasoning under such perturbations. In industry, this could affect deployment of LLMs where input formats vary across languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03511v1)

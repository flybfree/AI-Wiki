---
title: EliSeg: Verified Target Construction for Report-Grounded Abnormality Segmentation
url: http://arxiv.org/abs/2608.07299v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_14-52-35Z_EliSeg_VerifiedTargetConstructionforReport_Grounde.md
generated_at: 2026-08-09 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces EliSeg, a method that constructs segmentation targets directly from radiology reports without prior prompts. The approach combines an actor that proposes target slots and masks with a verifier that checks eligibility and a revision module that resolves conflicts. Experiments on MIMIC-CXR-ILS show EliSeg outperforms existing methods while suppressing invalid masks.

## Key Takeaways
- EliSeg builds target eligibility, cardinality, and finding-to-mask mapping directly from unfiltered reports.
- The framework uses a grammar‑constrained actor for proposal and an independent verifier to reconstruct eligible findings.
- Revision selectively reexecutes the actor when verification and actor outputs disagree.

## Context
Radiology report analysis requires models to interpret natural language into spatial masks, yet current systems rely on external target cues. This work addresses that gap by embedding target construction within a single model pipeline.

## Implications
The method enables automated segmentation from free‑form reports, reducing reliance on manual annotation and supporting scalable clinical AI tools. It also demonstrates transferable design for other medical imaging tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07299v1)

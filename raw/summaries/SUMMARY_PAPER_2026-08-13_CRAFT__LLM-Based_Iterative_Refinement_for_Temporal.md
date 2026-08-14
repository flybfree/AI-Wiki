---
title: CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical Narratives
url: http://arxiv.org/abs/2608.12779v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_03-37-11Z_CRAFT_LLM_BasedIterativeRefinementforTemporalReaso.md
generated_at: 2026-08-13 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CRAFT, an LLM framework that generates and refines symptom timelines using a generator paired with a constraint‑based verifier for clinical narratives lacking explicit temporal anchors. Experiments on MedTempo show improved ordering accuracy across four LLM backbones. The iterative refinement leverages feedback to correct ordering errors, producing a coherent symptom timeline.

## Key Takeaways
- The framework pairs a generator with a constraint‑based verifier to iteratively produce stage‑wise symptom timelines from anchor‑sparse reports.
- Evaluation on 5,347 vaccine adverse‑event narratives shows consistent improvement in temporal ordering accuracy across four LLM models.
- Ablation analysis isolates the contribution of each component (generator and verifier) at different model capability levels.

## Context
Current AI systems for clinical narrative processing often rely on paired timestamps or multi‑visit records, which are scarce in single‑report adverse events. Temporal reasoning remains a bottleneck for disease monitoring. This work addresses the gap between unstructured narrative input and structured temporal output.

## Implications
Accurate symptom trajectory reconstruction can enhance vaccine safety surveillance and early detection of adverse events. Practitioners can integrate CRAFT into clinical decision support systems to prioritize follow‑up actions based on symptom progression.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12779v1)

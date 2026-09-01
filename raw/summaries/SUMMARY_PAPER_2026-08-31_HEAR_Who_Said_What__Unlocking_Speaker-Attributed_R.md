---
title: HEAR Who Said What: Unlocking Speaker-Attributed Reasoning via Counterfactual Voice Grounding
url: http://arxiv.org/abs/2608.29120v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_08-01-20Z_HEARWhoSaidWhat_UnlockingSpeaker_AttributedReasoni.md
generated_at: 2026-08-31 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HEAR, a benchmark to test speaker-attributed reasoning in speech language models, and presents A2R, a large model fine‑tuned on Counterfactual Audio with Speaker-level Hard negatives (CASH). On HEAR, A2R outperforms other models by grounding attributions on acoustic cues rather than linguistic priors. The results show that learned speaker attribution can unlock zero‑shot reasoning across diverse multi‑speaker tasks.

## Key Takeaways
- HEAR provides 2.4K human‑verified samples from 887 audio clips to diagnose foundational capabilities of speaker‑attributed reasoning.
- A2R, a 30B model trained on CASH, achieves strong performance on HEAR and generalizes zero‑shot to downstream tasks.
- The study demonstrates that focusing attention on acoustic vocal cues rather than semantic priors improves attribution and reasoning.

## Context
Current speech language models often fail to attribute utterances correctly because they rely heavily on word meanings instead of speaker identity. This limits their usefulness in collaborative or multi‑speaker settings where clear speaker roles are essential. Understanding these limitations is crucial for developing more reliable conversational agents.

## Implications
For researchers, HEAR offers a standardized way to evaluate and improve speaker attribution models. For industry practitioners, the findings suggest that investing in acoustic cue grounding can lead to better performing assistants in real‑world multi‑speaker environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29120v1)

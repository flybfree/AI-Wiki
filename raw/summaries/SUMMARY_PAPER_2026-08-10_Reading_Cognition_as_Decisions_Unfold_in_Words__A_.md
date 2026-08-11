---
title: Reading Cognition as Decisions Unfold in Words: A Factorized Inverse Decision Model
url: http://arxiv.org/abs/2608.09222v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_07-46-13Z_ReadingCognitionasDecisionsUnfoldinWords_AFactoriz.md
generated_at: 2026-08-10 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a factorized inverse decision model (FIDM) that separates task execution from action in verbal cognitive tasks by modeling effort and action as independent factors. On data from 400 older adults performing a grocery‑shopping dialog, the model recovers selective estimates of these factors while preserving distinctions between actions and execution traces.

## Key Takeaways
- The FIDM decomposes each participant’s likelihood into an action factor and an effort factor, each with its own individual parameters, allowing separate inference from raw verbal transcripts.  
- Controlled recovery demonstrates that the model can estimate intended factors accurately, whereas semi‑synthetic conditions reveal it maintains clear separation between action and execution even when behavioral summaries are matched.  
- Action evidence is used to localize task‑defined deviations across participants, providing granular insights beyond aggregated behavior.

## Context
This work advances inverse decision modeling in natural language processing by integrating linguistic output into probabilistic inference pipelines. It demonstrates how latent cognitive factors can be extracted from conversational data, a capability that complements existing trajectory‑based approaches and frozen language representations.

## Implications
For AI researchers, FIDM offers a framework to interpret verbal behavior as a blend of intentional actions and effortful processing, improving diagnostic tools for cognitive screening. Clinicians could leverage these refined factors to personalize interventions, while industry practitioners may use the model to refine conversational agents that adapt to individual effort levels.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09222v1)

---
title: VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of Large Language Model Outputs
url: http://arxiv.org/abs/2608.03810v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_15-22-23Z_VIBE_AVAD_InformedBenchmarkforEntity_CenteredAffec.md
generated_at: 2026-08-05 01:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes VIBE, a benchmark that evaluates how large language models assign affective valence, arousal, and dominance to specific entities within their outputs. The study demonstrates that these dimensions are distinct, that whole‑response VAD differs from target‑directed VAD, and that reporting protocols affect the measured profiles.

## Key Takeaways
- Scalar favorability is validated by high inter‑judge agreement (rV = 0.944) yet does not fully capture arousal or dominance, which show lower correlation with human judgments (rA = 0.495, rD = 0.702).  
- The same textual response can produce a single overall affective tone while assigning different VAD values to the named target, showing that whole‑response and target‑directed profiles are separate contracts.  
- Elicitation conditions shift affective scores, indicating that context metadata is essential for reliable interpretation of any profile.

## Context
Entity‑centered affective profiling has remained undocumented in LLM evaluation, leaving practitioners without a standardized way to report how models frame social targets. This work fills the gap by introducing a clear measurement contract and an Affective Passport format, aligning with broader efforts toward transparent AI assessment.

## Implications
For researchers, VIBE provides a reproducible benchmark that can guide model development and fairness analysis of affective language generation. For industry users, adopting such profiles ensures consistent interpretation across teams and reduces miscommunication in applications where target‑directed sentiment matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03810v1)

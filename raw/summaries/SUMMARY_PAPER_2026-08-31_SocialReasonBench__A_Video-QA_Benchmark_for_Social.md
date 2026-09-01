---
title: SocialReasonBench: A Video-QA Benchmark for Social Reasoning with Counterfactual Narrative Videos
url: http://arxiv.org/abs/2608.30716v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_12-55-52Z_SocialReasonBench_AVideo_QABenchmarkforSocialReaso.md
generated_at: 2026-08-31 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
SocialReasonBench introduces a video multiple‑choice QA benchmark that tests large multimodal models on socially grounded reasoning extracted from branching narrative games. Experiments show that while models grasp basic social cues, they falter in counterfactual and causal reasoning tasks, indicating a gap between surface event recognition and deeper understanding of latent social states.

## Key Takeaways
- The benchmark uses Detroit: Become Human gameplay videos with branching storylines to create theory‑driven questions whose answers are verified against the game’s script and flowchart.  
- Models often rely on incomplete modality cues, leading to visual shortcuts that mask a lack of true social reasoning.  
- Seven reasoning dimensions—including intent recognition, emotional empathy, moral dilemma, counterfactual reasoning, and causal antecedent—are evaluated, revealing uneven performance across them.

## Context
Recent advances in large multimodal models have boosted video comprehension but rarely assess higher‑order human‑centered reasoning. Existing benchmarks focus on single trajectories, obscuring whether models truly model social dynamics or merely pattern match. SocialReasonBench addresses this by grounding questions on interactive narratives where player choices produce alternative outcomes.

## Implications
The findings highlight a critical limitation in current LMM evaluations: surface detection does not equate to deep social understanding. For industry practitioners, this underscores the need for benchmarks that probe counterfactual and causal reasoning to guide more robust model development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30716v1)

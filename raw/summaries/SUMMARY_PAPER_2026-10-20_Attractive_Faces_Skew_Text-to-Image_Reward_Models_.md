---
title: Attractive Faces Skew Text-to-Image Reward Models and Leaderboards
url: http://arxiv.org/abs/2610.28195v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_13-35-34Z_AttractiveFacesSkewText_to_ImageRewardModelsandLea.md
generated_at: 2026-10-20 22:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how human preference judgments for text-to-image models are systematically biased by facial attractiveness, independent of actual image quality. Through controlled user studies and analysis of five major human preference models, the authors demonstrate that perceived attractiveness overrides fidelity in ranking decisions, distorting leaderboards and reward model scores. They further show that preference-aligned generation shifts outputs toward younger, more feminine faces, limiting user control over generated content.

## Key Takeaways
- In a controlled user study, annotators consistently ranked more attractive faces as higher quality, even when comparing unattractive real photographs against attractive AI-generated images of identical fidelity. Simulating Elo rankings from this data demonstrated that attractiveness can invert a leaderboard's ordering, elevating synthetic attractive faces above real, unattractive ones, thereby corrupting model evaluation benchmarks.
- Editing 40 annotated facial attributes in isolation revealed that attractiveness is the strongest correlate of score for four out of five human preference models tested (PickScore, MPS, HPSv2.1, HPSv3), and the strongest predictor in regression analysis. This means these reward models, which are widely used for finetuning and ranking text-to-image generators, encode a cognitive bias rather than a genuine quality signal.
- Preference-aligned generation systematically shifts faces toward younger and more feminine appearances, and can override explicit user prompts requesting unattractive faces. This limits user control and introduces a homogenizing effect on generated outputs. The authors also explore mitigation strategies for both data collection and post-training adjustments to human preference models.

## Context
Human preference models have become the dominant mechanism for evaluating, guiding, and finetuning text-to-image generation systems, with tools like PickScore and HPSv3 serving as de facto standards in the field. This paper matters because it exposes a fundamental vulnerability in that evaluation pipeline: the preference signals these models learn are contaminated by a well-documented human cognitive bias toward facial attractiveness. As text-to-image models increasingly rely on preference-based optimization for training and benchmarking, any systematic bias in the reward signal propagates directly into model behavior and public leaderboards, undermining the reliability of comparisons across models.

## Implications
For practitioners building or deploying text-to-image systems, this work signals that current leaderboards and reward-model-based evaluations may be misleading, rewarding models that produce conventionally attractive faces rather than those with superior technical fidelity. Industry teams relying on preference models for finetuning should audit their training data for attractiveness bias and consider disentangling quality signals from cognitive preferences. The findings also carry implications for fairness and representation in generative AI, since preference-aligned generation systematically biases outputs toward specific demographic profiles, potentially marginalizing diverse user needs and limiting creative control.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28195v1)

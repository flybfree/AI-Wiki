---
title: From Memorization to Absorption: Mixed-Policy RL for Continual Knowledge Injection
url: http://arxiv.org/abs/2608.25243v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_00-04-46Z_FromMemorizationtoAbsorption_Mixed_PolicyRLforCont.md
generated_at: 2026-08-26 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Golden-GRPO Injection (GRIN), a mixed-policy reinforcement learning framework for continual knowledge injection that learns from a golden answer even when on‑policy rollouts fail. Experiments show GRIN outperforms supervised fine‑tuning and other RL baselines, especially on complex question types while matching them on simple recall.

## Key Takeaways
- Mixed‑policy reinforcement learning provides a learning signal through a golden answer, enabling knowledge absorption beyond what supervised fine‑tuning can achieve.
- The framework includes two benchmarks—Blank for novel acquisition and Counter for counterfactual overwrite—evaluating single‑fact recall, multi‑source retrieval, and inferential reasoning.
- GRIN matches or exceeds mixed‑policy RL baselines on basic fact recall while significantly improving performance on harder question types.

## Context
Continual learning in large language models faces challenges of preserving prior knowledge while adapting to new information. Existing supervised fine‑tuning methods often memorize facts without generalizing across paraphrases, document combinations, or reasoning tasks. This work addresses those limitations by leveraging reinforcement learning principles that prioritize understanding over rote memorization.

## Implications
For industry practitioners, GRIN offers a practical path to keep models up‑to‑date with minimal data and low risk of catastrophic forgetting. The mixed‑policy approach could be integrated into automated pipelines for real‑time knowledge updates, enhancing model reliability in dynamic environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25243v1)

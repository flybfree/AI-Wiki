---
title: SWE-Critix: Post-Training Generalist Verifiers for Assessing Coding-Agent Trajectories
url: http://arxiv.org/abs/2610.13356v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_10-30-21Z_SWE_Critix_Post_TrainingGeneralistVerifiersforAsse.md
generated_at: 2026-10-11 20:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SWE-Critix introduces a post-training pipeline that combines supervised fine-tuning (SFT) and reinforcement learning (RL) to train generalist verifiers capable of assessing coding-agent execution trajectories. The resulting 30B models predict completion labels and generate natural-language explanations of their judgments, improving classification accuracy from 57% to 78% on a held-out test set derived from CodeForge-Preview trajectories.

## Key Takeaways
- The paper addresses a critical gap in coding-agent evaluation: existing verifiers either rely on untrained general-purpose LLMs or produce only scalar rewards, leaving the training-based generalist verification approach largely unexplored. SWE-Critix fills this gap by training dedicated verifiers that both classify trajectory success and produce interpretable natural-language analyses.
- The training pipeline is a two-stage process: first supervised fine-tuning on CodeForge-Preview trajectories, then reinforcement learning to further refine judgment quality. This sequential approach yields progressive gains, moving accuracy from 57% (base Qwen3-30B-A3B) to 66% after SFT and ultimately 78% after RL, demonstrating that structured post-training substantially outperforms zero-shot or prompt-based verification.
- The models are trained on trajectories containing hundreds of iterative interactions with code repositories and external tools, meaning the verifiers must handle extremely long, complex execution sequences rather than simple single-step outputs. The authors release their models, datasets, and training code to enable reproducibility and further research in this area.

## Context
As coding agents increasingly handle long-horizon software engineering tasks end-to-end, the absence of a readily available oracle evaluator makes reliable, explainable verification essential for safe deployment. This paper sits at the intersection of agent evaluation, post-training methodology, and interpretability, pushing beyond the dominant paradigm of scalar reward modeling toward verifiers that can articulate why a trajectory succeeded or failed. It represents a meaningful step toward making autonomous coding agents auditable without human-in-the-loop inspection of every interaction.

## Implications
For practitioners deploying coding agents in production software pipelines, SWE-Critix offers a path toward automated quality gates that can flag failed or risky trajectories before code is merged, reducing reliance on manual code review. For the broader AI research community, the released models, datasets, and training code provide a reproducible benchmark for generalist verification, encouraging further work on scaling verifier training to more complex agent architectures and longer execution horizons. The natural-language explanation component also opens possibilities for debugging agent failures and building trust in autonomous software engineering systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13356v1)

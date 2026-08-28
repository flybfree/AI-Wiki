---
title: Sycophancy Suppression Can Impair Rational Updating: Anti-Sycophancy Should Preserve the Ability to Update
published: 2026-08-27T01:20:03Z
authors: Huanhuan Ma, Henry Peng Zou, Chengze Li, Enze Ma, Yunyue Su, Philip S. Yu
url: http://arxiv.org/abs/2608.26511v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sycophancy Suppression Can Impair Rational Updating: Anti-Sycophancy Should Preserve the Ability to Update

## Abstract
Large language models often exhibit sycophancy, revising their answers to align with users when users push back. Such answer flips, however, can arise from different causes. One possibility is that the model simply aligns with the user's feedback in order to satisfy them. Another is that the feedback genuinely contains useful evidence, prompting the model to update its answer in a rational way. We distinguish them as Unsupported-Yielding and Rational-Updating. Prior work focuses primarily on suppressing Unsupported-Yielding, while overlooking its effect on Rational-Updating. We address this gap with a two-turn evaluation framework that measures the two behaviors separately. Across representative training-time and inference-time interventions, we find that anti-sycophancy methods often encounter a trade-off in which reducing Unsupported-Yielding can sacrifice Rational-Updating, and vice versa, even when the two objectives are optimized jointly. Mechanistic analysis suggests that the two behaviors share an internal substrate: the MLP neurons and attention heads driving them overlap substantially, and their associated steering directions are positively aligned. We further conduct a preliminary orthogonalized steering exploration, which yields modest, backbone-dependent selectivity gains. Overall, our results suggest that anti-sycophancy should be treated not as a simple suppression problem, but as a selectivity problem, where effective interventions should preserve Rational-Updating while reducing Unsupported-Yielding.

## Metadata
- **Published**: 2026-08-27T01:20:03Z
- **Authors**: Huanhuan Ma, Henry Peng Zou, Chengze Li, Enze Ma, Yunyue Su, Philip S. Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26511v1)
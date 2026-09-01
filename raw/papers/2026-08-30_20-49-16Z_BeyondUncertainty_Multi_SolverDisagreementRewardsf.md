---
title: Beyond Uncertainty: Multi-Solver Disagreement Rewards for Self-Evolving Reasoning Curricula
published: 2026-08-30T20:49:16Z
authors: Vinoth Selvendran, Zhanming Zhang
url: http://arxiv.org/abs/2608.30035v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Uncertainty: Multi-Solver Disagreement Rewards for Self-Evolving Reasoning Curricula

## Abstract
Self-evolving reasoning frameworks train a Challenger to generate questions exposing a Solver's weaknesses, creating adaptive curricula without human data. However, existing approaches use a single solver's sampling uncertainty as the Challenger's reward. This creates a fundamental bottleneck: as the solver grows confident on the Challenger's question distribution, all sampled answers converge identically, collapsing the reward to zero and starving the Challenger of learning signal. Critically, this single-model reward cannot distinguish genuinely easy questions from those that merely align with one solver's learned biases. We propose a multi-solver disagreement reward using a heterogeneous ensemble varying in model capacity and sampling temperature. A normalized Shannon entropy over the ensemble's per-question plurality answers explicitly rewards questions where solvers produce conflicting solutions---capturing difficulty as inter-model divergence rather than intra-model sampling variance. This richer gradient enables the Challenger to discover questions targeting true capability boundaries, producing a curriculum that forces downstream Solvers to develop robust reasoning strategies generalizing across problem types. Our approach is a drop-in reward function replacement requiring no framework modifications or additional data. Experiments with Qwen3-4B show that Solvers trained on disagreement-Challenger questions achieve +1.34 points average improvement on competition-math benchmarks (MATH-500, AMC, Olympiad), suggesting that multi-solver disagreement provides a complementary and scalable signal for curriculum generation in self-play reasoning systems.

## Metadata
- **Published**: 2026-08-30T20:49:16Z
- **Authors**: Vinoth Selvendran, Zhanming Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30035v1)
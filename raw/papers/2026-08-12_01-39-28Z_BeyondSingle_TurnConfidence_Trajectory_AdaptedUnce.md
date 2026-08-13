---
title: Beyond Single-Turn Confidence: Trajectory-Adapted Uncertainty Quantification for LLM Agents
published: 2026-08-12T01:39:28Z
authors: Dylan Bouchard, Mohit Singh Chauhan
url: http://arxiv.org/abs/2608.11552v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Single-Turn Confidence: Trajectory-Adapted Uncertainty Quantification for LLM Agents

## Abstract
Uncertainty quantification (UQ) methods for language models are typically evaluated on single-turn outputs, where uncertainty is attached to one generated answer. For LLM agents, however, the unit of observation is an interactive trajectory, where the model can ask clarifying questions, call tools, update state, and make intermediate decisions whose errors propagate to the final outcome. We study whether three common families of single-turn UQ methods transfer to this setting. Across five LLMs and four multi-turn tool-use datasets from BFCL-v4 and $τ^2$-bench, we evaluate white-box scorers based on action-token probabilities, black-box consistency scorers based on resampled trajectories, and reflexive scorers based on model self-assessment of the trajectory. We find that transfer is often useful but uneven. Token-probability scores are highly sensitive to the choice of aggregator used across turns, reflexive scores provide the strongest low-cost baseline in most evaluated settings, and black-box self-consistency is often the strongest UQ family, with trajectory-equivalence and action-set consistency typically ranking highest among its variants. These results suggest that UQ methods developed for single generations should be revalidated at the trajectory level, with careful attention to the consistency measurement, aggregator choice, and computational budget.

## Metadata
- **Published**: 2026-08-12T01:39:28Z
- **Authors**: Dylan Bouchard, Mohit Singh Chauhan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11552v1)
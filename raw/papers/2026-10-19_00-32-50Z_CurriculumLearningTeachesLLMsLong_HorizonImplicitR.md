---
title: Curriculum Learning Teaches LLMs Long-Horizon Implicit Reasoning, Up To A Limit
published: 2026-10-19T00:32:50Z
authors: Jimson Huang, Maxwell Nickell, Ruowang Zhang, Abulhair Saparov
url: http://arxiv.org/abs/2610.25612v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Curriculum Learning Teaches LLMs Long-Horizon Implicit Reasoning, Up To A Limit

## Abstract
LLMs "reason" by externalizing intermediate steps as tokens through chain-of-thought (CoT), yet even frontier reasoning models hit abrupt performance cliffs on long-horizon tasks. Implicit reasoning (reasoning within a single forward pass) is useful during CoT generation, as the model can "search ahead" to decide the correct next move without explicit search. Models with weak implicit reasoning are more likely to commit to wrong paths and must attempt to recover via backtracking, while models with strong implicit reasoning identify the correct proof strategy directly, shortening the CoT. However, prior work shows LLMs struggle to reason implicitly beyond shallow depths, with no relief from scale. We investigate whether curriculum learning can extend this depth by fine-tuning on examples with progressively increasing vocabulary size and lookahead (the number of steps a model must search ahead to identify the correct next move). At matched compute, curriculum-trained models achieve lookaheads where no-curriculum training fails. Qwen3-0.6B reaches 98% accuracy on problems with lookahead up to 256 with curriculum, compared to 45% without. However, progress slows as fine-tuning continues, following a saturating exponential that suggests a maximum intrinsic lookahead to which models can learn to reason implicitly. Larger models reach higher fitted ceilings, fine-tuning pretrained models far outpaces training from scratch, and curriculum step sizes that are too large stall progression. Finally, the capability acquired on synthetic data transfers to natural language reasoning, with curriculum-trained models outperforming models trained without curriculum at matched compute on 11 natural language reasoning benchmarks.

## Metadata
- **Published**: 2026-10-19T00:32:50Z
- **Authors**: Jimson Huang, Maxwell Nickell, Ruowang Zhang, Abulhair Saparov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25612v1)
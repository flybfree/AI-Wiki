---
title: Learning to Accumulate Knowledge with Mutual Information
url: http://arxiv.org/abs/2610.10042v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_13-20-18Z_LearningtoAccumulateKnowledgewithMutualInformation.md
generated_at: 2026-10-07 22:21
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Knowledge Weaver, a reinforcement learning framework that trains a language model to curate reusable knowledge entries from agent trajectories by coupling token-wise mutual information feedback with marginal success rewards. The approach addresses the challenge of building knowledge banks that grow more useful over time by penalizing redundant overlap and rewarding entries that contribute beyond what the bank already contains. On ALFWorld and WebShop benchmarks, Knowledge Weaver outperforms GRPO-trained baselines by 16.9 and 18.7 percentage points respectively, and its learned knowledge banks surpass human-written and prompt-based banks when the executor model is frozen.

## Key Takeaways
- Standard GRPO training on standalone task success can inadvertently reinforce generic guidance that duplicates existing knowledge entries, failing to ensure that new additions genuinely expand the bank's utility. Knowledge Weaver resolves this by introducing mutual information–inspired feedback that penalizes token-level redundancy across entries, forcing the curator to preserve distinct information from each experience rather than restating what is already stored.
- The framework combines two complementary reward signals: marginal success rewards (measuring whether a new entry improves performance when added to the existing bank) and standalone success rewards (measuring whether an entry is useful in isolation). This dual objective ensures entries are both individually valuable and collectively non-redundant, producing knowledge banks that compound in usefulness as they grow.
- Empirically, with k=10 retrieved entries, Knowledge Weaver achieves 54.0% mean success on ALFWorld and 42.0% on WebShop, substantially exceeding GRPO baselines. Critically, the learned banks also outperform human-curated and prompt-based knowledge banks in overall success rate and score, demonstrating that the RL-trained curator discovers more effective knowledge organization than manual curation.

## Context
LLM agents increasingly rely on external memory or knowledge banks to improve performance across sequential tasks, yet the curation of these banks has largely been handled by hand-designed prompts or heuristic retrieval rules. This paper sits at the intersection of reinforcement learning for language models and lifelong agent learning, addressing a fundamental open problem: how to train a model to decide what is worth remembering and how to phrase it so that accumulated knowledge compounds rather than merely accumulates. By formalizing redundancy through mutual information and marginal utility through success deltas, the work provides a principled training signal that prior GRPO-based approaches lacked.

## Implications
For practitioners building agentic systems, Knowledge Weaver offers a concrete recipe for automating knowledge bank construction, reducing the labor-intensive curation currently required and yielding banks that generalize better across task distributions. For the broader field, the mutual-information-based penalty on redundancy suggests a general principle for any system that incrementally distills experience into reusable representations, from retrieval-augmented generation pipelines to continual learning architectures, indicating that explicit anti-redundancy objectives are essential for scalable, compounding knowledge accumulation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10042v1)

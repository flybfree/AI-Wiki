---
title: NTDH: Complex Reasoning for Comprehensive Affective Analysis
published: 2026-08-05T18:59:43Z
authors: Tianlei Zhu, Zhiwei Liu, Yuyan Wang, Xiao-Yang Liu, Sophia Ananiadou
url: http://arxiv.org/abs/2608.06425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NTDH: Complex Reasoning for Comprehensive Affective Analysis

## Abstract
Comprehensive affective analysis is challenging for two reasons: it spans heterogeneous prediction tasks with continuous, ordinal, and multi-label outputs, and affective meaning is context-dependent, requiring conflicting cues to be reconciled rather than mapped directly to labels. Existing methods learn this mapping directly and do not model the reconciliation explicitly. We recast the task as a complex-reasoning problem, which yields one output interface across heterogeneous label spaces and a trajectory over which a verifiable reward can be optimised; to our knowledge, this is the first such treatment covering both sentiment and emotion. The obstacle is on the data side: affective reasoning traces must be synthesised, and generic synthesis is misaligned with the targets, tolerances, and phenomena of affect, and discards or leaks its failure cases. We propose NTDH, which addresses these four failures. Naturalisation sets the training answer to the gold label, so it is correct by construction. A Tolerance-aware gate checks each answer against the task's own scoring margin. Domain-aware strategies refine the reasoning using ideas from affective science. Directional Hints report only the type and direction of an error, without exposing the target. We train Qwen3-8B with SFT and then GRPO under the same tolerance used for verification (up to a more permissive construction gate on the multi-label subtask), and a component ablation quantifies the data-quality effect of each part. Using 16,302 training records, about 14x fewer than comparable instruction-tuned systems, the final policy improves over its SFT checkpoint on five of six official-test metrics and achieves the strongest EI-reg result among the compared systems, at a Pearson correlation of 0.862.

## Metadata
- **Published**: 2026-08-05T18:59:43Z
- **Authors**: Tianlei Zhu, Zhiwei Liu, Yuyan Wang, Xiao-Yang Liu, Sophia Ananiadou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06425v1)
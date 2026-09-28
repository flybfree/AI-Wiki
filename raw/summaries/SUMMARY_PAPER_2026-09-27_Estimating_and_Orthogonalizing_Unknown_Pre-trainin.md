---
title: Estimating and Orthogonalizing Unknown Pre-training Gradients for Continual Fine-tuning of Large Language Models
url: http://arxiv.org/abs/2609.30935v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-25_07-52-37Z_EstimatingandOrthogonalizingUnknownPre_trainingGra.md
generated_at: 2026-09-27 21:23
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces EoupCT, a novel framework designed to mitigate catastrophic forgetting during the continual fine-tuning of large language models by estimating and orthogonalizing unknown pre-training gradients. By dynamically generating pseudo-data through learnable soft prompts equipped with Gumbel-Softmax relaxation, EoupCT approximates the elusive pre-training gradients and enforces orthogonality between new task updates and these estimates via a first-order efficient Pareto optimizer. Extensive experiments demonstrate that this approach successfully preserves both task-specific proficiency and the model's inherent general-purpose knowledge, addressing a critical gap in existing continual learning methods.

## Key Takeaways
- Existing orthogonal gradient projection methods fail to preserve general-purpose knowledge because they rely on original pre-training data and gradients that are strictly unknown and highly diverse; EoupCT bridges this gap by estimating these unknown gradients rather than requiring access to the original training distribution.
- The framework utilizes a learnable soft prompt with Gumbel-Softmax relaxation to dynamically generate pseudo-data that is most susceptible to forgetting for new tasks, allowing the model to approximate pre-training gradients effectively without direct access to source data.
- EoupCT formulates a multi-objective optimization problem solved by a first-order efficient Pareto optimizer that jointly updates LLM parameters and soft prompts, rigorously enforcing

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.30935v1)

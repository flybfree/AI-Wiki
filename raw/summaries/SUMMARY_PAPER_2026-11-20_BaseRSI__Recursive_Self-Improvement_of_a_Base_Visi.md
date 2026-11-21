---
title: BaseRSI: Recursive Self-Improvement of a Base Vision-Language Model via Training-Free Harness Internalization
url: http://arxiv.org/abs/2611.24578v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-18_15-10-11Z_BaseRSI_RecursiveSelf_ImprovementofaBaseVision_Lan.md
generated_at: 2026-11-20 21:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
BaseRSI introduces a new paradigm called Recursive Harness Internalization, in which a base vision-language model iteratively improves its own external harness (prompts, tools, scaffolding) and then writes the harness's contributions directly into its own weights through training-free edits, repeating this cycle on its own outputs. The method is supported by two novel mechanisms—ReGap, which supervises every transformer block using the high-dimensional activation difference the harness induces at that specific block, and ReKey, which encodes that signal into a small set of key-value neurons via regression while measuring each edit's site and strength on the model's own responses. Experiments across ten visual reasoning benchmarks demonstrate consistent improvements both in-distribution and on held-out benchmarks.

## Key Takeaways
- BaseRSI addresses three core limitations of existing recursive self-improvement (RSI) approaches: gains that remain trapped in the external harness rather than being absorbed into the base model, supervision that is limited to black-box output inspection, and edits whose location and magnitude are predetermined rather than measured from the model's own behavior. By internalizing the harness into the model's weights, the method ensures that each round of improvement compounds inside the model itself.
- ReGap provides block-level supervision by computing the activation difference that the harness produces at each individual transformer block, then updating that block's weights along this signal within a low-dimensional subspace. ReKey operationalizes this by regressing the signal into a few key-value neurons per block and empirically measuring the precise site and strength of each edit on the model's own generated responses, eliminating the need for fixed, pre-specified edit parameters.
- The entire recursive loop is executed using forward passes alone, requiring no gradient-based training or fine-tuning. Edits written at different sites compose additively within a single checkpoint without any refitting step, making the process computationally lightweight and compatible with existing inference infrastructure.

## Context
Recursive self-improvement has been a long-standing aspiration in AI research, but prior work has largely confined improvements to scaffolding around a frozen base model—prompt engineering, tool use, and external verification loops—leaving the model's internal representations unchanged. BaseRSI represents a conceptual shift by treating the harness as a temporary scaffold whose knowledge is distilled back into the model's weights through targeted, training-free weight edits. This bridges the gap between in-context learning gains and permanent model improvement, a problem that has limited the scalability of self-improving systems in both language and vision-language domains.

## Implications
For practitioners deploying vision-language models in production, BaseRSI offers a path to iterative capability enhancement without the cost and complexity of full fine-tuning or reinforcement learning from human feedback, potentially enabling continuous model improvement on edge or resource-constrained deployments. For the broader AI research community, the block-level activation-difference supervision (ReGap) and the regression-into-key-value-neurons strategy (ReKey) suggest a general recipe for internalizing external scaffolding into model weights that could extend beyond vision-language tasks to language models, multimodal agents, and autonomous self-improving systems, raising important questions about edit compositionality, safety of self-modifying models, and the long-term stability of recursively edited checkpoints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.24578v1)

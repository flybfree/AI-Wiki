---
title: SocialReasonBench: A Video-QA Benchmark for Social Reasoning with Counterfactual Narrative Videos
published: 2026-08-31T12:55:52Z
authors: Zheyu Huang, Zijing Shi, Haozhe Luo, Huadong Tang, Mingyu Liu, Meng Fang, Ling Chen
url: http://arxiv.org/abs/2608.30716v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SocialReasonBench: A Video-QA Benchmark for Social Reasoning with Counterfactual Narrative Videos

## Abstract
Recent advances in Large Multimodal Models (LMMs) have greatly improved video understanding, yet their ability to reason about human-centered social situations remains limited. Existing benchmarks typically rely on videos with a single observed trajectory, making it difficult to determine whether models truly understand social dynamics or merely exploit recurring narrative patterns. We introduce SocialReasonBench, a video multiple-choice QA benchmark for evaluating socially grounded reasoning in scenarios derived from interactive narratives. Built from gameplay videos of Detroit: Become Human, the benchmark leverages branching storylines where player decisions lead to alternative social outcomes that can be checked against the game's own script, flowchart, and recorded branches. We develop a multi-agent curation pipeline that localizes socially meaningful clips, grounds answer labels in game-state signals, and generates theory-guided questions with diagnostic distractors. SocialReasonBench covers seven reasoning dimensions, including intent recognition, emotional empathy, moral dilemma, counterfactual reasoning, and causal antecedent. Experiments on contemporary LMMs show that models perform reasonably well on basic social understanding but struggle with counterfactual and causal reasoning. Further ablation and diagnostic error analyses reveal that models often depend on incomplete modality cues and fall into reasoning traps such as visual shortcuts, highlighting a gap between observable event recognition and deeper reasoning over latent social states.

## Metadata
- **Published**: 2026-08-31T12:55:52Z
- **Authors**: Zheyu Huang, Zijing Shi, Haozhe Luo, Huadong Tang, Mingyu Liu, Meng Fang, Ling Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30716v1)
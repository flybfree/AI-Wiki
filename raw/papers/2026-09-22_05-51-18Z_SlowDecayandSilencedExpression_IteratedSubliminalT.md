---
title: Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages
published: 2026-09-22T05:51:18Z
authors: Ryan Vo, Duc-Vu Nguyen, Matt Kretchmar, Ngan Luu-Thuy Nguyen
url: http://arxiv.org/abs/2609.25721v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages

## Abstract
Language models are increasingly trained on the outputs of other models, forming chains that we call lineages, in which a trait present in one generation can pass to the next. Prior work on subliminal learning has shown that a teacher's trait can transmit to a student through filtered data carrying none of the trait's content. However, the evidence covers only a single training step. We study whether such a trait holds or fades across lineages. We instill the trait into three copies of Qwen2.5-7B-Instruct and iterate the training step to depth ten from each, reading every generation two ways on the same held-out prompts: a keyword screen that looks for expressions of the trait in the model's output, and an activation probe that projects each model's displacement from the base onto a direction built from the other lineages' teachers. We report two findings. First, the trait persists through ten generations across three lineages. The instilled models express it on every completion; the keyword-screen rate falls to 55.6% after the first step and to 21.1% by generation ten. The base itself matches the screen on none of its 300 completions. Second, the trait can be present internally while absent behaviorally. When the model's default system prompt is removed at evaluation, the generation-ten students' keyword-screen rate is zero on every prompt while the probe score stays positive on every prompt. Steering the untreated base with the displacement of a generation-ten student, which is trained and measured under the default system prompt, induces screened expression of the trait even with the system prompt removed, while that same student shows no expression of the trait with the system prompt removed.

## Metadata
- **Published**: 2026-09-22T05:51:18Z
- **Authors**: Ryan Vo, Duc-Vu Nguyen, Matt Kretchmar, Ngan Luu-Thuy Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25721v1)
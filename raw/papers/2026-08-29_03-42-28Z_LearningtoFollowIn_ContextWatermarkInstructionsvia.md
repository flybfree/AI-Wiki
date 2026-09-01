---
title: Learning to Follow In-Context Watermark Instructions via Self-Distillation
published: 2026-08-29T03:42:28Z
authors: Yepeng Liu, Tianyi Chen, Xuandong Zhao, Dawn Song, Yuheng Bu
url: http://arxiv.org/abs/2608.29030v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Follow In-Context Watermark Instructions via Self-Distillation

## Abstract
In-context watermarking (ICW) prepends an instruction to a query asking the model to embed a statistically detectable signal in its response. It thus equips LLMs with a watermarking interface that third parties can invoke without access to model internals. Its reliability hinges on the LLM following the instruction without degrading answer quality, yet how well current LLMs do so has not been measured. We introduce $\mathsf{ICWBench}$, a benchmark of three verifiable ICW instruction families, each scored on both detectability and answer quality. Evaluating 14 frontier proprietary and open-source LLMs, we find that none of the evaluated LLMs achieves both objectives across all three families. To address this, we propose a self-contained two-stage training method, requiring no distillation from a stronger model, no manual annotation, and no pre-existing ICW IF ability. The first stage, self-distillation with logits perturbation (SDLP), uses the same base LLM as both teacher and student: an instruction-equivalent decoding-time logits perturbation makes the teacher follow the ICW instruction, and the student is trained to match the teacher's output distribution. The second stage applies reinforcement learning with the automatic verifier as the reward. Applied to Qwen3-14B and GPT-OSS-20B, our method raises average TPR@$1\%$FPR across three ICW instructions from $0.100$ to $0.974$ and from $0.337$ to $0.968$, respectively, while maintaining high response quality under both perplexity evaluation and LLM-as-a-Judge.

## Metadata
- **Published**: 2026-08-29T03:42:28Z
- **Authors**: Yepeng Liu, Tianyi Chen, Xuandong Zhao, Dawn Song, Yuheng Bu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29030v1)
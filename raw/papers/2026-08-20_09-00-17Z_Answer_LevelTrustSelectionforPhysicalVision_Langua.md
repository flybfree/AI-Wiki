---
title: Answer-Level Trust Selection for Physical Vision-Language Reasoning
published: 2026-08-20T09:00:17Z
authors: Rongyu Yu, Ke Niu, Fengxiang He
url: http://arxiv.org/abs/2608.19807v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Answer-Level Trust Selection for Physical Vision-Language Reasoning

## Abstract
Vision-language models (VLMs) can estimate physical quantities such as duration, speed, and acceleration from visual observations, but existing benchmarks primarily assess overall model performance against annotated ground truth. In deployment, a key question is whether an individual prediction can be trusted when its ground truth is unavailable. Self-consistency alone may fail to capture important failure modes: a VLM may produce stable-but-wrong estimates or rely on textual priors rather than visual evidence. We formulate answer-level selective prediction for quantitative physical reasoning and propose Answer-Level Trust Selection (ATS), a post-hoc, model-agnostic framework for accepting or rejecting individual VLM predictions. ATS requires no fine-tuning, auxiliary verifier, or access to the model's internal logits. Instead, it aggregates eight interpretable behavioral diagnostic scores derived from repeated queries and controlled interventions into a unified trust score. We evaluate ATS in depth on Qwen2.5-VL-7B and across 20 VLM backbones, examining selective performance, diagnostic behavior, and targeted failure modes. Our results show that intervention-based diagnostics help identify stable-but-wrong and prior-tracking predictions that repeated agreement alone may miss. However, improved failure-case rejection can come at the cost of lower retention of correct predictions. ATS therefore complements model-level capability evaluation with answer-level reliability assessment for quantitative VLM predictions. Code will be released upon publication.

## Metadata
- **Published**: 2026-08-20T09:00:17Z
- **Authors**: Rongyu Yu, Ke Niu, Fengxiang He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19807v1)
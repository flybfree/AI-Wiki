---
title: Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization
published: 2026-09-02T09:01:51Z
authors: Bing Zheng, Zongyao Zhao, Wenming Yang
url: http://arxiv.org/abs/2609.02316v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization

## Abstract
Generative engine optimization (GEO) enables content producers to increase the visibility of their web pages in generative search engines, but the same techniques can deliver targeted misinformation when adversaries publish ordinary-looking GEO-optimized documents that victim large language models (LLMs) retrieve and synthesize into distorted answers. No existing benchmark evaluates defenses against this threat under controlled conditions. Therefore, we present Counter-GEO-Bench, a defense benchmark that pairs 247 human-verified, quality-gated queries with information-preserving and information-distorting GEO rewrites, and evaluates defenses on attack success rate (ASR), false positive rate, and answer quality across three victim LLMs. Under Counter-GEO-Bench, three off-the-shelf defenses (Granite Guardian, Llama Guard 3, and NeMo Self-Check Fact-Checking) reduce ASR by at most 5.7% relative, while Granite Guardian's reduction is not statistically significant. Safety-taxonomy guardrails target policy violations, while GEO misinformation passes through them as fluent informational content. To this end, a lightweight benchmark baseline, C-GEO Guard, is proposed, reducing ASR by 47.6% relative with near-zero utility loss, which proves threat tractable.

## Metadata
- **Published**: 2026-09-02T09:01:51Z
- **Authors**: Bing Zheng, Zongyao Zhao, Wenming Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02316v1)
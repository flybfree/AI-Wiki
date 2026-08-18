---
title: VARM-Bench: Benchmarking Verifiable Structured Reasoning in Chinese Abusive Speech Moderation
published: 2026-08-16T07:52:31Z
authors: Mingyu Yuan, Shengtao Wen, Lingbing Guo, Zhen Bi, Xiang Chen
url: http://arxiv.org/abs/2608.15600v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VARM-Bench: Benchmarking Verifiable Structured Reasoning in Chinese Abusive Speech Moderation

## Abstract
The widespread circulation of abusive online content has increased the need for reliable moderation of Chinese social-media text. Existing Chinese benchmarks support label classification, fine-grained toxicity categorization, and target-aware extraction, but do not provide a unified representation for deterministically verifying the stated basis of a moderation decision. We introduce VARM-Bench, a benchmark for field-anchored chain-of-thought rationales in Chinese abusive-speech moderation. Each instance contains a concise natural-language rationale with explicit anchors for six decisions: target, target type, target explicitness, author stance, harmfulness label, and fine-grained category. Our deterministic protocol evaluates field correctness, target alignment, output validity, complete-record agreement, and hidden record errors conditioned on correct final decisions, without relying on an LLM judge. Under a common structured-output protocol, we evaluate language models across multiple model families using zero-shot prompting, taxonomy guidance, and structured CoT supervision, and analyze lexical-cue sensitivity and field-level errors. Results show that strong label-level performance can conceal substantial errors in complete moderation records. VARM-Bench provides an auditable and reproducible benchmark for evaluating verifiable moderation rationales in Chinese abusive-speech moderation.

## Metadata
- **Published**: 2026-08-16T07:52:31Z
- **Authors**: Mingyu Yuan, Shengtao Wen, Lingbing Guo, Zhen Bi, Xiang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15600v1)
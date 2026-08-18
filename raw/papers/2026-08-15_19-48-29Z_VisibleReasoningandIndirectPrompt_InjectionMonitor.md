---
title: Visible Reasoning and Indirect Prompt-Injection Monitorability Across English, Tamil, and Tanglish
published: 2026-08-15T19:48:29Z
authors: Madhusudhanan G
url: http://arxiv.org/abs/2608.15392v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Visible Reasoning and Indirect Prompt-Injection Monitorability Across English, Tamil, and Tanglish

## Abstract
Chain-of-thought monitoring is a potentially useful safety signal, but its reliability across languages and behavioral settings remains uncertain. In a small case study of eight manually verified synthetic scenarios, one model, one annotator, and one deterministic generation seed, I study API-visible reasoning during indirect prompt injection in Sarvam-105B across English, Tamil, and Tanglish. A four scenario pilot found 5/12 injected attack successes without reasoning and 1/11 with reasoning. A preregistered four-scenario follow-up reversed that direction, finding 2/12 attacks without reasoning and 3/12 with reasoning. With only four scenarios per phase, this design cannot distinguish a real reasoning-mode effect from prompt-specific variation or sampling noise. Across 20 non-empty injected-thinking traces, all 17 benign-correct outputs stated an intent to ignore the injection, while all three attack successes stated an intent to follow it. These descriptive observations provide a reproducible case study of behaviorally informative visible reasoning when it is available; they do not establish that reasoning mode improves safety, that visible reasoning is mechanistically faithful, or that the findings generalize beyond this configuration.

## Metadata
- **Published**: 2026-08-15T19:48:29Z
- **Authors**: Madhusudhanan G
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15392v1)
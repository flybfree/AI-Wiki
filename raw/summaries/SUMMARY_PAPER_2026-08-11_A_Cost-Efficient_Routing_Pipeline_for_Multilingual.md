---
title: A Cost-Efficient Routing Pipeline for Multilingual Short-Text Classification Using Small Language Models
url: http://arxiv.org/abs/2608.10939v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_14-06-53Z_ACost_EfficientRoutingPipelineforMultilingualShort.md
generated_at: 2026-08-11 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a cost‑efficient routing pipeline for multilingual short‑text classification that distinguishes high‑resource and low‑resource languages without task‑specific fine‑tuning. By routing stronger languages directly through a compact sentence encoder while translating weaker ones to English, the system improves performance on low‑resource tiers and offers a fully self‑hosted solution using pretrained models.

## Key Takeaways
- The pipeline selectively translates only the lowest tier of languages, leaving high‑ and mid‑tier Macro‑F1 scores unchanged.  
- On SIB‑200, translating the low‑resource tier raises its Macro‑F1 from 0.4632 to 0.6828 while preserving higher tiers.  
- The optimal routing strategy varies by task; full translation (R3) yields the best overall result on MASSIVE despite higher latency.

## Context
Multilingual short‑text classification remains a bottleneck for operational AI systems that must serve diverse language communities without costly retraining. Current approaches often apply uniform inference policies, which can degrade performance for under‑represented languages and obscure trade‑offs between accuracy and efficiency.

## Implications
This work provides a practical framework for deploying multilingual classifiers with minimal resource allocation, encouraging industry adoption of tiered routing strategies. Practitioners can leverage this method to enhance inclusivity in customer support and content moderation while maintaining low latency across high‑resource languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10939v1)

---
title: Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator
published: 2026-08-27T17:29:09Z
authors: Varun Singh, Anuj Doshi, Makesh Narsimhan Sreedhar, Shaona Ghosh, Katherine Luna
url: http://arxiv.org/abs/2608.27548v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator

## Abstract
Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.

## Metadata
- **Published**: 2026-08-27T17:29:09Z
- **Authors**: Varun Singh, Anuj Doshi, Makesh Narsimhan Sreedhar, Shaona Ghosh, Katherine Luna
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27548v1)
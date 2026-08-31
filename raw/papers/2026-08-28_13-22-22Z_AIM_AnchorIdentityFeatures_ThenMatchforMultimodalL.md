---
title: AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning
published: 2026-08-28T13:22:22Z
authors: Wonjun Lee, Jaehyuk Jang, Kangwook Ko, Hee-Seon Kim, Changick Kim
url: http://arxiv.org/abs/2608.28312v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning

## Abstract
Multimodal large language models (MLLMs) can memorize identity-specific facts about people in their fine-tuning data, creating privacy risks when a person requests deletion. Existing MLLM unlearning methods often assume access to retain images or ground-truth answers during deletion, which is unrealistic in many practical scenarios. We study identity unlearning when retain images are unavailable at deletion time. Our analysis shows that identity and visual-perception questions occupy distinct regions in fine-tuned hidden states and are organized differently: identity questions cluster by person, whereas perception questions cluster by question type. This suggests that identity knowledge can be suppressed without erasing general visual perception. Building on this observation, we propose AIM, a two-stage method that anchors an identity-forgetting target with a universal visual prompt and then matches the vision encoder to that target under a Fisher-based constraint. Extensive experiments show that AIM achieves competitive identity forgetting while preserving non-deleted identities, prior knowledge, and visual perception on the same images.

## Metadata
- **Published**: 2026-08-28T13:22:22Z
- **Authors**: Wonjun Lee, Jaehyuk Jang, Kangwook Ko, Hee-Seon Kim, Changick Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28312v1)
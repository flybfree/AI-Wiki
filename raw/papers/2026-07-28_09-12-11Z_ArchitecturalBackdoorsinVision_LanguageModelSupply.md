---
title: Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering
published: 2026-07-28T09:12:11Z
authors: Maria Rosaria Briglia, Igor Maljkovic, Antonio Emanuele Cinà, Luca Oneto, Iacopo Masi, Fabio Roli
url: http://arxiv.org/abs/2607.25479v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering

## Abstract
Vision--Language Models (VLMs) are increasingly deployed through a model supply chain in which pretrained checkpoints, architecture definitions, text encoders, and exported computation graphs are distributed by third parties and reused across downstream services. This reuse model creates a security-critical trust boundary: VLM deployments inherit not only learned parameters but also executable behavior encoded in shared model artifacts. In this paper, we show that a malicious provider can exploit this trust boundary by embedding architectural backdoors into VLM supply chains through representation steering. Our attack introduces dormant steering logic into the model architecture through a trigger-gated additive modification of an intermediate representation, without poisoning training data, controlling downstream fine-tuning, or modifying prompts at deployment time. When the trigger is absent, the modification reduces to zero and the model follows its normal computation, preserving clean utility. When the trigger is present, a steering direction shifts the internal representation toward an attacker-defined objective. We evaluate the attack across multiple VLM families and downstream tasks, including visual question answering, text-to-image generation, retrieval, and semantic response biasing. The results show that the proposed architectural steering backdoor compromises integrity, safety enforcement, and ranking fairness while preserving normal behavior on clean inputs. We further show that shared VLM artifacts can carry dormant steering logic against downstream services, and we propose an auditing defense that inspects the executable logic distributed with model artifacts rather than only their learned weights.

## Metadata
- **Published**: 2026-07-28T09:12:11Z
- **Authors**: Maria Rosaria Briglia, Igor Maljkovic, Antonio Emanuele Cinà, Luca Oneto, Iacopo Masi, Fabio Roli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25479v1)
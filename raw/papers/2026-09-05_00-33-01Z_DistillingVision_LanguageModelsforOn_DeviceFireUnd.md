---
title: Distilling Vision-Language Models for On-Device Fire Understanding
published: 2026-09-05T00:33:01Z
authors: Mohammad Kazzazi, Zixuan Liu, Siavash Khajavi
url: http://arxiv.org/abs/2609.05782v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distilling Vision-Language Models for On-Device Fire Understanding

## Abstract
Vision-language models (VLMs) offer a promising alternative to conventional fire detection systems by reasoning about the semantic context of a scene and thus reducing false alarms, yet their large model size makes deployment on embedded fire sensors impractical. In this paper, we study how domain-specialized VLMs can be compressed for fully on-device deployment without losing the safety-critical behavior required for fire detection. We develop a teacher-student knowledge distillation framework in which large VLMs fine-tuned for fire understanding can be distilled into lightweight students. Experiments across multiple VLM families and model scales show that compact students preserve most of their teachers' fire-understanding capability. We further deploy the distilled models on our commercial Detectium fire detection sensor and jointly evaluate reasoning accuracy, latency, and memory usage. The results show that compression and deployment affect not only accuracy but also model failure modes, with Qwen2.5-0.5B providing the strongest overall deployment trade-off. Our findings provide broader guidance for deploying domain-specialized VLMs in resource-constrained, safety-critical settings.

## Metadata
- **Published**: 2026-09-05T00:33:01Z
- **Authors**: Mohammad Kazzazi, Zixuan Liu, Siavash Khajavi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05782v1)
---
title: MedUP: Awakening Unified Understanding and Perception in Medical Vision-Language Models
published: 2026-08-11T08:22:13Z
authors: Yuan Wang, Hualiang Wang, Yixin Chen, Songtao Jiang, Shujian Gao, Jiaming Lin, Siming Fu, Jian Wu, Zuozhu Liu
url: http://arxiv.org/abs/2608.10635v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MedUP: Awakening Unified Understanding and Perception in Medical Vision-Language Models

## Abstract
Medical Vision-Language Models (Med-VLMs) excel at verbalizing visual content, yet precise visual perception, segmentation, and grounding remain challenging. Existing approaches either verbalize regions as coordinate strings or rely on external modules that decouple perception from understanding, creating representation gaps for region-language alignment. We present MedUP, a Med-VLM that natively unifies perception and understanding within a shared token space. At its core lies UniMedTok, a region tokenizer that encodes masks as discrete tokens in the LLM vocabulary, enabling the model to seamlessly interleave mask tokens with text. We curate UniMed-Train, a 1.84M-instance corpus spanning text-guided segmentation, region-grounded understanding, medical VQA and CoT-based segmentation, and introduce UniMed-Bench for unified evaluation. Extensive experiments show that MedUP outperforms native, agentic, and dual-decoder Med-VLMs across all tasks while remaining competitive with specialist segmentors, demonstrating the strong potential of unified understanding and perception modeling.

## Metadata
- **Published**: 2026-08-11T08:22:13Z
- **Authors**: Yuan Wang, Hualiang Wang, Yixin Chen, Songtao Jiang, Shujian Gao, Jiaming Lin, Siming Fu, Jian Wu, Zuozhu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10635v1)
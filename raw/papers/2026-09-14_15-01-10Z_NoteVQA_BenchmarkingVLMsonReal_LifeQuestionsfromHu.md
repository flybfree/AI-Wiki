---
title: NoteVQA: Benchmarking VLMs on Real-Life Questions from Human Communities
published: 2026-09-14T15:01:10Z
authors: Haonan Jiang, Guojian Zhan, Jiancong Xie, Shijun Wan, Dongiia Zhao, Cheng Chen, Yahui Liu, Yao Hu, Chuan Mu
url: http://arxiv.org/abs/2609.15695v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NoteVQA: Benchmarking VLMs on Real-Life Questions from Human Communities

## Abstract
Vision-language models (VLMs) increasingly power consumer-facing AI search, yet evaluating them on the diversity of everyday visual questions remains challenging. Existing benchmarks often target predefined capabilities, such as multi-hop retrieval or long-form synthesis, whereas users ask photo-grounded questions spanning a long tail of everyday scenarios. Despite advances in VLMs, users on Xiaohongshu, a mainstream Chinese image-sharing platform, continue to turn to other people for help with everyday visual questions. Motivated by this behaviour, we curate NoteVQA from these questions, yielding 252 items across 12 topical categories and 7 user intents. Each item includes a concise reference distilled from expert community responses and a human-audited interleaved reference answer that combines textual explanations with supporting visual evidence. We evaluate both short-answer correctness and interleaved-answer quality. To support the latter, we introduce AgenticInterleave, a single-agent ReAct framework for retrieval-supported answer generation, together with IVR-12, a 12-dimensional rubric for assessing the content, presentation, and image quality of interleaved references and model outputs. Across 10 frontier VLMs, the highest short-answer accuracy is 52.8\%, while adding agentic search to Qwen3.5-397B-A17B improves accuracy by only 2.0\%. For interleaved answers, the same model running AgenticInterleave scores 3.52 under IVR-12, compared with 4.65 for the human-audited references, with the largest gap in content quality. These results highlight the challenges that everyday visual questions pose for current VLMs in both answer accuracy and the quality of visually grounded explanations.

## Metadata
- **Published**: 2026-09-14T15:01:10Z
- **Authors**: Haonan Jiang, Guojian Zhan, Jiancong Xie, Shijun Wan, Dongiia Zhao, Cheng Chen, Yahui Liu, Yao Hu, Chuan Mu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15695v1)
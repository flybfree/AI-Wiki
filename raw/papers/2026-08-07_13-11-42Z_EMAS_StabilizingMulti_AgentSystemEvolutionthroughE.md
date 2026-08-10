---
title: EMAS: Stabilizing Multi-Agent System Evolution through Evidence-Guided Revision
published: 2026-08-07T13:11:42Z
authors: Chao Fei, Qingyi Si, Kaihua Liang, Yanghua Xiao, Panos Kalnis, Hongcheng Guo
url: http://arxiv.org/abs/2608.07196v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EMAS: Stabilizing Multi-Agent System Evolution through Evidence-Guided Revision

## Abstract
Many methods for automated multi-agent system design optimize prompts and topologies during an initial design stage and then deploy the resulting system unchanged on subsequent samples. Experience from these samples is rarely consolidated into reusable system updates, while accuracy-oriented designs may incur high token costs. We introduce EMAS (Evolving Multi-Agent System), which uses this experience to revise MAS topology and prompts without updating LLM parameters, either to improve accuracy or to reduce cost. EMAS converts traces into structured diagnoses that specify a revision operation and target. It generates a candidate revision only when the same diagnosis recurs across samples and applies it only if paired validation against the current MAS meets the corresponding acceptance criterion. Across four benchmarks and two LLMs, EMAS attains the highest task-weighted overall accuracy for both backbones and is best or tied in six of eight model--benchmark settings. Within two evolution epochs, EMAS achieves relative gains of 6.30% and 20.10% in task-weighted accuracy on Kimi-K2-6 and Qwen3.6-27B, respectively. On MBPP with Qwen3.6-27B, EMAS raises accuracy from 55.09% to 89.12% while reducing token use per task by 62.2%. These results show that EMAS can turn experience from new samples into reusable updates to MAS topology and prompts.

## Metadata
- **Published**: 2026-08-07T13:11:42Z
- **Authors**: Chao Fei, Qingyi Si, Kaihua Liang, Yanghua Xiao, Panos Kalnis, Hongcheng Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07196v1)
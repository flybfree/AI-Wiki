---
title: Equitable System-Prompt Selection via Constrained Mixed-Strategy GroupDRO
published: 2026-08-05T01:35:08Z
authors: Mengyu Xu, Qiaoxin Yang, Zhihan Liu, Ruiyao Xu, Zachary Liu, Kezhen Chen, Chongyang Gao
url: http://arxiv.org/abs/2608.04339v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Equitable System-Prompt Selection via Constrained Mixed-Strategy GroupDRO

## Abstract
Large language models are increasingly used for information seeking, yet semantically equivalent questions phrased in different ways can receive answers of considerably different quality. System prompts are widely employed to steer response behavior, but they are typically optimized for average-case quality, so some question phrasings may still receive incomplete or low-quality answers. To address this, we formulate a constrained mixed-strategy GroupDRO framework for system-prompt selection. Instead of optimizing the system-prompt text, the framework assigns weights to system prompts in an existing pool to minimize the worst-case information-quality loss across evaluation metrics and groups, while constraining the mean loss to stay close to that of average-based selection. Because pool generation and selection are decoupled, the method applies to any system-prompt pool and can leverage an ensemble of complementary system prompts rather than a single one. Across five LLMs on two bilingual medical and consumer-finance benchmarks, the constrained method reduces the Overall Mean, Worst 25% Mean, and Worst by 13.1%, 13.2%, and 13.7% on average relative to no mitigation while keeping overall quality close to Average selection. Its multi-prompt weights reveal complementarity across metric-group pairs. Code and data are available at https://github.com/Rainxu09/equitable-system-prompt-selection.

## Metadata
- **Published**: 2026-08-05T01:35:08Z
- **Authors**: Mengyu Xu, Qiaoxin Yang, Zhihan Liu, Ruiyao Xu, Zachary Liu, Kezhen Chen, Chongyang Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04339v1)
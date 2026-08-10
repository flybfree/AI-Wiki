---
title: Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence
published: 2026-08-07T03:52:33Z
authors: Jiayun Zhang, Junshen Xu, Zejun Xie, Yi Fan
url: http://arxiv.org/abs/2608.06778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence

## Abstract
Mapping cyber threat intelligence (CTI) text to MITRE ATT&CK techniques is essential for structured threat analysis, yet manual annotation is costly and does not scale. The ATT&CK taxonomy comprises several hundred attack techniques, and a single CTI passage may describe multiple techniques, making accurate and complete extraction challenging. Existing automated approaches fall short in different ways: multi-label classifiers struggle with severe class imbalance and the large label space, while LLM-based methods--retrieval pipelines and fine-tuned generators--optimize token-level objectives that treat technique annotation as sequence generation rather than set prediction, lacking direct supervision on whether the predicted technique set is correct and complete. We propose TTP-R1, a two-stage framework that combines retrieval-augmented supervised fine-tuning (SFT) with reinforcement learning using verifiable rewards (RLVR). A hybrid retriever first narrows the large label space to a candidate set, and a fine-tuned LLM learns to select the correct techniques. We then apply Group Relative Policy Optimization with a decomposed reward that directly supervises the precision, recall, and output format of the predicted technique set. Across four CTI benchmarks, TTP-R1 achieves the best average F1, improving sub-technique-level F1 by 7.4 percentage points over Claude Sonnet 4.5 with retrieval augmentation, while running 28x faster when served as an 8B-parameter model on a single GPU.

## Metadata
- **Published**: 2026-08-07T03:52:33Z
- **Authors**: Jiayun Zhang, Junshen Xu, Zejun Xie, Yi Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06778v1)
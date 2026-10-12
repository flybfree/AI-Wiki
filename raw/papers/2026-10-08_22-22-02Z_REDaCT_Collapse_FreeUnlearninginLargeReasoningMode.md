---
title: REDaCT: Collapse-Free Unlearning in Large Reasoning Models
published: 2026-10-08T22:22:02Z
authors: Joshua Maccoby, Wendy Hui Wang
url: http://arxiv.org/abs/2610.12769v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REDaCT: Collapse-Free Unlearning in Large Reasoning Models

## Abstract
Unlearning in large reasoning models (LRMs) requires removing forget-set information from both the reasoning trace and the final answer. Existing approaches achieve this objective at the cost of reasoning collapse, where the model fails to produce a coherent chain-of-thought (CoT) and does not properly terminate its reasoning process. To address this challenge, we propose REDaCT (REgenerate via Detection and Corrective Tuning), an inference-time unlearning framework for LRMs. REDaCT consists of two key components: (1) a binary leak detector that identifies sentences in the reasoning trace that leak forget-set information, and (2) an embedding optimization module that learns a corrective embedding offline, such that when injected at the first detected leak during inference, it guides subsequent reasoning towards sentences that do not leak forget-set information. Experimental results show that REDaCT completely avoids reasoning collapse, substantially improving reasoning preservation compared to state-of-the-art unlearning methods while maintaining perfect answer forgetting and near-perfect CoT forgetting. Our code is available at: https://github.com/jmaccoby/redact.

## Metadata
- **Published**: 2026-10-08T22:22:02Z
- **Authors**: Joshua Maccoby, Wendy Hui Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12769v1)
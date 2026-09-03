---
title: Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large Language Models
published: 2026-09-02T04:12:35Z
authors: Tianqi Xiao, Shiyao Cui, Minghao Zhang, Junxiao Yang, Renmiao Chen
url: http://arxiv.org/abs/2609.02082v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large Language Models

## Abstract
Visual modality enhances the capabilities of multimodal large language models (MLLMs) but also introduces a safety concern: a benign textual query may convey harmful intent when grounded in a visual image. We term this cross-modal safety drift and our pilot studies show that the safety response rate for such requests is substantially lower than that for requests containing explicitly unsafe text. This paper aims to systematically study this issue. First, we conduct an empirical analysis to identify representative unsafe response patterns. Building on these, we interpret model representations and attentions, revealing that visually risky cues receive limited attention and weakly trigger refusal. Motivated by the observation that safety signals from unsafe text processing can be transferred, we propose safety-awareness representation transfer (SRT), a lightweight direction-refinement method that mitigates cross-modal safety drift with a frozen MLLM backbone. Experiments across multiple benchmarks and models show that SRT effectively improves safety in diverse cross-modal settings while preserving utility. Code is available at https://github.com/cucu220123/safety-awareness.

## Metadata
- **Published**: 2026-09-02T04:12:35Z
- **Authors**: Tianqi Xiao, Shiyao Cui, Minghao Zhang, Junxiao Yang, Renmiao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02082v1)
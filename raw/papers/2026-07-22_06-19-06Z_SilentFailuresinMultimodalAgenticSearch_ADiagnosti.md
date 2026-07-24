---
title: Silent Failures in Multimodal Agentic Search:A Diagnostic Taxonomy and Cross-Judge Evaluation
published: 2026-07-22T06:19:06Z
authors: Zhengxian Wu, Junjie Gao, Kai Yang
url: http://arxiv.org/abs/2607.19793v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Silent Failures in Multimodal Agentic Search:A Diagnostic Taxonomy and Cross-Judge Evaluation

## Abstract
Multimodal agentic search systems increasingly rely on external tools to answer knowledge-intensive visual questions. However, existing evaluations mainly focus on final-answer accuracy and may miss failures in the search trajectory. In this work, we study such hidden reliability issues as silent failures. We introduce a six-category taxonomy covering modality shortcuts, phantom grounding, wrong-evidence-right-answer cases, over-retrieval laundering, cross-modal contradiction, and provenance hallucination. Based on this taxonomy, we build a trajectory-level diagnostic pipeline that evaluates both answer correctness and evidence-grounding quality under a unified ReAct-style scaffold. Experiments on MMSearch-Plus trajectories across four frontier multimodal models show that surface accuracy consistently overestimates true trajectory-level correctness. We further use cross-judge validation, blank-image stress tests, and tool ablations to show that silent failures are capability-dependent and often shift rather than disappear. Home-page: https://github.com/DingWu1021/silent-failures-multimodal-agentic-search

## Metadata
- **Published**: 2026-07-22T06:19:06Z
- **Authors**: Zhengxian Wu, Junjie Gao, Kai Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19793v1)
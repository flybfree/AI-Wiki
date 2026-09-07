---
title: DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems
published: 2026-09-04T05:29:31Z
authors: Zehao Wang, Lanjun Wang, Shilong Jin, Junjie Chen, Yanghua Xiao
url: http://arxiv.org/abs/2609.04749v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems

## Abstract
Large language model (LLM)-based multi-agent systems have experienced rapid growth in recent years. Despite their promise, such systems remain fragile, frequently exhibiting reasoning and coordination errors that can lead to system-level failures. Failure attribution in such systems relies on tracing natural language interactions among agents to identify the decisive error, which refers to the earliest action whose correction can reverse system failure. There are two key challenges: 1) Shallow attribution: Existing methods often capture only minor deviations, such as incomplete retrievals or formatting errors, which verification mechanisms can correct, while missing the decisive cause of system failure. 2) Contextual degradation: As the length of the system traces increases, the model's reasoning ability rapidly deteriorates. To address these challenges, we propose DCFA, a training-free framework for failure attribution. DCFA integrates a global module that constructs structured causal-inspired dependency graphs from system traces to identify the initial decisive error, and a local module that applies local counterfactual-inspired reasoning to refine causal-inspired attribution. Experiments on the Who&When benchmark across six LLMs show that DCFA improves step-level accuracy by up to 8.27% over state-of-the-art baselines.

## Metadata
- **Published**: 2026-09-04T05:29:31Z
- **Authors**: Zehao Wang, Lanjun Wang, Shilong Jin, Junjie Chen, Yanghua Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04749v1)
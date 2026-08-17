---
title: BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs
published: 2026-08-14T10:16:13Z
authors: Varsha Ramineni, Hossein A. Rahmani, Jerome Ramos, Karin Sevegnani, Emine Yilmaz
url: http://arxiv.org/abs/2608.14161v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs

## Abstract
LLMs exhibit social biases that can produce inaccurate and discriminatory inferences, posing risks in high-stakes applications. While prior work has made progress in measuring and mitigating bias, it largely focuses on final outputs of models, with limited understanding of the mechanisms that produce biased outcomes. Recent advances in LLM reasoning offers a new lens for investigating bias, yet the link between reasoning and bias remains poorly understood. Existing approaches focus primarily on final answer correctness or explicitly biased language, overlooking different behaviours in reasoning that can drive biased outcomes. We introduce BiasTrace, an annotation scheme for labelling reasoning behaviours in model-generated traces and linking them to biased outcomes. BiasTrace captures bias-specific behaviours (e.g., unsupported demographic assumptions) as well as general reasoning patterns that may implicitly contribute to bias (e.g. overthinking). We apply BiasTrace to reasoning traces in bias-sensitive contexts, scaled using validated LLM-as-a-judge methods, producing a large annotated dataset. Our analysis shows that biased outputs often stem from subtle reasoning behaviours rather than explicitly biased language, and that reasoning-level annotations improve bias detection. We further show that BiasTrace behaviours can be exploited for inference-time mitigation. These findings underscore the importance of examining a broader range of reasoning patterns to better understand bias in LLMs.

## Metadata
- **Published**: 2026-08-14T10:16:13Z
- **Authors**: Varsha Ramineni, Hossein A. Rahmani, Jerome Ramos, Karin Sevegnani, Emine Yilmaz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14161v1)
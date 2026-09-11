---
title: Understanding In-Context Multimodal Jailbreaks via Posterior Reweighting
published: 2026-09-08T15:26:43Z
authors: Xu Zhang, Dev Mistry, Xiang Xu, Ren Wang
url: http://arxiv.org/abs/2609.10613v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding In-Context Multimodal Jailbreaks via Posterior Reweighting

## Abstract
In-context learning (ICL) jailbreaks reveal a critical vulnerability in multimodal large language models (MLLMs): harmful demonstrations in the prompt can induce unsafe outputs without modifying model parameters. Despite extensive empirical evidence, existing work lacks a principled understanding of why such jailbreaks reliably succeed or how their effectiveness scales with context composition. We propose a posterior reweighting framework that models a safety-aligned MLLM as implicitly operating over competing behavioral modes, and interprets in-context demonstrations as inference-time evidence that dynamically shifts the model's posterior preference between safe and harmful behaviors. This view formalizes jailbreak as a process of evidence accumulation, yielding predictive scaling laws with respect to demonstration count, harmful ratio, adversarial strength, and semantic diversity. Guided by this framework, we introduce a posterior-aware inference-time defense that adaptively injects benign counter-evidence based on estimated risk, effectively suppressing harmful posterior drift while preserving model utility. Compared to existing in-context defenses, our method achieves a significantly improved robustness-utility trade-off under a fixed intervention budget. Together, our results establish posterior reweighting as a unifying and predictive framework for understanding and mitigating ICL jailbreak in MLLMs.

## Metadata
- **Published**: 2026-09-08T15:26:43Z
- **Authors**: Xu Zhang, Dev Mistry, Xiang Xu, Ren Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.10613v1)
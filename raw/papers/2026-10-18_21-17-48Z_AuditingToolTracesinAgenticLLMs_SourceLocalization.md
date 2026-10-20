---
title: Auditing Tool Traces in Agentic LLMs: Source Localization and Counterfactual Dependence Testing
published: 2026-10-18T21:17:48Z
authors: Junhao Liu, Tianxiao Li, Yongxian Wu, Ziheng Duan, Ren Li, Jing Zhang, Martin Renqiang Min
url: http://arxiv.org/abs/2610.25540v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Tool Traces in Agentic LLMs: Source Localization and Counterfactual Dependence Testing

## Abstract
Agentic LLMs increasingly support scientific prediction by grounding decisions in external evidence. In biology, they promise accurate, interpretable predictions for important problems by integrating complex experimental and computational evidence. However, serialized tool results can contain hidden label shortcuts, such as dataset identifiers or template artifacts, that create apparent success without biological reasoning. To address this risk, we introduce a two-stage audit. Stage 1, Per-Tool TF-IDF Decomposition (PT2D), localizes label-predictive patterns to individual tool results while avoiding signal dilution in the concatenated tool trace. Stage 2, Token-Class Redaction, counterfactually tests whether the frozen LLM depends on the localized shortcut. We apply this audit to TCR-pMHC binding, where tool augmentation substantially outperforms a no-evidence baseline. At face value, this suggests that the LLM has learned to use scientific evidence. The audit overturns this interpretation: PT2D localizes the strongest signal to identifiers in one tool result, and redacting them reduces performance to chance. These findings show how hidden label shortcuts can masquerade as scientific reasoning or discovery, motivating source-level audits before benchmark gains are trusted.

## Metadata
- **Published**: 2026-10-18T21:17:48Z
- **Authors**: Junhao Liu, Tianxiao Li, Yongxian Wu, Ziheng Duan, Ren Li, Jing Zhang, Martin Renqiang Min
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25540v1)
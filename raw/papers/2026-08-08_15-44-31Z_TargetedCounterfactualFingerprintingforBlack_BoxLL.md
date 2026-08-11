---
title: Targeted Counterfactual Fingerprinting for Black-Box LLM Ownership Verification
published: 2026-08-08T15:44:31Z
authors: Yutong Wu, Xiaofan Bai, Shixin Li, Pingyi Hu, Ziqi Zhou, Zilong Wang, Xiaojing Ma, Songfeng Lu, Yuhong Li, Jin Xuan, Yi Wang, Dongmei Zhang, Bin Benjamin Zhu
url: http://arxiv.org/abs/2608.08195v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Targeted Counterfactual Fingerprinting for Black-Box LLM Ownership Verification

## Abstract
Large language models (LLMs) are high-value assets that can be derived through redeployment, fine-tuning, quantization, or further alignment. Because deployed LLMs are commonly exposed only through query APIs, ownership verification must often rely on black-box text responses. This setting is difficult: generations are open-ended and can vary across repeated queries, while existing black-box fingerprints rely on signals that are fragile under a final-response interface, including full-text matching, soft behavioral features, or model-specific prompts designed not to transfer. We propose TCF (Targeted Counterfactual Fingerprinting), a black-box LLM fingerprinting framework that converts open-ended generation comparison into constrained-answer targeted counterfactual transfer. TCF restricts each verification query to a finite answer space, reducing the surface-form ambiguity that enters the verification score, and optimizes a prompt perturbation toward a counterfactual target different from the protected model's clean answer on the original prompt. Verification reduces to checking whether the suspect model's parsed final answer matches the recorded target. We introduce the source-model counterfactual margin (SCM), a protected-model-only quantity that certifies the target is unlikely before the perturbation and likely after it; SCM controls target selection, perturbation stopping, and fingerprint filtering. Under explicit derived-preservation and independent-transfer budgets motivated by local behavioral closeness, we derive a target-accuracy gap between derived and independent models. Across four LLM families, TCF achieves an average AUC of 0.9861, improving over TRAP, ProFLingo, and ZeroPrint by 0.07 to 0.19.

## Metadata
- **Published**: 2026-08-08T15:44:31Z
- **Authors**: Yutong Wu, Xiaofan Bai, Shixin Li, Pingyi Hu, Ziqi Zhou, Zilong Wang, Xiaojing Ma, Songfeng Lu, Yuhong Li, Jin Xuan, Yi Wang, Dongmei Zhang, Bin Benjamin Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08195v1)
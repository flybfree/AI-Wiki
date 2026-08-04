---
title: Toward Fine-Grained Forgetting:Attribute Unlearning for Multimodal Large Language Models
published: 2026-08-02T05:23:44Z
authors: Junkai Lin, Junkai Chen, Siqi Hou, Yuhao He, Ruiqi Liu, Chenhan Jin, Shengze Xu, Tieyong Zeng
url: http://arxiv.org/abs/2608.01008v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward Fine-Grained Forgetting:Attribute Unlearning for Multimodal Large Language Models

## Abstract
Multimodal large language models (MLLMs) exhibit strong vision--language capabilities but may also memorize and disclose sensitive information. Machine unlearning seeks to remove designated knowledge without retraining from scratch while preserving general utility. Existing privacy-oriented benchmarks primarily adopt profile-level deletion, whereas practical requests are often finer grained: a model should forget a specified attribute while retaining non-sensitive information about the same identity. We therefore introduce attribute-level MLLM unlearning as a finer-grained task and construct a benchmark spanning long-text, numeric, and short-text targets, multiple forget ratios, and diverse question types. Our evaluation reveals that target and retained attributes share identity-specific and visual evidence, making selective forgetting susceptible to residual leakage or collateral degradation; accordingly, existing methods exhibit unstable forgetting--retention trade-offs in this setting. To address this challenge, we propose Causal Localization and Retain-Aware Projection (CLRP), a lightweight training-free framework. CLRP uses activation patching to identify the layer that causally mediates target-attribute disclosure, then applies a retain-aware projection that removes the target-attribute subspace while preserving same-identity evidence. Experiments across multiple widely used MLLMs with distinct architectures and parameter scales demonstrate the effectiveness of CLRP.

## Metadata
- **Published**: 2026-08-02T05:23:44Z
- **Authors**: Junkai Lin, Junkai Chen, Siqi Hou, Yuhao He, Ruiqi Liu, Chenhan Jin, Shengze Xu, Tieyong Zeng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01008v1)
---
title: Quantization-Triggered Backdoors in Language Models: Cross-Quantizer Transferability and the Validation--Deployment Gap
published: 2026-08-27T08:34:10Z
authors: Jacopo Dardini, Claudio Stanzione, Giordano Colò, Giuseppe Fenza
url: http://arxiv.org/abs/2608.27512v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantization-Triggered Backdoors in Language Models: Cross-Quantizer Transferability and the Validation--Deployment Gap

## Abstract
Post-training quantization is often treated as a semantically neutral optimization for edge deployment of Large Language Models. When a full-precision source checkpoint is evaluated and quantization is applied downstream without equivalent re-evaluation, this workflow creates a structural validation--deployment gap: because quantization is a many-to-one mapping over parameter space, source-precision certification does not guarantee behavioral equivalence in the deployed configuration. We formalize this gap through Quantization Behavioral Equivalence Classes (QBECs) and prove that QBEC membership does not imply behavioral equivalence, providing a theoretical basis for quantization-triggered backdoor attacks. Building on a three-stage adversarial fine-tuning framework, we embed latent malicious payloads into models that satisfy the source-precision checks used in our evaluation, yet activate targeted adversarial behavior upon INT8 or 4-bit compression. We evaluate this threat in two operationally motivated scenarios, tactical machine translation and political content analysis, extending prior work from decoder-only causal LMs to multilingual encoder-decoder sequence-to-sequence models. Results show that backdoored translation models move from zero measured friend--foe corruption at repaired FP16 to up to 85.02% inversion after quantization, and that a paired stance classifier measures an ideological shift of up to $Δ\mathrm{Bias}=0.33$ upon compression. A cross-quantizer transferability analysis further shows that attack persistence varies across quantization schemes and model architectures, rather than being determined by nominal bit-width alone. These findings demonstrate that source-precision auditing alone does not rule out quantization-triggered behavior and that the final deployed configuration must be included in behavioral certification for trustworthy edge AI.

## Metadata
- **Published**: 2026-08-27T08:34:10Z
- **Authors**: Jacopo Dardini, Claudio Stanzione, Giordano Colò, Giuseppe Fenza
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27512v1)
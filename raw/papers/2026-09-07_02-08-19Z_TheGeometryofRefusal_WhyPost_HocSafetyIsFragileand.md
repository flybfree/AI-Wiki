---
title: The Geometry of Refusal: Why Post-Hoc Safety Is Fragile and Pretraining-Time Safety Persists
published: 2026-09-07T02:08:19Z
authors: Srikanth Malla, Chiho Choi, Joon Hee Choi
url: http://arxiv.org/abs/2609.06934v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Geometry of Refusal: Why Post-Hoc Safety Is Fragile and Pretraining-Time Safety Persists

## Abstract
Post-hoc safety training (RLHF, DPO) is the dominant way to align large language models, yet jailbreaks (Zou et al., 2023b), fine-tuning attacks (Qi et al., 2024), and activation-space probes (Arditi et al., 2024) keep recovering the behaviors it was meant to remove. We give this fragility one geometric explanation and trace it to when, during pretraining, safety can take hold. We measure the safety update $Δ= W_{\text{safe}} - W_{\text{base}}$ against the curvature of the model's capabilities (the empirical Fisher of a capability loss). Post-hoc safety consistently lands in a suppression regime: $Δ$ is nearly orthogonal to the capability directions, and its small in-subspace part concentrates on a few high-curvature ones. The update is thin but sharp, a refusal gate laid over intact capabilities rather than erasure of them. A kernel-immobility lemma explains why such an update can only mask a capability, not remove it, so a little benign fine-tuning restores it: 100 steps of benign fine-tuning collapse refusal on Qwen-2.5-7B and Llama-3-8B Instruct at preserved capability, a signature that replicates across five model families.   Following the account into pretraining, a 267-checkpoint sweep of OLMo-2-1B (OLMo et al., 2025) shows the substrate that safety engages emerging in a sharp transition between roughly 6B and 60B pretraining tokens. We then use the account constructively: models trained from scratch with safety co-training spread continuously across pretraining reach 87 to 98% refusal whose post-attack level holds at 84 to 91% at every scale, an erosion of 2 to 14 pp against 35 to 38 pp for post-hoc installs, at capability matched or better than an LM-only baseline and holding from 410M to 6.9B, whereas a compute-matched windowed schedule installs no lasting refusal. Persistence of the safety signal across pretraining, not its timing, is what buys attack robustness.

## Metadata
- **Published**: 2026-09-07T02:08:19Z
- **Authors**: Srikanth Malla, Chiho Choi, Joon Hee Choi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06934v1)
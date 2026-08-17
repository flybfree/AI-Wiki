---
title: Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers
published: 2026-08-14T08:50:51Z
authors: Thiago Sandoval, Ufuk Topcu
url: http://arxiv.org/abs/2608.14089v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers

## Abstract
Safety classifiers deployed with large language models often fail for two reasons: their decisions reflect the policy learned during training rather than the deployer's desired policy, and their performance degrades as deployment traffic evolves. We present Regime-Conditional Verification (RCV), a lightweight wrapper that adapts an off-the-shelf safety classifier without retraining it. RCV estimates, from the classifier's internal representations, the probability that each prediction disagrees with the deployer's policy, and selectively corrects predictions likely to be wrong. The same correctness estimates also provide a label-free signal for detecting distribution shift, enabling a maintenance loop that updates the correctness estimation layer and resorts to classifier fine-tuning only when necessary. Across three off-the-shelf safety classifiers and two benchmark datasets, RCV improves adherence to the deployer's policy in every classifier-dataset combination, catching up to 0.81 of previously missed unsafe content without modifying the underlying classifier. In a deployment study with ten attack campaigns, each a harm category held out of RCV's training, RCV detects every campaign in a dedicated injection panel; in the maintenance census most drift episodes are repaired without updating the classifier, and the fine-tune is reserved for the residual episodes that repair does not restore.

## Metadata
- **Published**: 2026-08-14T08:50:51Z
- **Authors**: Thiago Sandoval, Ufuk Topcu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14089v1)
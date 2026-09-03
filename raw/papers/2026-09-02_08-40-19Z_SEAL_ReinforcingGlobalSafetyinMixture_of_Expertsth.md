---
title: SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment
published: 2026-09-02T08:40:19Z
authors: Qingyu Meng, Yiwei Zha, Jiahuan Pei, Koen Hindriks, Herbert Bos, Min Chen
url: http://arxiv.org/abs/2609.02293v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment

## Abstract
Mixture-of-Experts (MoE) is a scaling architecture for large language models that activates only a small subset of expert modules per token, enabling massive parameter growth with nearly constant computation. Recent Hybrid MoE architecture adds \textit{shared experts} to capture consistently useful representations, further improving stability and generalization. MoE now powers many flagship open-source and commercial models, yet remains vulnerable to adversarial attacks. Specifically, sparse routing introduces a structural vulnerability: MoE safety hinges on which experts are activated, and adversaries can subvert this selection through jailbreak prompts, malicious fine-tuning, and weight-level pruning of safety-critical neurons. Existing defenses primarily focus on hardening the router, but an adversary may still manipulate or bypass the routing trajectory due to the routing process's nondeterministic nature, thereby collapsing the defense. To cope with this problem, we first identify theoretically and empirically that shared expert, an always-activated component containing a small proportion of safety-critical neurons, can overcome the uncertainty of sparsely activated routing path and serve as a router-independent anchor to enhance global safety alignment. Based on this insight, we propose SEAL, a training-time parameter-efficient defense that produces a plug-and-play adapter attached to shared expert, and SEAL++, a variant that adds an orthogonal constraint preserving pre-existing safety subspaces during training. We evaluate SEAL and SEAL++ across six attack scenarios that combine three adversarial inputs (harmful prompting, jailbreak, malicious fine-tuning) with and without neuron pruning. SEAL reduces attack success rate (ASR) by up to 60\%, at a capability cost of at most 1.4\% on a five-benchmark average. Additionally, SEAL can seamlessly integrate with router-level ......

## Metadata
- **Published**: 2026-09-02T08:40:19Z
- **Authors**: Qingyu Meng, Yiwei Zha, Jiahuan Pei, Koen Hindriks, Herbert Bos, Min Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02293v1)
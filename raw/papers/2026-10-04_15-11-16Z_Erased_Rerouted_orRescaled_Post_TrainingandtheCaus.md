---
title: Erased, Rerouted, or Rescaled? Post-Training and the Causal Quotient of a Language Model's Belief State
published: 2026-10-04T15:11:16Z
authors: Weihan Li, Tianshi Zheng, Junhao Wu, Xinlei Chen
url: http://arxiv.org/abs/2610.05292v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Erased, Rerouted, or Rescaled? Post-Training and the Causal Quotient of a Language Model's Belief State

## Abstract
What happens to information a pretrained model already encodes when post-training no longer rewards using it? The common language of representation compression conflates three fates: information may be erased, rerouted away from the decision while still represented, or rescaled to occupy less variance while still represented and used. We make these fates identifiable in models whose pretraining recovers Bayesian belief states. A reward that reads only a coarse function of the hidden state defines an exact reward-null kernel. The kernel lets us separately measure whether the information remains recoverable, whether decisions causally depend on it, and how much activation variance it occupies. Theory says what is protected: KL-anchored reinforcement learning preserves the reference policy's log-odds among equally rewarded outputs, supervised and unanchored objectives carry no such constraint, and spectral compression implies neither erasure nor loss of use. In controlled worlds, post-training mostly reroutes or rescales reward-null information and leaves it decodable. Without an anchor decisions can stop using it although the representation survives, and with one they keep using it. Erasure appears only under prolonged weight decay, for distinctions that neither reward nor next-token prediction can see. Open language models show the same dissociation: in-context belief geometry stays decodable under late-layer spectral compression, and within-class behavior depends on the anchor. Post-training thus selects a causal quotient of the pretrained belief state: the reward defines decision-equivalence, the anchor and the state update protect part of what it ignores, and optimization decides whether the rest is erased, rerouted, or rescaled.

## Metadata
- **Published**: 2026-10-04T15:11:16Z
- **Authors**: Weihan Li, Tianshi Zheng, Junhao Wu, Xinlei Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05292v1)
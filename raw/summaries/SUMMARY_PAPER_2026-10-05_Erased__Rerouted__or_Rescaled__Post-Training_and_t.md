---
title: Erased, Rerouted, or Rescaled? Post-Training and the Causal Quotient of a Language Model's Belief State
url: http://arxiv.org/abs/2610.05292v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-04_15-11-16Z_Erased_Rerouted_orRescaled_Post_TrainingandtheCaus.md
generated_at: 2026-10-05 22:18
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates what happens to information already encoded in a pretrained language model when post-training objectives no longer reward its use. The authors distinguish three distinct fates for such information—erasure, rerouting, and rescaling—and develop a formal framework using Bayesian belief-state models and a "reward-null kernel" to identify which fate actually occurs. Their central finding is that post-training overwhelmingly reroutes or rescales reward-null information rather than erasing it, and that the presence or absence of an anchor (such as a KL constraint) determines whether the model continues to causally use that information in its decisions.

## Key Takeaways
- The paper introduces the concept of a reward-null kernel, defined as the set of hidden-state distinctions that a reward function cannot distinguish because it reads only a coarse function of the state. This kernel allows researchers to separately measure three things: whether information remains recoverable from the representation, whether the model's decisions causally depend on that information, and how much activation variance the information occupies. This tripartite decomposition is the paper's core methodological contribution, enabling precise identification of erasure versus rerouting versus rescaling in controlled settings.
- The theoretical results establish clear protection guarantees: KL-anchored reinforcement learning provably preserves the reference policy's log-odds among equally rewarded outputs, meaning the anchor acts as a causal shield for belief-state information the reward ignores. Supervised fine-tuning and unanchored objectives carry no such constraint, so decisions can stop using information even though the representation survives intact. Spectral compression, often interpreted as information loss, is shown to imply neither erasure nor loss of use, challenging a common assumption in the representation-compression literature.
- Empirical results in controlled worlds and open language models confirm the dissociation: in-context belief geometry remains decodable under late-layer spectral compression, and within-class behavior depends critically on the anchor. True erasure appears only under prolonged weight decay applied to distinctions that neither the reward nor next-token prediction can observe, making erasure a rare and specific outcome rather than the default consequence of post-training.

## Context
This work addresses a foundational question in the post-training and alignment literature: when we fine-tune, RLHF, or otherwise post-train a language model, do we destroy the rich information the pretraining stage encoded, or do we merely change how the model routes and weights that information? The broader field often conflates representation compression with information loss, treating spectral changes in hidden states as evidence that knowledge has been erased. By formalizing the causal quotient of a belief state and introducing the reward-null kernel, the paper provides the first rigorous framework for separating representational survival from causal use, bridging Bayesian decision theory, information geometry, and practical model-training objectives.

## Implications
For practitioners designing post-training pipelines, the findings suggest that the choice of anchor—whether a KL penalty, a reference-policy constraint, or no anchor at all—determines whether a model retains access to pretrained knowledge that the reward signal does not explicitly reward. This has direct consequences for safety alignment, where preserving nuanced belief states may matter even when the reward function is coarse, and for model editing or distillation, where spectral compression should not be assumed to erase capability. The paper also implies that auditing a model's "knowledge" by probing its activations may overstate what the model actually uses in decisions, and that causal-dependence tests, not just decodability tests, are needed to assess whether post-training has genuinely degraded a model's internal reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.05292v1)

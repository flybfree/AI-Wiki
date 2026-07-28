---
title: Inference-Time Consensus for Mitigating Hidden Behaviors from LLM Fine-Tuning
published: 2026-07-25T23:41:47Z
authors: Adhyyan Narang, Artin Tajdini, Claire Zhang, Jamie Morgenstern
url: http://arxiv.org/abs/2607.23394v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inference-Time Consensus for Mitigating Hidden Behaviors from LLM Fine-Tuning

## Abstract
Recent work shows that fine-tuning language models on even a small amount of poisoned data can install targeted misbehavior, and ostensibly benign data can transmit hidden preferences that generalize broadly. Standard defenses, such as data filtering, mixing in harmless data, and regularization, attenuate these effects but do not eliminate them. We instead pursue robustness through redundancy: collecting multiple datasets from different sources and only learning what is common between them. Thus, if only a subset of sources are malicious, the misbehavior will be blocked. In order to implement this defense strategy, we fine-tune a separate reference model on each source's dataset and aggregate their next-token distributions at decoding time. We introduce two consensus decoders: a token-wise minimum, which caps each token at the lowest probability any source assigns, and a base-relative variant, which reverts to the base probability on any token the sources move in opposing directions. We further relax exact agreement to tolerate partial support across sources and different surface expressions of the same intention. Across controlled poisoning tasks, subliminal learning, and emergent misalignment, consensus decoding suppresses source-specific misbehavior while preserving shared desirable behavior, including cases where union training and weight averaging retain the unwanted behavior.

## Metadata
- **Published**: 2026-07-25T23:41:47Z
- **Authors**: Adhyyan Narang, Artin Tajdini, Claire Zhang, Jamie Morgenstern
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23394v1)
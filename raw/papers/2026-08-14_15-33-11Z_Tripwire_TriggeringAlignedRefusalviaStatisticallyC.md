---
title: Tripwire: Triggering Aligned Refusal via Statistically Certified Safety Neurons
published: 2026-08-14T15:33:11Z
authors: Wei Zhao, Zhe Li, Peixin Zhang, Jun Sun
url: http://arxiv.org/abs/2608.14392v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tripwire: Triggering Aligned Refusal via Statistically Certified Safety Neurons

## Abstract
Neuron- and path-level interventions offer the finest-grained route to defending large language models (LLMs) against jailbreak attacks, yet existing methods fall short of this promise, i.e., they often compromise model utility significantly. Specifically, one line of work suppresses toxic neurons to erase harmful semantics, but since such semantics are distributed across the network, blocking every pathway forces a large intervention footprint. An alternative line of research focus on identify safety neurons using external classifiers. While promising, the existing approaches suffer from compromising neurons that are important for the model utility as well. Moreover, both approaches remain always on and thus perturb every benign request even when no attack is present. To address these limitations, we present \ours{}, a training-free defense that first identifies safety-specific neurons through per-neuron hypothesis tests under false-discovery-rate control together with a utility-specificity filter. Based on this identification, a trigger-style clamp holds the selected neurons at their harmful-conditional mean activations, injecting an internal harmful-input signal that triggers the refusal behavior learned during alignment. The clamp is then realized by two provably equivalent deployment modes, namely a detector-gated inference-time intervention and an offline bias-patch weight edit. Extensive experiments across four safety-aligned LLMs and four representative attacks demonstrate that \ours{} reduces the average attack success rate to at most 2.0\% while incurring a utility drop of only 0.5\% to 5.3\% on MT-Bench, the smallest among all defenses. Code is available at https://anonymous.4open.science/r/Tripwire-65C4.

## Metadata
- **Published**: 2026-08-14T15:33:11Z
- **Authors**: Wei Zhao, Zhe Li, Peixin Zhang, Jun Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14392v1)
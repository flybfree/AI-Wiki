---
title: TRACE: A Multi-Layer Benchmark for Human AI Controller Coordination Under Drift and Failure
published: 2026-08-07T00:03:55Z
authors: Joshua Zuniga, Srinivasan Subramanian, Ramya Madhuri Narapureddy, Md Abdullah Al Hafiz Khan
url: http://arxiv.org/abs/2608.06657v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE: A Multi-Layer Benchmark for Human AI Controller Coordination Under Drift and Failure

## Abstract
Modern cyber-physical and AI-assisted systems couple human operators, AI decision modules, and automated controllers in a single control loop, so trustworthiness depends on the whole loop, not any one model. Yet no standard benchmark captures time-aligned, multi-layer traces of how drift and failures propagate across these layers, so we cannot diagnose where coordination breaks down, why, or how to recover. This paper targets one facet of that gap: drift, a deviation that can originate in any stack layer and that conventional single-modality monitoring cannot localize to a layer or pin to an onset time. We construct a benchmark by injecting controlled drift into traces derived from ALFRED, a grounded-instruction benchmark for everyday household tasks, yielding 1,918 drifted traces. Each trace is a time-aligned sequence of per-step records across five execution layers (state, observation, decision, rules, control), labeled with the drift type, affected layer, onset time, responsible actor, and causal mechanism, and validated by independent raters with inter-annotator agreement reported. We pair the dataset with a leak-aware protocol that removes a near-perfect onset leak, and a baseline study across classical, recurrent, and attention-based model families. Under this honest protocol, drift is identifiable and attributable well above random and majority baselines across every family (affected layer macro-F1 near 0.70, responsible actor near 0.85, causal mechanism near 0.49), and heavy attention offers no advantage over simpler models on this symbolic benchmark.

## Metadata
- **Published**: 2026-08-07T00:03:55Z
- **Authors**: Joshua Zuniga, Srinivasan Subramanian, Ramya Madhuri Narapureddy, Md Abdullah Al Hafiz Khan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06657v1)
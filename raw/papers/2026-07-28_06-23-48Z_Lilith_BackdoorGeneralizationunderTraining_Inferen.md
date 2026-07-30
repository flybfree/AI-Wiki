---
title: Lilith: Backdoor Generalization under Training-Inference Trigger Shift
published: 2026-07-28T06:23:48Z
authors: Zhou Feng, Jiahao Chen, Chunyi Zhou, Yuan Su, Tianyu Du, Yuwen Pu, Jianhai Chen, Jinbao Li, Shouling Ji
url: http://arxiv.org/abs/2607.26099v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lilith: Backdoor Generalization under Training-Inference Trigger Shift

## Abstract
Machine-learning services increasingly rely on public data, third-party providers, and outsourced training, creating opportunities for data-poisoning attacks that implant persistent malicious behavior while preserving benign utility. However, existing backdoor studies largely evaluate exact trigger reuse, training-exposed trigger diversity, or variations along predefined transformation axes. They therefore leave a critical blind spot: whether a backdoor learned from one training-time trigger can generalize to an inference-time trigger family absent from victim training. We formulate this problem as backdoor generalization under training--inference trigger shift and introduce Lilith, a black-box anchor-to-family framework. Using only disjoint surrogate resources, Lilith first induces a compact target-side vulnerability with a single training anchor, then constructs a bounded inference-only family that preserves the anchor-induced representation geometry. We characterize this mechanism through anchor clearance and family reach, deriving sufficient conditions for family-wise target preservation under local regularity and bounded surrogate--victim discrepancy. Experiments across datasets, architectures, poisoning rates, and defenses show that Lilith achieves high family-wise attack success with limited utility degradation and a small trigger generalization gap. Additional analyses show that family activation depends on representation alignment rather than the proposal mechanism, exposing a broader threat overlooked by exact-trigger evaluation.

## Metadata
- **Published**: 2026-07-28T06:23:48Z
- **Authors**: Zhou Feng, Jiahao Chen, Chunyi Zhou, Yuan Su, Tianyu Du, Yuwen Pu, Jianhai Chen, Jinbao Li, Shouling Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26099v1)
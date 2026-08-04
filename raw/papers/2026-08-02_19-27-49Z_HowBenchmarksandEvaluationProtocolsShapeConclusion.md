---
title: How Benchmarks and Evaluation Protocols Shape Conclusions in Provenance-Based Intrusion Detection
published: 2026-08-02T19:27:49Z
authors: Lorenzo Guerra, Thomas Chapuis, Guillaume Duc, Pavlo Mozharovskyi, Van-Tam Nguyen
url: http://arxiv.org/abs/2608.01454v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Benchmarks and Evaluation Protocols Shape Conclusions in Provenance-Based Intrusion Detection

## Abstract
Provenance-based intrusion detection systems (PIDS) frequently report strong performance, but the conclusions drawn from these results can be highly sensitive to benchmarking choices and evaluation protocols. We investigate this dependency by re-evaluating representative PIDS on public datasets that meet our audit, labeling, and calibration requirements. Focusing primarily on the audited DARPA TC E3 datasets, we apply a unified protocol with temporally separated test periods and validation-only checkpoint and threshold calibration, and ask which architectural claims are empirically supported. We find that alerting success and investigation utility can diverge sharply, as several systems surface attacks without providing enough process-level context to support forensic investigation. On three of the four primary datasets, a simple allowlist built from training executable names and paths matches or exceeds the selected learned baselines on key operating-point metrics, suggesting that much of their measured performance reflects lexical novelty rather than richer provenance modeling. To explain why only some datasets expose architectural differences, we measure semantic signal quality through feature completeness and field entropy. This analysis helps explain why several audited E3 datasets can expose alerting behavior without reliably separating model architectures, while Theia pairs the strongest semantic signal quality with the clearest improvements in ranking and node-level recovery by our reference model. These results show that architectural claims in PIDS should be interpreted together with the benchmark properties and evaluation protocol that produced them.

## Metadata
- **Published**: 2026-08-02T19:27:49Z
- **Authors**: Lorenzo Guerra, Thomas Chapuis, Guillaume Duc, Pavlo Mozharovskyi, Van-Tam Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01454v1)
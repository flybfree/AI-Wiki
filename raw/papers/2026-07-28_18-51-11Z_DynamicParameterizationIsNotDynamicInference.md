---
title: Dynamic Parameterization Is Not Dynamic Inference
published: 2026-07-28T18:51:11Z
authors: Zongfei Li, Yuan-yih Shang, Guozhong Luo
url: http://arxiv.org/abs/2607.26192v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Parameterization Is Not Dynamic Inference

## Abstract
Input-dependent controller coefficients are often treated as evidence of dynamic inference or computational savings. This interpretation conflates three properties: coefficient variation, dependence of a frozen model on how coefficients are assigned to inputs, and conditional execution. We focus on the second property and formulate a general principle of frozen-controller auditing. We provide one concrete implementation, Frozen-Controller Auditing (FCA), which caches the complete coefficient tensor along an unperturbed trajectory, disables the controller, and replays the frozen model with cross-input reassignment, token shuffling, and static profiles estimated from an independent calibration set. Because the coefficients are cached before any intervention, performance changes under replay measure assignment dependence without feedback from recomputing the controller on perturbed hidden states. Across seven independently trained 76M FeatureGate Transformers and three 504M models, static layerwise profiles retain 98.70% and 99.43% of the Correct-to-GlobalMean performance gap, respectively. Layer identity explains 87% to 96% of the coefficient variance. FeatureGate nevertheless executes every Transformer block, and its measured inference is 30.8% slower than Dense. On the public MUDDPythia-1.4B checkpoint, cross-input reassignment and token shuffling increase NLL by 1.9067 and 2.9637, respectively. These penalties show that the model depends strongly on content-conditioned cross-layer assignment. MUDDPythia also executes every Transformer block. The results show that dynamic parameterization alone does not establish dynamic inference and that functional dynamics do not establish computational savings. Claims about dynamic models should separately report coefficient variation, functional dependence of the frozen model, and actual execution.

## Metadata
- **Published**: 2026-07-28T18:51:11Z
- **Authors**: Zongfei Li, Yuan-yih Shang, Guozhong Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26192v1)
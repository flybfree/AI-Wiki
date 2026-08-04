---
title: Breaking Diversity Collapse in Spiking Pseudo-Ensembles for Efficient OOD Detection in Remote Sensing
published: 2026-08-02T08:44:25Z
authors: Srinivas Anumasa, Rushi Shah, Qiran Zou, Dianbo Liu
url: http://arxiv.org/abs/2608.01090v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Breaking Diversity Collapse in Spiking Pseudo-Ensembles for Efficient OOD Detection in Remote Sensing

## Abstract
Spiking Neural Networks (SNNs) are attractive for resource-constrained remote-sensing systems, but reliable out-of-distribution (OOD) detection remains challenging. Deep ensembles provide strong predictive uncertainty, yet require multiple complete models and backbone evaluations. We propose an efficient spiking pseudo-ensemble that attaches multiple lightweight classification heads to a frozen SNN backbone. Naively training these heads with cross-entropy can lead to diversity collapse, where independently parameterized heads may produce correlated predictions. To address this, we introduce an agree--disagree objective that preserves correct predictions on clean in-distribution samples while encouraging diversity on structured, uncertainty-inducing transformations of the same inputs. This provides a diversity-promoting training signal without requiring external OOD data. Experiments with Spikformer and ResNet19-SNN on EuroSAT demonstrate consistent improvements over conventionally trained pseudo-ensembles. Using three backbones with five heads each matches or improves upon a five-model deep ensemble on UCM and AID, while requiring approximately 38% fewer parameters and 40% fewer backbone evaluations. These results show that explicit diversity promotion can recover useful ensemble-style uncertainty at substantially lower deployment cost.

## Metadata
- **Published**: 2026-08-02T08:44:25Z
- **Authors**: Srinivas Anumasa, Rushi Shah, Qiran Zou, Dianbo Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01090v1)
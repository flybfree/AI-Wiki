---
title: Machine-learned syndrome post-selection for reliable quantum error correction
published: 2026-07-21T20:39:56Z
authors: Tobias Haug, Askery Canabarro, Leandro Aolita
url: http://arxiv.org/abs/2607.19563v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Machine-learned syndrome post-selection for reliable quantum error correction

## Abstract
Quantum error correction can be enhanced by post-selecting out runs that are likely to produce a logical failure, but the most accurate measures for that require costly decoder-level information. We introduce a practical, decoder-agnostic post-selection method that learns directly from syndrome data. The method trains a supervised classifier to distinguish between syndromes from low- and high-noise regimes, and then uses the classifier's output as an abort score for new runs, without requiring logical-error labels, correction operators, or code-specific likelihood calculations. We validate the approach in three complementary settings: circuit-level simulations of the Gross bivariate-bicycle code, code-capacity simulations of the surface code, and experimental logical magic-state distillation data from the QuEra neutral-atom processor. In the Gross and surface codes, learned syndrome post-selection reduces the conditional logical error rate at a fixed acceptance rate, with performance comparable to syndrome-weight filtering. For the surface code, the learned classifier reveals a post-selection transition distinct from the conventional decoding threshold. In the experimental data, the machine-learning score outperforms syndrome-weight post-selection and, when combined with logical-gap filtering, improves the output fidelity beyond using the logical gap alone. These results show that syndrome-only learning provides a scalable and hardware-compatible route to improving the reliability of quantum error correction.

## Metadata
- **Published**: 2026-07-21T20:39:56Z
- **Authors**: Tobias Haug, Askery Canabarro, Leandro Aolita
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19563v1)
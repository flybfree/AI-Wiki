---
title: From Atomic Evidence to Logical Composition: Structured Compositional Reasoning over Compound Answer Options
published: 2026-08-13T05:18:55Z
authors: Obed Junias, Maria Leonor Pacheco
url: http://arxiv.org/abs/2608.12836v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Atomic Evidence to Logical Composition: Structured Compositional Reasoning over Compound Answer Options

## Abstract
Large language models often fail when answer options require combining atomic judgments under explicit logical operators, even when they judge the individual atoms correctly. We study compound options connected by AND, OR, and NEITHER/NOR, introducing a framework that decomposes each option into atomic answers and scores contrastive hypotheses about each one, so the model never sees a compound option. An operator-constrained integer linear program then composes the calibrated scores into a single prediction. We evaluate on LOGICAL-COMMONSENSEQA and introduce LOGICAL-SATA, a reading-comprehension benchmark derived from SATA-Bench. Our framework improves Macro-F1 from 48.3 to 77.0 on the human-validated LOGICAL-COMMONSENSEQA split and from 47.0 to 75.6 on LOGICAL-SATA, with the largest gains on NEITHER/NOR.

## Metadata
- **Published**: 2026-08-13T05:18:55Z
- **Authors**: Obed Junias, Maria Leonor Pacheco
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12836v1)
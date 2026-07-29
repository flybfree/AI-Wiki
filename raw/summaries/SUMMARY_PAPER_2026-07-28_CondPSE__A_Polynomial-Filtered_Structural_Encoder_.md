---
title: CondPSE: A Polynomial-Filtered Structural Encoder with Conditional Modulation for Graphs
url: http://arxiv.org/abs/2607.25169v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_00-46-34Z_CondPSE_APolynomial_FilteredStructuralEncoderwithC.md
generated_at: 2026-07-28 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
CondPSE introduces a learned positional and structural encoder that applies a polynomial filter bank to Gaussian node probes, then refines the signals through FiLM-style modulation conditioned on cross-filter, local message-passing, and graph-level features. The encoder is pretrained to reconstruct both node‑level targets and global invariants, after which it is frozen for use as an input encoding in downstream tasks. Experiments show a substantial boost in synthetic structural discrimination benchmarks—CSL accuracy rises from 42.9 % to 97.3 % and EXP accuracy from 68.3 % to 99.9 % relative to GPSE, with the filter bank accounting for most of this gain.

## Key Takeaways
- The polynomial filter bank enables CondPSE to capture fine‑grained topological cues that standard message‑passing GNNs cannot represent.
- Freezing a pretrained PSE encoder yields strong performance on synthetic graph discrimination tasks, indicating that the encoder alone can learn discriminative structural representations.
- Despite these gains, real molecular property prediction shows no clear advantage over GPSE, suggesting that downstream integration and label alignment are crucial for transfer.

## Context
Message‑passing GNNs often fail to distinguish non‑isomorphic graphs because they lack explicit topological encodings. Positional and structural encoders (PSE) address this gap by injecting topology‑derived signals into graph representations. CondPSE extends this idea with a learned filter bank, offering a more expressive way to encode graph structure while remaining compatible with downstream models.

## Implications
For AI practitioners, CondPSE demonstrates that pretrained structural encoders can be powerful building blocks when properly aligned with task objectives. However, the paper cautions that success is not guaranteed across domains, highlighting the need for careful integration and alignment of pretraining targets with real‑world labels to unlock meaningful performance improvements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25169v1)

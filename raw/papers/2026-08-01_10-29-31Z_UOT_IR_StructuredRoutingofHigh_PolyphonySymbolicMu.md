---
title: UOT-IR: Structured Routing of High-Polyphony Symbolic Music into Fixed-Budget Representations
published: 2026-08-01T10:29:31Z
authors: Ziyue Kang, Nan Nan, Chenhao Lin, Xiaohong Guan
url: http://arxiv.org/abs/2608.00576v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UOT-IR: Structured Routing of High-Polyphony Symbolic Music into Fixed-Budget Representations

## Abstract
High-polyphony symbolic music is increasingly used in generation, analysis, and arrangement, yet many downstream tasks require bounded representations with fixed tracks or slots. Converting richly orchestrated scores into compact forms is therefore necessary, but existing approaches relying on heuristic simplification or generic representation-space reduction often fail to preserve structural roles, orchestration compatibility, and playability under strict budgets. To address the issue, this study reformulates the compression problem as a fixed-budget structured routing problem and proposes Unbalanced Optimal Transport for Information Routing (UOT-IR), a training-free framework based on constrained unbalanced optimal transport. UOT-IR combines an orchestration prior, adaptive marginal relaxation, temporal decoding, and playability-aware projection to produce compact and musically coherent bounded representations. This work further studies two practical settings under the same slot budget: template standardization, which maps each input to a predefined bounded template, and adaptive preservation, which retains representative content without assuming an external template. Experiments on the SymphonyNet corpus show that UOT-IR delivers strong overall performance across both settings, including the best Note-F1 in adaptive preservation (0.9120), together with the lowest structural cost (14.7165) and bad structural confusion rate (0.3406) in template standardization. This work establishes a principled paradigm for fixed-budget symbolic music compression, offering a practical path toward compact, structured, and musically coherent symbolic representations.

## Metadata
- **Published**: 2026-08-01T10:29:31Z
- **Authors**: Ziyue Kang, Nan Nan, Chenhao Lin, Xiaohong Guan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00576v1)
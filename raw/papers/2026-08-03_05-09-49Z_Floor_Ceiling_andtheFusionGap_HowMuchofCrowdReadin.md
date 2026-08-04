---
title: Floor, Ceiling, and the Fusion Gap: How Much of Crowd Reading Attention Can Machines Predict?
published: 2026-08-03T05:09:49Z
authors: Kazuki Nakayashiki, Keisuke Watanabe
url: http://arxiv.org/abs/2608.01704v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Floor, Ceiling, and the Fusion Gap: How Much of Crowd Reading Attention Can Machines Predict?

## Abstract
A benchmark score means nothing without knowing what a trivial method achieves and what the best possible method could achieve. We construct both bounds for a task with a rare kind of ground truth: predicting which sentences a crowd of readers -- highlighting for their own purposes, unpaid, uninstructed, and blind to each other -- marked in 120 web documents. The floor is naive truncation (lead); the ceiling is a split-half oracle: half the crowd predicting the other half. The gap between them is +0.2028 AP [+0.1698, +0.2342, domain-clustered], and three findings structure it. First, the gap is semantic: position and length features recover 5% of it. Second, frontier language models reach 35-53% of it zero-shot -- far above classical baselines, far below the crowd; a state-of-the-art prompt compressor (LLMLingua-2) lands below the floor, indistinguishable from random selection. Third, an unweighted cross-vendor fusion of five frontier rankings plus a position prior reaches 60%, beating the best single model by +0.0159 [+0.0044, +0.0269; Holm p=0.019] -- a gain that survives ablation of its best member, split-half arm selection, prompt paraphrase, and label, gate, and seed perturbations, and was CONFIRMED by a pre-registered replication on 217 independent documents (+0.0179, Holm p=0.042). Finally, the bracket compresses: distilling the fusion into one open-weight 8B student that reads the whole document retains 90% of the fusion's edge and reaches statistical parity with the strongest single frontier model (+0.0070 [-0.0068, +0.0200]), where a local-context student retains only 63% -- the crowd's signal lives in document-level structure, and the cheapest known improvement is to ask several different models and average.

## Metadata
- **Published**: 2026-08-03T05:09:49Z
- **Authors**: Kazuki Nakayashiki, Keisuke Watanabe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01704v1)
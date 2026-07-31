---
title: PlantBGC: Transformer for Plant BGC Discovery via Label-Free Domain Adaptation and Weak Supervision
published: 2026-07-29T03:13:48Z
authors: Yuhan Zhao, Nidhi Grover, Zhishan Guo, Ning Sui
url: http://arxiv.org/abs/2607.27258v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PlantBGC: Transformer for Plant BGC Discovery via Label-Free Domain Adaptation and Weak Supervision

## Abstract
Plant biosynthetic gene clusters (BGCs) encode specialized-metabolite pathways, yet curated plant BGC labels remain scarce, hindering supervised discovery at genome scale. Existing plant BGC mining tools are largely signature- and rule-driven and do not fully leverage recent advances in contextual representation learning for modeling long-range domain context and controlling false positives under strong domain shift. We seek an AI-assisted workflow that narrows experimental search space by transferring supervision from well-annotated microbial BGCs to plant genomes. We present PlantBGC, representing genomes as ordered Pfam-domain sequences and learning BGC-likeness with an encoder-only Transformer trained on MIBiG microbial BGCs and adapted to plants via label-free masked language modeling. On microbial benchmarks, PlantBGC achieves token-level AUC = 0.988 (10-fold CV) and 0.979 (leave-class-out). On plants, adaptation improves known-BGC recovery on n = 34 curated loci under strict 100% coverage, increasing recovery from 29.4% to 67.6% and indicating more complete boundaries. GO/KEGG-derived weak supervision reduces proxy primary-like ratio by 48.40% (GO) and 45.20% (KEGG), with consistent per-species reductions (paired Wilcoxon p = 1.53e-5). Compared to plantiSMASH, PlantBGC yields more compact loci on matched regions (median length ratio = 0.278; 93.8% of pairs are shorter).

## Metadata
- **Published**: 2026-07-29T03:13:48Z
- **Authors**: Yuhan Zhao, Nidhi Grover, Zhishan Guo, Ning Sui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27258v1)
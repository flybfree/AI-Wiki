---
title: Evolutionary Curriculum Learning Improves Biological Sequence Modeling
published: 2026-08-01T14:54:45Z
authors: Richard Zhu, Kento Nishi
url: http://arxiv.org/abs/2608.00697v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evolutionary Curriculum Learning Improves Biological Sequence Modeling

## Abstract
Variational autoencoders (VAEs) trained on multiple sequence alignments (MSAs) have emerged as powerful generative models for biological sequences, with applications ranging from disease variant prediction to functional RNA design. However, standard biological VAE training treats all sequences as exchangeable, ignoring the rich evolutionary structure that organizes homologous sequences from evolutionarily close to highly divergent. We propose Evolutionary Curriculum Learning (ECL), a training strategy that exploits this structure by progressively exposing the model to sequences of increasing evolutionary distance from sampled anchors, following a power-law expansion schedule. Applied to two architecturally distinct VAE models and two biological domains--protein variant effect prediction with EVE and RNA family sequence generation with RfamGen--ECL improves downstream task performance across five random seeds per configuration. Mean ClinVar classification AUROC rises from 0.981 to 0.989 for p53; for PTEN, ECL attains 1.000 in every seed whereas the baseline is unstable (mean 0.905, falling as low as 0.54). For RNA, ECL raises mean covariance-model bit scores on all three families tested and exceeds its seed-matched baseline in 12 of 15 training runs, though with only three families the effect cannot be established as significant at the family level. Ablation experiments show that progressively expanding the sampled sequences by evolutionary distance outperforms fixed-size neighborhood sampling in addition to uniform random sampling. Evolutionary distance is therefore a useful inductive bias for ordering the training curriculum in biological sequence modeling.

## Metadata
- **Published**: 2026-08-01T14:54:45Z
- **Authors**: Richard Zhu, Kento Nishi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00697v1)
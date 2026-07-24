---
title: Causal dictionary learning reveals and validates transcription-factor binding features in genomic language models
published: 2026-07-21T22:54:46Z
authors: Sarwan Ali
url: http://arxiv.org/abs/2607.19618v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Causal dictionary learning reveals and validates transcription-factor binding features in genomic language models

## Abstract
Genomic language models achieve strong performance across regulatory-genomics tasks, yet what these models internally represent remains opaque, and the field lacks a principled procedure for verifying that an apparent ``concept'' inside a model is real rather than an artifact of sequence composition. We introduce a framework that combines sparse dictionary learning with causal intervention to extract, validate, and causally test interpretable features in genomic foundation models. Training top-$k$ sparse autoencoders on the hidden activations of two architecturally distinct models, Nucleotide Transformer ($6$-mer tokenization) and DNABERT-2 (byte-pair encoding), we recover thousands of monosemantic features that map to transcription-factor (TF) sequence motifs. We show that the naive validation of such features against position weight matrices is severely confounded by GC composition and repetitive elements, producing hundreds of spurious ``TF features'', and we develop a composition-matched, binding-resolved protocol that removes these confounds. Critically, we move beyond correlation: by ablating individual dictionary directions during the model's forward pass and measuring the induced shift in the model's own predictive distribution, we establish that specific features are \emph{causally} used to represent cell-type-specific TF binding, not merely motif presence. Across three transcription factors (CTCF, GATA1, REST) and both architectures, causally validated binding features emerge reproducibly ($7$--$14$ of $15$ tested features per condition), while two classes of negative control, scrambled binding labels and randomly selected features, yield no detectable signal. The framework is purely computational, uses only public data, and provides a reusable standard for interpretability claims in genomic deep learning.

## Metadata
- **Published**: 2026-07-21T22:54:46Z
- **Authors**: Sarwan Ali
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19618v1)
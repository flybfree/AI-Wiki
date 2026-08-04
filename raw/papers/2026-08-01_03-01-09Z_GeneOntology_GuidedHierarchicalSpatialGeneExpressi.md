---
title: Gene Ontology-Guided Hierarchical Spatial Gene Expression Prediction from Histopathology Images
published: 2026-08-01T03:01:09Z
authors: Zhiwen Xu, Xiaoming Yan, Chengkun Wu, Juan Chen, Haoang Chi, Liyang Xu
url: http://arxiv.org/abs/2608.00405v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gene Ontology-Guided Hierarchical Spatial Gene Expression Prediction from Histopathology Images

## Abstract
Predicting spatial gene expression from histopathology images enables large-scale transcriptomic profiling without the cost of direct measurement. Existing methods decode the target gene set as a flat, unstructured vector, ignoring the inter-gene dependencies arising from shared biological pathways and regulatory programs. Without explicit structural guidance, models must infer these dependencies entirely from limited paired data, constraining prediction quality. We propose MSGR (Multi-Scale Gene Refiner), which bridges this gap by incorporating the Gene Ontology (GO), a curated functional hierarchy of genes, as an explicit structural prior. MSGR organizes target genes into a four-level GO tree. Its GO-guided decoder then progressively refines predictions from coarse functional domains to fine individual genes via residual corrections under scale-weighted supervision. Operating solely on the gene side, the GO-guided decoder serves as a seamless plug-in replacement that consistently improves existing architectures without requiring any image-side modifications. Extensive experiments on nine datasets from the HEST-1k benchmark provide empirical evidence for two central claims: GO-structured decoding consistently outperforms flat decoding, even against a state-of-the-art generative baseline, and the gain is attributable to biological ontology structure rather than hierarchical decomposition per se, as confirmed by a +0.027 margin over a structurally equivalent random hierarchy.

## Metadata
- **Published**: 2026-08-01T03:01:09Z
- **Authors**: Zhiwen Xu, Xiaoming Yan, Chengkun Wu, Juan Chen, Haoang Chi, Liyang Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00405v1)
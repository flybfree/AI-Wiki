---
title: Do General NLP Embeddings Capture Ontological Reasoning?
published: 2026-08-31T18:03:23Z
authors: Hamed Babaei Giglou, Jennifer D'Souza, Sören Auer
url: http://arxiv.org/abs/2609.00177v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do General NLP Embeddings Capture Ontological Reasoning?

## Abstract
General-purpose NLP embedding models perform well on linguistic tasks, but their ability to capture symbolic ontological structure remains unclear. We introduce AVA, a systematic framework for evaluating whether embeddings distinguish logic-sensitive relational semantics in ontologies and knowledge graphs. AVA comprises 171,007 contrastive triplets derived from 163 heterogeneous ontologies using hierarchy inversion, relation substitution, and disjointness injection. Each triplet contains an ontology statement, a semantically equivalent paraphrase, and a logic-sensitive hard negative with contradictory relational meaning. We evaluate more than 25 state-of-the-art embedding models and find substantial limitations: the best model achieves only 0.739 triplet accuracy, while hard negative accuracy falls to 0.135. Fine-tuning improves discrimination by a large margin but transfers poorly to downstream Semantic Web tasks, including taxonomy discovery and ontology alignment. Further analysis suggests that improvements stem partly from perturbation-specific pattern recognition rather than robust ontological understanding. These findings reveal a persistent gap between linguistic representation learning and ontology-level discrimination, challenging the assumption that strong NLP benchmark performance translates to Semantic Web competence.

## Metadata
- **Published**: 2026-08-31T18:03:23Z
- **Authors**: Hamed Babaei Giglou, Jennifer D'Souza, Sören Auer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00177v1)
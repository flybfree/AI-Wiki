---
title: An Ontology for Machine Learning Interatomic Potentials
published: 2026-07-25T14:16:09Z
authors: Daniel Hernández, Jong Hyun Jung, Yuji Ikeda, Yongliang Ou, Pranav Kumar, Tom Schächtel, Wenchuan Liu, Xin Li, Xi Zhang, Xiang Xu, Lifang Zhu, Fritz Körmann, Steffen Staab, Blazej Grabowski
url: http://arxiv.org/abs/2607.23219v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Ontology for Machine Learning Interatomic Potentials

## Abstract
Machine learning interatomic potentials (MLIPs) approximate quantum-mechanical energies and forces---conventionally computed by density functional theory (DFT) or wave-function methods---at a fraction of the cost. The field encompasses a growing ecosystem of algorithms, training datasets, hyperparameters, and target materials, yet the metadata needed to systematically compare, reproduce, and build upon MLIP studies remains scattered across papers, scripts, and ad-hoc file formats. We present the MLIPs ontology, an OWL 2 DL ontology that captures the concepts needed to describe MLIP methods, their hyperparameters, training datasets with DFT provenance, and published benchmarks. The ontology is organized into three modules---Method, Training Data, and Benchmark---and connects existing ontologies in materials science (MDO, CMSO/ASMO) and machine learning (ML-Schema), complementing dataset-side schemas such as Croissant. It declares 27 formal axioms enforcing data completeness and consistency, including property chains that link trained models to their methods and training data. We demonstrate the ontology through a running example based on Moment Tensor Potentials and evaluate it through competency-question execution on a 20-paper seeded knowledge graph, OWL reasoning, and comparison with existing ontologies.

## Metadata
- **Published**: 2026-07-25T14:16:09Z
- **Authors**: Daniel Hernández, Jong Hyun Jung, Yuji Ikeda, Yongliang Ou, Pranav Kumar, Tom Schächtel, Wenchuan Liu, Xin Li, Xi Zhang, Xiang Xu, Lifang Zhu, Fritz Körmann, Steffen Staab, Blazej Grabowski
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23219v1)
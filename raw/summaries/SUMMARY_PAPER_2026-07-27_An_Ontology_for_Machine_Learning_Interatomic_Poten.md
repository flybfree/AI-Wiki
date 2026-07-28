---
title: An Ontology for Machine Learning Interatomic Potentials
url: http://arxiv.org/abs/2607.23219v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_14-16-09Z_AnOntologyforMachineLearningInteratomicPotentials.md
generated_at: 2026-07-27 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces the MLIPs ontology, an OWL 2 DL framework designed to capture the concepts needed for describing machine‑learning interatomic potentials, their hyperparameters, training datasets with DFT provenance, and benchmark results. The ontology is organized into three modules—Method, Training Data, and Benchmark—and includes 27 formal axioms that enforce completeness and consistency. A running example based on Moment Tensor Potentials demonstrates the ontology through competency‑question execution on a knowledge graph.

## Key Takeaways
- Metadata for MLIP studies is currently scattered across papers, scripts, and ad‑hoc file formats, making systematic comparison and reproduction difficult.
- The ontology provides a structured representation of methods, hyperparameters, training datasets (with DFT provenance), and published benchmarks to enable reproducibility.
- Demonstrations include competency‑question execution on a 20‑paper seeded knowledge graph, OWL reasoning, and comparison with existing ontologies.

## Context
The machine‑learning interatomic potentials field has expanded rapidly, yet the lack of standardized metadata hampers progress. This ontology addresses that gap by offering a unified schema that integrates materials‑science ontologies (MDO, CMSO/ASMO) with machine‑learning schemas (ML‑Schema). By linking trained models to their underlying methods and data, it supports reproducible research across AI and computational chemistry.

## Implications
For researchers, the ontology enables systematic comparison of MLIP studies, facilitating the building upon previous work. In industry, standardized metadata can accelerate the adoption of MLIPs for materials design, reducing development time and cost. Practitioners benefit from a common language that integrates with existing tools like Croissant, enhancing interoperability across research pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23219v1)

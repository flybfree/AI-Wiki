---
title: Generative Artificial Intelligence (GenAI) to convert images of queuing networks into verifiable simulation models: an open-weight LLM workflow approach
published: 2026-07-27T10:50:37Z
authors: Thomas Monks, Alison Harper, Amy Heather, Navonil Mustafee
url: http://arxiv.org/abs/2607.24259v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generative Artificial Intelligence (GenAI) to convert images of queuing networks into verifiable simulation models: an open-weight LLM workflow approach

## Abstract
Recent work has explored the use of Large Language Models (LLMs) to automate simulation model building, typically by generating executable code directly from natural language descriptions. However, this raises challenges for verification and reproducibility particularly for users without programming expertise. We propose Sketch2DES, a sketch-to-simulation workflow that converts diagrammatic representations of queuing networks into verifiable discrete-event simulation models using open-weight LLMs. The workflow has three stages: (1) translation of a diagram into a semi-structured textual description using a multimodal LLM; (2) conversion into schema-validated structured data (JSON) via an LLM with a reflection-based verification loop; and (3) deterministic transformation into an executable simulation model using a software adapter. Intermediate artefacts can therefore be inspected and automatically validated before execution. We evaluate the approach on eight queuing-network diagrams of varying complexity. The workflow achieved high reliability for all stages, and results were statistically indistinguishable from human-coded and analytical benchmarks. Compared to direct code generation, the workflow improves reproducibility, transparency, and verifiability, while reducing the need for programming expertise. Limitations include restricted model scope and dependence on accurate visual interpretation. The results demonstrate the feasibility of structured, workflow-based model generation as a robust foundation for LLM-assisted simulation modelling.

## Metadata
- **Published**: 2026-07-27T10:50:37Z
- **Authors**: Thomas Monks, Alison Harper, Amy Heather, Navonil Mustafee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24259v1)
---
title: A Multi-Domain and Multi-Task Generative Framework with Explicit Task and Domain Conditioning for Cross-Domain Event Extraction
published: 2026-08-24T13:24:24Z
authors: Siting Liang, Omar Adjali, Daniel Sonntag
url: http://arxiv.org/abs/2608.23235v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Multi-Domain and Multi-Task Generative Framework with Explicit Task and Domain Conditioning for Cross-Domain Event Extraction

## Abstract
Event extraction aims to identify event triggers, classify event types, and extract arguments to construct structured event representations. Despite strong in-domain performance, developing models that generalize robustly across domains remains challenging due to variations in contextual expressions and event schemas. Prior unified and multi-task approaches improve in-domain accuracy but exhibit limited flexibility when applied to unseen domains. Even large language model-based methods that provide full event ontologies at inference time often underperform compared to smaller, task-specific fine-tuned models. We propose a unified multi-domain and multi-task training framework that models heterogeneous event schemas within a single model. Our approach introduces domain conditioning signals, jointly with task-specific prompts, enabling dynamic adaptation to dataset-specific schemas without requiring complete event label sets at inference time. The framework supports both pipeline and end-to-end extraction settings, facilitating efficient task- and domain-level transfer. Experiments on diverse event extraction benchmarks demonstrate that our method achieves competitive performance, strong cross-domain generalization, and practical scalability, while preserving domain-specific precision.

## Metadata
- **Published**: 2026-08-24T13:24:24Z
- **Authors**: Siting Liang, Omar Adjali, Daniel Sonntag
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23235v1)
---
title: Valhalla: A Layered Knowledge-State and Service-Governance Framework for Long-Term Scientific Knowledge Work
published: 2026-08-15T12:21:41Z
authors: Yuyang Zheng, Nan Li, Wenxia Deng, Lige Yan, Xiang Li, Si Chen
url: http://arxiv.org/abs/2608.15193v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Valhalla: A Layered Knowledge-State and Service-Governance Framework for Long-Term Scientific Knowledge Work

## Abstract
As large language model (LLM) agents are increasingly adopted in scientific research, external knowledge bases, knowledge graphs, and long-term memory have improved information retrieval and task continuity. However, most structured knowledge systems remain node-centric, representing files, concepts, results, and judgments as nodes and relations in a graph. While suitable for personal knowledge management, such structures often depend on individual organizational practices, limiting knowledge sharing, integration, and reorganization across users. This paper presents Valhalla, a layered knowledge-state and service-governance framework for long-term scientific knowledge work. Valhalla replaces flat graphs with layered encapsulation and stable semantic boundaries through a five-layer File-Resource-Entity-Relationship-Graph (FREG) model. File and Resource preserve source identity and provenance, Entity represents knowledge objects, Relationship captures semantic judgments, and Graph provides task-oriented knowledge views, enabling knowledge states from different researchers to be exchanged and reorganized under a unified structure. We further introduce a Router-Contract-Workflow service-governance architecture, inspired by the microkernel paradigm, to constrain how language models access, modify, and extend knowledge states while maintaining structural consistency and auditable operational boundaries. We implement a Valhalla prototype and validate knowledge ingestion, cross-member integration, and scientific writing support through an antibody-design review task comprising 26 paper resources, 80 knowledge entities, and 92 semantic relations. Rather than proposing a new knowledge-extraction algorithm, Valhalla offers a paradigm for organizing collaborative scientific knowledge, transforming individualized knowledge structures into transferable and reorganizable shared knowledge states.

## Metadata
- **Published**: 2026-08-15T12:21:41Z
- **Authors**: Yuyang Zheng, Nan Li, Wenxia Deng, Lige Yan, Xiang Li, Si Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15193v1)
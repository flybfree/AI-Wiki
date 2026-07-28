---
title: SINT-Flow: Schema Integration using Large Language Model Workflows
published: 2026-07-27T14:28:17Z
authors: Keti Korini, Christian Bizer
url: http://arxiv.org/abs/2607.24492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SINT-Flow: Schema Integration using Large Language Model Workflows

## Abstract
The goal of schema integration is, given a set of input schemata or tables, to derive a global, unified schema that is able to represent the concepts, attributes, and relationships of all input tables in a coherent fashion. This paper presents SINT-Flow, a schema integration framework composed of five LLM-based operators that can be combined into workflows to perform fully automated, end-to-end schema integration. In contrast to existing approaches, SINT-Flow can process denormalized source tables that contain attributes describing multiple entity types. During the schema integration process, these tables are decomposed into separate entity-specific relations. To evaluate SINT-Flow, we introduce SINT-Bench, a schema integration benchmark comprising 10 schema integration tasks consisting of altogether 93 relational tables, including tables that describe multiple types of entities. We evaluate SINT-Flow using GPT-5.2 as well as the open-weight model Qwen-3.6-27B as alternative backbone models. Using these models, SINT-Flow achieves F1 scores of at least 96% for entity-type detection, 85% for attribute detection, and 83% for schema mapping. Furthermore, we perform an ablation study to prove the utility of the applied self-consistency strategy as well as the inclusion of a review loop into the schema matching operator.

## Metadata
- **Published**: 2026-07-27T14:28:17Z
- **Authors**: Keti Korini, Christian Bizer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24492v1)
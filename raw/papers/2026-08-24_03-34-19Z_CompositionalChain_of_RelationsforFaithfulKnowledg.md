---
title: Compositional Chain-of-Relations for Faithful Knowledge Graph Question Answering with Large Language Models
published: 2026-08-24T03:34:19Z
authors: Chenhui Liu, Jianpeng Zhou, Jiahai Wang
url: http://arxiv.org/abs/2608.22762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compositional Chain-of-Relations for Faithful Knowledge Graph Question Answering with Large Language Models

## Abstract
Knowledge graph question answering (KGQA) is a key task for evaluating KG-augmented Large Language Models (LLMs), and complex KGQA that requires multi-hop reasoning is especially challenging. Solving a complex query involves two coupled phases: candidate retrieval, which locates answer candidates over the KG, and constraint handling, which filters these candidates against the query constraints. Faithful reasoning requires grounding both phases in the KG. However, existing agent-based methods ground candidate retrieval through entity-centric exploration, while leaving constraint handling to the LLM's internal knowledge, which leads to two critical limitations. (1) Unreliable entity pruning: entity-centric exploration uses entities as search units and must prune them to a fixed-size subset at each hop. Because entity information in KGs is often incomplete and a fixed-size subset cannot retain all valid entities, such pruning inevitably drops valid entities and ultimately leads to wrong answers. (2) Ungrounded constraint handling: query constraints are resolved from the LLM's internal knowledge rather than the KG, leaving the final answers unverifiable and prone to hallucination. To address these limitations, this paper introduces a relation-centric exploration paradigm, which uses relations rather than entities as search units and thus avoids unreliable entity pruning. Built on this paradigm, this paper proposes Compositional Chain-of-Relations (CCoR), a simple and effective framework that grounds both phases in the KG with two relation chains: a main chain for candidate retrieval and a constraint chain that verifies query constraints through explicit KG exploration. Experiments on four KGQA benchmarks show that CCoR consistently improves accuracy, faithfulness, and efficiency over strong baselines, with more pronounced gains on complex queries.

## Metadata
- **Published**: 2026-08-24T03:34:19Z
- **Authors**: Chenhui Liu, Jianpeng Zhou, Jiahai Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22762v1)
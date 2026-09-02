---
title: Automated Tree Knowledge Graph Construction using Ontology Expansion and Retrieval from Vietnamese History Textbooks
published: 2026-09-01T05:52:50Z
authors: Ket Doan Nguyen, Minh N. H. Nguyen
url: http://arxiv.org/abs/2609.00763v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automated Tree Knowledge Graph Construction using Ontology Expansion and Retrieval from Vietnamese History Textbooks

## Abstract
Hierarchical Knowledge graph (KG)-based retrieval augmented generation (RAG) has emerged as a powerful approach for supporting large language models with structured knowledge. However, there are primary challenges: (i) the lack of methods for automatic KG construction using ontology expansion for low-resource languages such as Vietnamese, (ii) the absence of systematic evaluation for knowledge retrieval strategies leveraging the hierarchical structures. In this paper, we propose an end-to-end pipeline for KG construction and retrieval strategies evaluation. In the KG construction, we employ a three-phase hybrid relation extraction pipeline: intra-batch deduplication via Union-Find, approximate cross-batch search, and LLM extraction with a centroid filter that reduces prompts combined with a five-step dual-LLM validator to prevent bloated ontology. A two-tier architecture consists of unmergeable structural nodes to preserve the document structure and mergeable content nodes. The retrieval evaluation consists of three graph traversal strategies: Top-Down, Horizontal, and Bottom-Up, which are evaluated on a synthetically generated benchmark of 1,210 Vietnamese queries from 109 subgraphs, categorized by five query directions. In this paper, we construct the tree knowledge graph from Vietnamese high school History textbooks (nearly 400 pages) to produce 750 nodes and 4,341 semantic edges with controlled ontology growth from 40 to 41 types. Among experimental graph traversal strategies, the Top-Down strategy with structure surpasses the vector baseline by 4.7 percentage points in NDCG@10. As a result, tree-structural information provides valuable information beyond flat cosine similarity but degrades performance when the query does not require structural context.

## Metadata
- **Published**: 2026-09-01T05:52:50Z
- **Authors**: Ket Doan Nguyen, Minh N. H. Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00763v1)
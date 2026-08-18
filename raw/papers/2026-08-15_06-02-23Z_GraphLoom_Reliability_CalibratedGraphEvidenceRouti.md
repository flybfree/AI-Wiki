---
title: GraphLoom: Reliability-Calibrated Graph Evidence Routing for Multimodal KG-RAG
published: 2026-08-15T06:02:23Z
authors: Zafar Ali, Asad Khan, Aalia Malik, Pavlos Kefalas
url: http://arxiv.org/abs/2608.15056v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GraphLoom: Reliability-Calibrated Graph Evidence Routing for Multimodal KG-RAG

## Abstract
Multimodal retrieval-augmented generation (RAG) systems often rely on long unstructured contexts or aggressively expanded evidence graphs, which can introduce noisy evidence, weaken multi-hop reasoning, and increase unsupported generation. We present GraphLoom, a reliability-calibrated multimodal knowledge-graph RAG framework for compact and faithful evidence routing. Given a question and its associated multimodal input, GraphLoom constructs an instance-level multimodal knowledge graph from grounded scene descriptions, extracted relational triples, and external commonsense knowledge. Instead of injecting all retrieved evidence into the generator, GraphLoom performs reliability-aware subgraph retrieval with bounded expansion and selectively routes high-utility evidence through hierarchical graph memory slots and joint graph-sequence attention in a frozen language model. To improve robustness in complex reasoning settings, GraphLoom further combines interleaved retrieval with budgeted corrective retrieval, enabling adaptive multi-hop evidence refinement under noisy retrieval conditions. We evaluate GraphLoom on ScienceQA, MultiModalQA, and OK-VQA, including large distractor evidence pools that approximate noisy external knowledge retrieval. Experimental results show consistent gains in answer quality and evidence faithfulness over strong multimodal RAG, graph-retrieval, and open-source vision-language baselines, with improved retrieval quality on MultiModalQA and stable performance under noisy evidence pools. Additional analyses using MiniCheck-based verification, human evaluation, and latency profiling show that reliability-calibrated graph evidence routing provides an effective alternative to long-context multimodal evidence injection.

## Metadata
- **Published**: 2026-08-15T06:02:23Z
- **Authors**: Zafar Ali, Asad Khan, Aalia Malik, Pavlos Kefalas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15056v1)
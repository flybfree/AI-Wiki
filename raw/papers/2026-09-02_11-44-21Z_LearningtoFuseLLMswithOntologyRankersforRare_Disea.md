---
title: Learning to Fuse LLMs with Ontology Rankers for Rare-Disease Diagnosis
published: 2026-09-02T11:44:21Z
authors: Zhaoyang Jiang, Zhizhong Fu, Yunsoo Kim, Zicheng Li, Xuanqi Peng, Fei Teng, Jiacong Mi, Honghan Wu
url: http://arxiv.org/abs/2609.02473v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Fuse LLMs with Ontology Rankers for Rare-Disease Diagnosis

## Abstract
Ontology rankers remain useful for rare-disease diagnosis because each candidate can be traced to matched patient phenotypes. Large language models (LLMs) can generate differential diagnoses from the same patient description, but their predictions lack an equally clear evidence trail. Rather than asking which system should replace the other, we ask whether an LLM can improve the ranker without giving up its evidence. Our behavior-based fusion model examines the two ranked lists, their agreement, and the ontology support behind each candidate, and learns how much to rely on each system for the individual case. Before comparison, we remove a documented test-set leakage pathway caused by benchmark cases and ontology annotations being derived from the same publications. Across eight open LLMs, fusion improves Phenomizer Recall@1 by 7.86 percentage points on Phenopacket Store and 20.18 points on RAMEDIS. When paired with DeepSeek-V4-Flash through an API, a fusion model trained only on the other LLMs improves Recall@1 from 0.1657 to 0.2176, a 5.19-point gain, without retraining. For 90.8% of correct fused diagnoses, the disease retains candidate-level ontology evidence that can be inspected. These results show that LLMs can strengthen an established diagnostic tool without discarding the structured evidence that makes it useful.

## Metadata
- **Published**: 2026-09-02T11:44:21Z
- **Authors**: Zhaoyang Jiang, Zhizhong Fu, Yunsoo Kim, Zicheng Li, Xuanqi Peng, Fei Teng, Jiacong Mi, Honghan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02473v1)
---
title: Beyond Top-$k$ Skill Retrieval: Diversity-Aware Skill Routing for LLM Agents
published: 2026-09-05T02:39:28Z
authors: Wang Wei, Tiankai Yang, Samyadeep Basu, Hongjie Chen, Yue Zhao, Zhengzhong Tu, Xiyang Hu, Franck Dernoncourt, Ryan A. Rossi, Hoda Eldardiry
url: http://arxiv.org/abs/2609.05824v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Top-$k$ Skill Retrieval: Diversity-Aware Skill Routing for LLM Agents

## Abstract
Large language model (LLM) agents increasingly rely on external skills, but routing user requests over large skill registries is difficult because many skills are functionally redundant while complex tasks often require complementary skill sets. Existing skill routers typically rank candidates independently by query relevance, which can waste context budget on redundant skills. We propose Diverse Skill Routing (DSR), a diversity-aware reranking framework that uses a Determinantal Point Process to balance relevance and non-redundancy. DSR introduces a query-residual diversity kernel that penalizes redundant skill overlap while reducing penalties caused only by shared query relevance. On the SkillRouter benchmark, DSR improves recall and full coverage over a strong pointwise reranking baseline, with larger gains on multi-skill queries. These results suggest that skill routing should be treated not only as relevance ranking, but also as complementary set selection.

## Metadata
- **Published**: 2026-09-05T02:39:28Z
- **Authors**: Wang Wei, Tiankai Yang, Samyadeep Basu, Hongjie Chen, Yue Zhao, Zhengzhong Tu, Xiyang Hu, Franck Dernoncourt, Ryan A. Rossi, Hoda Eldardiry
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05824v1)
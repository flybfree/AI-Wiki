---
title: From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-Term Dialogue
published: 2026-10-08T06:21:45Z
authors: Zirui Liao, Zhengxian Wu, Zhuohong Chen, Yunyao Yu, Xiaoyu Liu, Yifan Xu, Haoqian Wang
url: http://arxiv.org/abs/2610.11314v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-Term Dialogue

## Abstract
Large Language Models (LLMs) serving as long-term dialogue agents require memory systems that support reliable reasoning over extended interactions. However, existing Retrieval-Augmented Generation (RAG) frameworks typically treat memory as passive storage, making it difficult to distinguish source-attributed beliefs from unattributed event/fact records and to connect evidence dispersed across sessions. We introduce CogMem, a cognitive memory architecture based on the PEC$^2$F (Person-Event-Concept-Claim-Fact) graph schema. Dedicated Claim nodes preserve the source and target of subjective statements, while Fact and Event nodes represent semantic and episodic knowledge. Dialogue turns are incrementally converted into provenance-aware graph records, consolidated into higher-level facts, and reconciled into temporally scoped Claim views when the same source provides conflicting updates. For retrieval, a rule-based controller driven by LLM intent parsing composes four deterministic graph operators---anchoring, traversal, intersection, and evidence grounding---to reconstruct query-relevant context. Experiments on LoCoMo and LongMemEval show strong performance, especially on multi-hop, temporal, and knowledge-update tasks. Ablations and a semantic-collapse probe support complementary contributions from epistemic separation, consolidation, and agentic retrieval. Code: https://github.com/Silent-Rain02/CogMem.

## Metadata
- **Published**: 2026-10-08T06:21:45Z
- **Authors**: Zirui Liao, Zhengxian Wu, Zhuohong Chen, Yunyao Yu, Xiaoyu Liu, Yifan Xu, Haoqian Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11314v1)
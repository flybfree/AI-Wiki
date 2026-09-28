---
title: Meet, Compare, or Abstain: LatWeave for Deterministic Multi-Hop Question Answering on Knowledge Lattices
published: 2026-09-23T01:45:23Z
authors: Yuze Ren, Shaoheng Fan, Tao Wang, Yabo Yan, Han Han
url: http://arxiv.org/abs/2609.27225v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Meet, Compare, or Abstain: LatWeave for Deterministic Multi-Hop Question Answering on Knowledge Lattices

## Abstract
Probabilistic question-answering systems -- whether large language models (LLMs) themselves, retrieval-augmented generation (RAG), or trained multi-hop retrievers -- conflate "what is known" and "how to reason" into a single probabilistic computation: hallucination cannot be eradicated, evidence chains cannot be audited, and the system answers even when it does not know. We present LatWeave, which organizes knowledge into a multidimensional knowledge lattice and compiles multi-hop QA into three deterministic operators -- meet (constraint intersection), compare (lattice-order comparison), and abstain (structural abstention); LLMs appear only on the construction side (one-shot extraction) and the query-planning side, while the answer-generation path is zero-LLM, zero-task-training, and auditable end to end -- so that question answering over Web-published knowledge becomes reproducible item by item. Rather than claiming across-the-board SOTA, we characterize the operating envelope of this paradigm on six public benchmarks: when knowledge is complete (MetaQA, 39,093 questions) meet chains are near-lossless over three hops (any-hit 0.9975, on par with fully supervised KBQA); on templated multi-hop home ground (2WikiMultihopQA held-out n=1,258) EM 0.865, well above published structure-augmented RAG reproductions; on open-text deep composition (MuSiQue) and extraction-coverage gaps (HotpotQA) we report degradation honestly and attribute it to causes outside the lattice-algebra layer; and when information is incomplete (IIRC) we achieve structural abstention with abstain accuracy 0.971 and leak rate 0.029. Within the operating envelope, deterministic execution pays no performance penalty, and every step on the answer path can be recomputed -- precisely the source of end-to-end auditability.

## Metadata
- **Published**: 2026-09-23T01:45:23Z
- **Authors**: Yuze Ren, Shaoheng Fan, Tao Wang, Yabo Yan, Han Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27225v1)
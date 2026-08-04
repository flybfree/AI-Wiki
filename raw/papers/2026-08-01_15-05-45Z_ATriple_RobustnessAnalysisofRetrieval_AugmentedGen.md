---
title: A Triple-Robustness Analysis of Retrieval-Augmented Generation for Multi-Hop Requirements Traceability
published: 2026-08-01T15:05:45Z
authors: Meftun Akarsu, Burak Özdemir, Doğancan Büyükçolak, Recep Kaan Karaman
url: http://arxiv.org/abs/2608.00705v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Triple-Robustness Analysis of Retrieval-Augmented Generation for Multi-Hop Requirements Traceability

## Abstract
Reported verdicts on GraphRAG versus vector RAG disagree, and the evidence is typically tied to a single corpus, embedder, and judge -- and, we show, to where citation quality is measured. We present a triple-robustness analysis that holds a five-pipeline architecture matrix fixed and varies embedder (local e5-small vs. Azure text-embedding-3-small), corpus (DO-178C typed-edge requirements vs. Wikipedia paragraph chains via MuSiQue), and judge (paired GPT-5.4 x GPT-4.1 on both corpora), over 2x4,440 main-matrix runs, 600 cross-corpus runs, and over 5,000 faithfulness judgments. (C2a) GraphRAG's graph walk floods the context window at precision 0.12-0.23, but the synthesizer cites selectively at precision 0.48-0.65; scoring the retrieved set as the attribution set inverts the architecture ranking, which reconciles part of the disagreement in prior reports. (C1) Answer-level citation winners are corpus- and stratum-conditional but embedder-robust: GraphRAG ties vanilla on short-hop DO-178C queries and wins every MuSiQue stratum, while agentic pipelines lead only on 3+-hop requirements queries. (C2b) Faithfulness is corpus-conditional: on DO-178C it declines with hop distance (trend p<0.05 in three of four judge x embedder combinations); on Wikipedia chains neither judge shows a collapse. (C3) Single-judge LLM faithfulness is fragile to retrieval state: GPT-5.4's self-kappa across embedders is 0.137 (41% verdict change) against a same-day test-retest floor of 0.76, and re-judging frozen inputs eleven weeks later gives kappa <= 0.14 for both judges. A learned router on dense embeddings alone reaches macro-F1 0.86 on hop classification (C4). We argue that RAG architecture claims should be tested at this level of robustness -- including robustness to the citation-measurement point -- before they are trusted.

## Metadata
- **Published**: 2026-08-01T15:05:45Z
- **Authors**: Meftun Akarsu, Burak Özdemir, Doğancan Büyükçolak, Recep Kaan Karaman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00705v1)
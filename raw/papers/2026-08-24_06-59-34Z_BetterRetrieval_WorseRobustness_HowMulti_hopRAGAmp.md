---
title: Better Retrieval, Worse Robustness:How Multi-hop RAG Amplifies Upstream ASR Errors
published: 2026-08-24T06:59:34Z
authors: Zhenghua Bao
url: http://arxiv.org/abs/2608.22872v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Better Retrieval, Worse Robustness:How Multi-hop RAG Amplifies Upstream ASR Errors

## Abstract
Speech-based applications pass spoken queries through automatic speech recognition (ASR) before any retrieval module, so ASR errors enter the pipeline as a fixed upstream constraint. We empirically test whether two extensions to standard retrieval-augmented generation (RAG), entity-graph linking and iterative reformulation, absorb or amplify these errors. Using four English accents synthesized through neural TTS, we evaluate four RAG configurations on three multi-hop QA benchmarks (HotpotQA, 2WikiMultiHopQA and MuSiQue) against a clean-text oracle. Although the structurally richer configurations generally retain higher absolute F1 under ASR input, both extensions amplify the error: the F1 gap from clean text to the highest-WER accent is 36-67% larger under their combination than under naive dense retrieval, on all three benchmarks. The dominant failure mode is corruption of one or more query entities, accounting for 87-96% of degradation cases on 2WikiMultiHopQA across all four methods. Two lightweight surface-form mitigations leave most of the gap intact, indicating that downstream retrieval structure amplifies remaining entity errors. We release code and data at https://github.com/ZhenghuaBao/spoken-multihop-rag .

## Metadata
- **Published**: 2026-08-24T06:59:34Z
- **Authors**: Zhenghua Bao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22872v1)
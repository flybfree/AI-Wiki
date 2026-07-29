---
title: Every Time I Hire a Linguist, Inference Costs Go Down: On Linguistic Rules as Effective Prompt Compressors
published: 2026-07-28T06:33:27Z
authors: Jianfei Ma, Zhaoxin Feng, Emmanuele Chersoni, Si Chen
url: http://arxiv.org/abs/2607.25335v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Every Time I Hire a Linguist, Inference Costs Go Down: On Linguistic Rules as Effective Prompt Compressors

## Abstract
Prompt compression shortens LLM input to reduce inference cost, yet existing methods score token importance through LM forward passes. It remains questionable whether such nuanced, costly token selection is necessary. Compression requires identifying informative content, a problem that linguistic research has long addressed through cues that can be operationalized as deterministic rules. We therefore ask: can \textbf{linguistic rules alone} serve as effective prompt compressors, without LM-based scoring at compression time?   To address this, we conduct offline evolutionary search over lexical, syntactic, semantic, and discourse seeds to find competitive rule combinations. The resulting linguistic compressor requires no LM forward pass at deployment and uses only CPU-side processing for compression. We evaluate it with a dual-path protocol to balance compression quality and reconstruction fidelity.   Across short passages, multi-document reasoning, and dialogue-memory QA datasets, evolved compressors achieve performance similar to that of recent advanced prompt-compression strategies. Performance is strongest under light-to-moderate compression and degrades as compression becomes more aggressive, while the Direct and Reconstruction paths exhibit distinct patterns. Evolutionary analysis reveals that effective compression fuses signals across linguistic levels and, as the compression ratio increases, rules shift from token pruning to sentence extraction.

## Metadata
- **Published**: 2026-07-28T06:33:27Z
- **Authors**: Jianfei Ma, Zhaoxin Feng, Emmanuele Chersoni, Si Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25335v1)
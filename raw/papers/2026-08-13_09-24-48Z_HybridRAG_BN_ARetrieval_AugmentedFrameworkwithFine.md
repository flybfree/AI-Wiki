---
title: HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification for Bangla KBQA
published: 2026-08-13T09:24:48Z
authors: Rathijit Aich, Nirjhar Das, Mahfuzulhoq Chowdhury
url: http://arxiv.org/abs/2608.13004v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification for Bangla KBQA

## Abstract
Knowledge-base question answering (KBQA) systems rely on effective retrieval and reasoning mechanisms to generate accurate answers from external knowledge sources. However, developing reliable KBQA systems for low-resource languages such as Bangla remains challenging due to limited retrieval-focused research, scarce language resources, and difficulties in grounding generated responses in external knowledge. In this work, we propose HybridRAG-BN, a retrieval-augmented framework for Bangla KBQA that integrates hybrid retrieval using BM25 and BGE-M3, answer generation using the GGUF version of Gemma-4-31B-Instruct, and a LoRA-fine-tuned Gemma-4-31B-Instruct model for answer verification and refinement. To further improve robustness, the framework incorporates a post-processing stage that addresses unresolved cases through fallback answer replacement and DuckDuckGo-assisted retrieval. Experimental results demonstrate the effectiveness of the proposed framework, achieving token-level F1 scores of 0.71654 and 0.72912 on the public and private leaderboards, respectively, securing first place in the competition.

## Metadata
- **Published**: 2026-08-13T09:24:48Z
- **Authors**: Rathijit Aich, Nirjhar Das, Mahfuzulhoq Chowdhury
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13004v1)
---
title: MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
published: 2026-07-08T03:51:37Z
authors: Ruilin Tong, Dong Gong
url: http://arxiv.org/abs/2607.06974v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning

## Abstract
Large language models (LLMs) increasingly improve their reasoning at test time via additional computation, yet most existing works treat each problem in isolation. When problems arrive sequentially, accumulating reusable experience across them can further improve performance. Existing memory-based methods either store whole-solution templates that generalize poorly to novel problems or use heuristic step-level selection that is not optimized for final-answer correctness. Learning selection policies requires large-scale training data and fixed action spaces, making such approaches unsuitable for test-time settings where memory expands incrementally and only limited supervision is available. We propose MILES (Modular Instruction Memory with LEarnable Selection for self-improving LLM reasoning), a framework that dynamically expands step-wise memory and applies correctness-optimized memory composition under realistic test-time constraints. MILES maintains modular memory units consisting of asymmetric pairs of sub-goal embeddings and sub-instructions, each associated with a learnable selection head. This memory structure enables a coarse-to-fine retrieval mechanism: The coarse level enables memory expansion and collects supervision for training selection heads from confident samples, while the fine stage applies learned selection heads to rerank coarse-level candidates and guide reasoning for uncertain samples. MILES consistently matches or outperforms prior methods while achieving superior accuracy-efficiency tradeoffs. Extensive experiments demonstrate its effectiveness, robustness, and transferability.

## Metadata
- **Published**: 2026-07-08T03:51:37Z
- **Authors**: Ruilin Tong, Dong Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.06974v1)
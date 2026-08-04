---
title: GraphIR: Architecture-Level Search States for LLM-Guided Neural Architecture Evolution
published: 2026-08-03T03:06:58Z
authors: Zhen Liu, Wanqi Zhou, Shuanghao Bai, Yuhan Liu, Jinjun Wang, Jingwen Fu
url: http://arxiv.org/abs/2608.01633v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GraphIR: Architecture-Level Search States for LLM-Guided Neural Architecture Evolution

## Abstract
Large language models (LLMs) enable neural architecture search (NAS) directly over executable neural network programs. However, code-level flexibility does not provide the architecture state needed for effective mutation: LLMs must infer tensor dependencies, editable components, and compatibility constraints from implementation details. To address this representation mismatch, we propose GraphIR, an architecture-aware intermediate representation that supplements executable programs with a mutation-aligned candidate state. GraphIR organizes each candidate through three complementary views: a computation skeleton describing tensor flow, a mutation surface exposing editable modules and operations, and a validity envelope capturing interface contracts, propagated shapes, and downstream dependencies. To evaluate our method, we construct NAS-Dependency, a 120-question benchmark covering six complementary dependency-reasoning dimensions. The diagnostic shows that GraphIR is particularly effective at identifying exact producer occurrences, tracing dependency propagation, and diagnosing interface and failure risks. Across six downstream benchmarks including CLRS, GraphIR achieves the best overall search performance while maintaining comparable model size and favorable end-to-end NAS efficiency when integrated into OpenEvolve. These results show that a mutation-oriented architecture state provides an effective interface between executable neural programs and LLM-guided architecture evolution.

## Metadata
- **Published**: 2026-08-03T03:06:58Z
- **Authors**: Zhen Liu, Wanqi Zhou, Shuanghao Bai, Yuhan Liu, Jinjun Wang, Jingwen Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01633v1)
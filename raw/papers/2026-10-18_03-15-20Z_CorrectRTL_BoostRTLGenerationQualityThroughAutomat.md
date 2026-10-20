---
title: CorrectRTL: Boost RTL Generation Quality Through Automated Self-Correction with Instruction Decomposition
published: 2026-10-18T03:15:20Z
authors: Jing Wang, Shang Liu, Hangan Zhou, Wenji Fang, Yuchao Wu, Yugao Zhu, Zhiyao Xie
url: http://arxiv.org/abs/2610.24977v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CorrectRTL: Boost RTL Generation Quality Through Automated Self-Correction with Instruction Decomposition

## Abstract
Large language models (LLMs) have shown strong promise in specification-to-RTL generation. Among the explorations, the self-correction paradigm has significantly advanced LLM-based RTL generation. However, two challenges limit further progress. Existing benchmarks are saturated by advanced LLMs, leaving little room to evaluate the agentic self-correction framework. The monolithic self-correction paradigm rewrites the entire design at once, where LLMs are susceptible to error confusion and corruption of originally correct code. To address the benchmark challenge, we contribute ScaleBench, a more challenging benchmark of 200 complex RTL designs. To address the challenge in methodology, we propose CorrectRTL, an agentic framework that realizes a new decompose-then-correct paradigm, in which the LLM agent explicitly decouples scaffold construction from detailed implementation. CorrectRTL contributes three core techniques: (1)~\emph{Structure-oriented decomposition}, (2)~\emph{Snippet-based RAG}, and (3)~\emph{SVA-based self-correction}. On ScaleBench, CorrectRTL improves Pass@1 from 20.5% to 49.0% (+28.5%). On VerilogEval, CorrectRTL achieves up to 96.1% Pass@1, demonstrating consistent improvements across both simple and complex designs.

## Metadata
- **Published**: 2026-10-18T03:15:20Z
- **Authors**: Jing Wang, Shang Liu, Hangan Zhou, Wenji Fang, Yuchao Wu, Yugao Zhu, Zhiyao Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24977v1)
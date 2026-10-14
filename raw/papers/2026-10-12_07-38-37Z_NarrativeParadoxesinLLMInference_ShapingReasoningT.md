---
title: Narrative Paradoxes in LLM Inference: Shaping Reasoning Trajectories toward Misalignment
published: 2026-10-12T07:38:37Z
authors: Haoming Yang, Ke Ma, Yangbangyan Jiang, Ligong Zhang, Xiaojun Jia, Longtao Huang, Yingfei Sun, Qianqian Xu, Qingming Huang
url: http://arxiv.org/abs/2610.16312v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Narrative Paradoxes in LLM Inference: Shaping Reasoning Trajectories toward Misalignment

## Abstract
Explicit reasoning in large language models (LLMs) is often associated with reliability, yet it can still pose risks when a model infers harmful goals under a benign context. We identify a distinct challenge: ensuring the safety of the \emph{multi-step reasoning process} itself, where locally coherent steps may still lead to globally harmful outcomes. To explore this vulnerability, we propose PDRA (Paradox-driven Reasoning-based Attack), a novel attack method that programs a harmful reasoning trajectory. PDRA first constructs a paradoxical narrative core by pairing a malicious actor (e.g., a terrorist) with a benign task (e.g., writing a safety bulletin). It then embeds this core into a structured analytical framework that forces the model through a mandatory three-stage analysis -- surface purpose, latent intent, and operational reconstruction -- guiding it to produce detailed harmful content while maintaining narrative coherence. Mechanistically, we show PDRA steers the model's internal representations away from refusal-related patterns, suppressing safety-triggering lexicons while activating planning-oriented terms. Empirically, PDRA achieves state-of-the-art attack success rates across diverse LLMs with high efficiency. \textcolor{red}{\textbf{Warning:} This paper may contain sensitive content.}

## Metadata
- **Published**: 2026-10-12T07:38:37Z
- **Authors**: Haoming Yang, Ke Ma, Yangbangyan Jiang, Ligong Zhang, Xiaojun Jia, Longtao Huang, Yingfei Sun, Qianqian Xu, Qingming Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16312v1)
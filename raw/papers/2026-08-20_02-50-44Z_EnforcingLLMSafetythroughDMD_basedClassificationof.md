---
title: Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics
published: 2026-08-20T02:50:44Z
authors: Mohamed Akrout, Olivera Kotevska, Dan Wilson
url: http://arxiv.org/abs/2608.19579v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics

## Abstract
Large Language Models (LLMs) are increasingly deployed in high-stakes applications, yet their tendency to generate toxic, harmful, or policy-violating content poses significant risks. Detecting these unsafe outputs efficiently in a black-box manner remains an open challenge. In this paper, we extend a recently proposed dynamical systems framework designed for hallucination detection to LLM safety classification. By projecting both prompts and responses into high-dimensional embedding spaces and fitting separate Koopman-based predictive models for safe and unsafe regimes, we classify new outputs using a new differential residual score that compares prediction errors of the safe and unsafe regimes. A key contribution is the incorporation of the prompt and response embedding dynamics, yielding fitted Koopman operators that capture crucial interaction patterns. We evaluate our black-box method across three safety benchmarks using three embedding models. Our results show that incorporating prompt embeddings yields consistent improvements, particularly for interaction-dependent violations when paired with causal decoders (e.g., in Llama-3), while response-only violations benefit more from dense semantic embedding representations. These findings opens the door for using dynamical systems to analyze AI systems rather than the dominant paradigm of using AI to model dynamical systems.

## Metadata
- **Published**: 2026-08-20T02:50:44Z
- **Authors**: Mohamed Akrout, Olivera Kotevska, Dan Wilson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19579v1)
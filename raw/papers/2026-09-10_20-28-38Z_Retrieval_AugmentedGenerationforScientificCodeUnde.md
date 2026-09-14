---
title: Retrieval-Augmented Generation for Scientific Code Understanding
published: 2026-09-10T20:28:38Z
authors: Aaron Nobile, Andreas Adelmann, Mohsen Sadr
url: http://arxiv.org/abs/2609.12190v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval-Augmented Generation for Scientific Code Understanding

## Abstract
Large language models have become central to modern coding assistants, but state-of-the-art systems such as Claude Code or Codex rely on very large, cloud-hosted models with significant computational cost and data-privacy implications. This work investigates whether a useful, fully local coding agent can be built around small open-source models by shifting the computational burden away from inference. We develop a Retrieval-Augmented Generation (RAG) system for scientific code understanding that strictly separates an expensive offline ingestion stage parsing, structural graph construction, LLM-generated entity explanations, and embedding from a lightweight online answering stage. The system is evaluated on a 100-question benchmark spanning eleven categories over the IPPL scientific codebase written in C++, with answers scored by an independent frontier model as the judge. Across seven answering models, we find that model family and retrieval quality matter more than parameter count, i.e. a 9B model achieves the highest average score (0.795), outperforming both larger models within our pipeline and the same models embedded in the Claude Code retrieval architecture. The results indicate that front-loading code understanding into a reusable, codebase-specialised vector store enables small local models to deliver grounded and repository-specific answers, making the agent well suited as a privacy-preserving development tool for in-house scientific codebases.

## Metadata
- **Published**: 2026-09-10T20:28:38Z
- **Authors**: Aaron Nobile, Andreas Adelmann, Mohsen Sadr
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12190v1)
---
title: S3C-LLM: Skill-Code Guided Agentic Language Models for Spectrum-to-Structure Elucidation
published: 2026-08-31T14:55:32Z
authors: Xuanle Zhao, Xinyuan Cai, Xiang Cheng, Bo Xu
url: http://arxiv.org/abs/2608.30910v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# S3C-LLM: Skill-Code Guided Agentic Language Models for Spectrum-to-Structure Elucidation

## Abstract
Spectroscopic structure elucidation is central to molecular analysis, but recent Large Language Model (LLM)-based methods mostly formulate it as direct spectrum-to-SMILES generation. Although this paradigm can leverage paired spectral data, it does not explicitly model the analytical workflow used by spectroscopists, such as diagnostic peak interpretation, fragment reasoning, formula constraints, and chemical consistency checking. In this paper, we introduce S3C-LLM, a skill-guided and code-grounded agentic LLM for spectrum-to-structure elucidation. Rather than directly predicting a molecule, S3C-LLM retrieves modality-specific spectroscopy skills, executes analysis code to instantiate these skills on the input spectra, and integrates the resulting peak-level evidence and formula constraints before generating SMILES. Specifically, we contribute a self-evolving spectroscopy skill library, a thinking-augmented skill-code trajectory construction pipeline, and a two-stage training strategy that teaches Qwen3-4B through supervised fine-tuning (SFT) followed by our proposed step-level reinforcement learning (RL). Experiments on diverse benchmarks show that S3C-LLM consistently outperforms current general LLMs and spectrum-specific models across spectra, while using less than 1/10th of SpectraLLM's training corpus.

## Metadata
- **Published**: 2026-08-31T14:55:32Z
- **Authors**: Xuanle Zhao, Xinyuan Cai, Xiang Cheng, Bo Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30910v1)
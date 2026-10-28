---
title: Can LLMs Reliably Grade Olympiad Proofs? A Study of Mathematical Verification with LLMs
published: 2026-10-27T07:28:08Z
authors: Azim Ospanov, Zijin Feng, Ding Ding, Chengwu Liu, Haoli Bai, Jiacheng Sun, Lifeng Shang, Farzan Farnia
url: http://arxiv.org/abs/2610.36767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can LLMs Reliably Grade Olympiad Proofs? A Study of Mathematical Verification with LLMs

## Abstract
Large Language Models (LLMs) have made remarkable progress on solving competition-level mathematics, yet their ability to verify natural-language mathematical proofs remains relatively underexplored. This gap is especially pronounced for Olympiad-level proofs, which require meticulous assessment of each claim in a long reasoning chain. Current proof verification thus primarily relies on expert inspection, which is costly to scale. In this paper, we present a systematic study of LLM-based verification in this setting. Specifically, we introduce a human-curated dataset of USAMO 2025 candidate solutions with expert grading, and conduct a broad evaluation of existing LLM verifiers across frontier models. We also propose TROJAN, an iterative self-critique pipeline for generating high-fidelity adversarial proofs at scale. Our comprehensive evaluation covers 20 models spanning seven metrics, two prompt styles, three inference methods, and three prompt templates, showing that state-of-the-art models still leave considerable room for improvement. To narrow this gap, we propose MABGrader, a Multi-Armed Bandit framework that reframes grading as arm selection over the discrete score space. MABGrader outperforms the SOTA ProofGrader by 26.4% in Quadratic Weighted Kappa and reduces grading error by 14%. Code and dataset are available at https://github.com/aziksh-ospanov/TROJAN.

## Metadata
- **Published**: 2026-10-27T07:28:08Z
- **Authors**: Azim Ospanov, Zijin Feng, Ding Ding, Chengwu Liu, Haoli Bai, Jiacheng Sun, Lifeng Shang, Farzan Farnia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36767v1)
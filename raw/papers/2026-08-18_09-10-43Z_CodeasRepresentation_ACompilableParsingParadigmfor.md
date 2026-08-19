---
title: Code as Representation: A Compilable Parsing Paradigm for Academic Documents
published: 2026-08-18T09:10:43Z
authors: Rihui Jin, Jun Wang, chengyuan zhu, Liang Mingyu, Yue Gao, Li Yunxuan, Kuicai Dong, Guilin Qi, Lin Ren, Yongrui Chen, Xinbang Dai, Jiaqi Li, Tongtong Wu, Gholamreza Haffari
url: http://arxiv.org/abs/2608.17550v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Code as Representation: A Compilable Parsing Paradigm for Academic Documents

## Abstract
Academic papers are a primary carrier of scientific knowledge, yet most of this knowledge remains locked in PDFs that are optimized for human reading rather than machine use. For Multimodal Large Language Models (MLLMs), the core challenge is not only perception, but representation: scientific pages interleave text with Structured Academic Elements (SAEs) such as tables, formulas, charts, and pseudocode, whose structure, data, and logic are poorly preserved by common surrogates like Markdown. We therefore propose Compilable Academic Document Parsing (CADP), a paradigm that reconstructs a full page as contextual \LaTeX{} plus executable Python, so that structure-preserving elements and executable chart representations can be reconstructed, recompiled, and directly verified against the source page. To support this setting, we introduce CADP-Bench, an expert-verified benchmark of full academic pages containing tightly coupled text and multiple SAE types, evaluated through a re-injection compilation protocol. We further study current capabilities using SOTA MLLMs and an exploratory multi-agent baseline that incorporates common agentic techniques. Results show that even frontier models still struggle to produce high-fidelity executable reconstructions, highlighting substantial room for improvement in structure-aware scientific document parsing. CADP-Bench is released for future research.

## Metadata
- **Published**: 2026-08-18T09:10:43Z
- **Authors**: Rihui Jin, Jun Wang, chengyuan zhu, Liang Mingyu, Yue Gao, Li Yunxuan, Kuicai Dong, Guilin Qi, Lin Ren, Yongrui Chen, Xinbang Dai, Jiaqi Li, Tongtong Wu, Gholamreza Haffari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17550v1)
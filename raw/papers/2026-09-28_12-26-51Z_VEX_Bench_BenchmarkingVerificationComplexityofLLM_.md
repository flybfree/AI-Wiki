---
title: VEX-Bench: Benchmarking Verification Complexity of LLM-Generated Misinformation
published: 2026-09-28T12:26:51Z
authors: Hanxun Huang, Yutao Wu, Qizhou Wang, Silvia Montaña-Niño, Yige Li, Xiang Zheng, Elif Buse Doyuran, Phoebe Matich, Xiao Liu, Xingjun Ma, Sarah Erfani, Christopher Leckie
url: http://arxiv.org/abs/2609.35028v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VEX-Bench: Benchmarking Verification Complexity of LLM-Generated Misinformation

## Abstract
Large language models (LLMs) have made misinformation inexpensive to produce but not to verify, creating a growing asymmetry in the information ecosystem. Under tight time, labor, and budget constraints, media organizations, platforms, and fact-checkers rely on screening to prioritize which content to verify. We introduce VEX-Bench, a unified benchmark for evaluating the verification complexity of LLM-generated misinformation, as perceived during screening, across models and generation methods. Verification complexity is assessed along multiple dimensions derived from journalistic and fact-checking practices, capturing checkability, harm potential, source credibility signals, imposter legitimacy, and expected verification effort. We define the VEX score as an integrated measure combining elicitation yield and verification complexity to quantify how generated content consumes limited verification capacity. We construct a benchmark spanning two misinformation categories, 6 high-stakes domains, and 60 real-world topics, and evaluate 7 frontier LLMs and 7 generation methods, yielding 5{,}880 articles. We employ an LLM-as-judge for scalable evaluation and validate it using content-analysis methodology, including ordinal Krippendorff $α$ for inter-annotator reliability, complemented by fact-checking agents for verification. Our findings show that no single method dominates all dimensions, underscoring the need for multi-dimensional evaluation. LLMs can generate high-VEX misinformation at 3$\times$ to 169$\times$ lower cost than agent-based verification. Such content is often prioritized during screening, consuming scarce verification resources and introducing a systematic risk of misallocation in resource-constrained verification systems. The code is publicly available in our \href{https://github.com/HanxunH/VEX-Bench}{GitHub repository}.

## Metadata
- **Published**: 2026-09-28T12:26:51Z
- **Authors**: Hanxun Huang, Yutao Wu, Qizhou Wang, Silvia Montaña-Niño, Yige Li, Xiang Zheng, Elif Buse Doyuran, Phoebe Matich, Xiao Liu, Xingjun Ma, Sarah Erfani, Christopher Leckie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35028v1)
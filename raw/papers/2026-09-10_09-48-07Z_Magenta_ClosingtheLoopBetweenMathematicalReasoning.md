---
title: Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification
published: 2026-09-10T09:48:07Z
authors: Joshua Ong Jun Leang, Haonan Li, Zheng Zhao, Xinyi Shang, Wenda Li, Zhengzhong Liu, Erix Xing, Shay Cohen, Eleonora Giunchiglia
url: http://arxiv.org/abs/2609.11319v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification

## Abstract
Most of mathematical knowledge has been communicated through so-called informal use of mathematics and natural language. With large language models (LLMs) being highly adept in using natural language, they achieve strong performance, yet not perfect, in informal mathematical reasoning. Restraining LLMs to informal reasoning misses out on the opportunity to use the discrete verification abilities that machines offer through machine-checkable proofs. In this paper, we bridge the gap between informal and formal reasoning by integrating Lean signals into the informal reasoning process. We introduce Magenta, a training-free agentic pipeline that, given only a natural-language problem, produces an answer, expresses it as a Lean 4 statement, and constructs a machine-checked proof. A statement judge verifies whether the formalisation preserves the original problem, while an error-attribution judge routes failed attempts either to mathematical re-derivation or local Lean repair. Magenta achieves 100% accuracy across all evaluated olympiad benchmarks, including AIME 2025, AIME 2026, and HMMT February 2026. When paired with the open-weight K2-Horizon-7B reasoner, it solves all six IMO 2026 problems. Our analysis shows that statement adjudication is essential for preventing false certificates and that feedback-guided correction outperforms independent resampling on difficult problems.

## Metadata
- **Published**: 2026-09-10T09:48:07Z
- **Authors**: Joshua Ong Jun Leang, Haonan Li, Zheng Zhao, Xinyi Shang, Wenda Li, Zhengzhong Liu, Erix Xing, Shay Cohen, Eleonora Giunchiglia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11319v1)
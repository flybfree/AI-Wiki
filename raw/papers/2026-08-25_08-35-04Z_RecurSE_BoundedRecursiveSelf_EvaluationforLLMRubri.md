---
title: RecurSE: Bounded Recursive Self-Evaluation for LLM Rubric Judges
published: 2026-08-25T08:35:04Z
authors: Kaiyuan Liu, Ziyuan Zhuang, Rongxiang Weng, Jieping Ye
url: http://arxiv.org/abs/2608.24231v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RecurSE: Bounded Recursive Self-Evaluation for LLM Rubric Judges

## Abstract
LLM-as-judge is essential for evaluating open-ended text and steering post-training, yet improving the judge itself typically relies on expensive annotations, reward models, or distillation from stronger teachers. In this work, we eliminate external gold supervision from the RL training reward: the model's own evaluative capability generates learning signals for its optimization -- a closed-loop setting of bounded recursive self-improvement (RSI) termed Recursive Self-Evaluation (RecurSE). We study two central questions: when can self-improvement occur, and when must it stop? First, RecurSE pairs a trainable judge evaluating candidate responses under per-rule rubrics (Pass 1) with a synchronized policy-copy checker that audits the judge's reasoning against meta-rubrics to supply a scalar process reward (Pass 2). To enable learning, interface decoupling structurally isolates the checker's scalar score from the judge's verdict tokens, eliminating a degenerative token-copying shortcut that inflates self-assigned rewards. Second, because unanchored recursive learning is inherently bounded, Pairwise Advantage Validity (PAV) serves as an unbiased validation monitor that jointly tracks judge accuracy and checker fidelity to reliably identify the optimal early-stopping window. Across Qwen3.5-9B, Gemma-4-E4B-it, and Qwen3.6-27B, RecurSE achieves consistent generalization gains across held-out medical, pairwise, summarization, and professional benchmarks. Ablations demonstrate that synchronized judge-checker co-evolution outperforms frozen checkers, external meta-judges, self-consistency, and scaled teacher distillation. Furthermore, preference pairs curated by our judge effectively enhance downstream policy alignment. Bounded RSI for LLM-as-judge is thus viable when self-produced reward validity is explicitly decoupled and monitored.

## Metadata
- **Published**: 2026-08-25T08:35:04Z
- **Authors**: Kaiyuan Liu, Ziyuan Zhuang, Rongxiang Weng, Jieping Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24231v1)
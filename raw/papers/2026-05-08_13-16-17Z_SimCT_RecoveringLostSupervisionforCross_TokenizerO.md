---
title: 'SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation'
published: 2026-05-08T13:16:17Z
authors: Jie Sun, Mao Zheng, Mingyang Song, Qiyong Zhong, Yilin Cheng, Bichuan Feng, Pengfei Liu, Junfeng Fang, Xiang Wang
url: http://arxiv.org/abs/2605.07711v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation

## Abstract
On-policy distillation (OPD) is a standard tool for transferring teacher behavior to a smaller student, but it implicitly assumes that teacher and student predictions are comparable token by token, an assumption that fails whenever the two models tokenize the same text differently. Under heterogeneous tokenizers, exact shared-token matching silently discards a large fraction of the teacher signal at precisely the positions where vocabularies disagree. We propose \textbf{\underline{Sim}ple \underline{C}ross-\underline{T}okenizer OPD (SimCT)}, which restores this signal by enlarging the supervision space: alongside shared tokens, SimCT compares teacher and student over short multi-token continuations that both tokenizers can realize, leaving the OPD loss form itself unchanged. We show that these units are the finest jointly tokenizable supervision interface, and that coarser alternatives remove teacher-student distinctions that are useful for on-policy learning. Across three heterogeneous teacher-student pairs on mathematical reasoning and code-generation benchmarks, SimCT shows consistent gains over shared-vocabulary OPD and representative cross-tokenizer baselines, with ablations confirming that the improvements come from recovering supervision discarded by exact shared-token matching. Code is available at \href{https://github.com/sunjie279/SimCT-}{https://github.com/sunjie279/SimCT-}.

## Metadata
- **Published**: 2026-05-08T13:16:17Z
- **Authors**: Jie Sun, Mao Zheng, Mingyang Song, Qiyong Zhong, Yilin Cheng, Bichuan Feng, Pengfei Liu, Junfeng Fang, Xiang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.07711v1)
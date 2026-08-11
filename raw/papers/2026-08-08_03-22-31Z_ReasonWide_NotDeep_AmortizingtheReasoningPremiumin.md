---
title: Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills
published: 2026-08-08T03:22:31Z
authors: Agamdeep Singh, Srishti Gautam, Priyanshu Gupta, Nikita Mehrotra, Tanmay Bakshi, Sumit Gulwani
url: http://arxiv.org/abs/2608.07885v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills

## Abstract
Reasoning modes of language models outperform their non-reasoning counterparts on multi-step agentic tasks, but pay a 3-6x premium in output tokens on every episode -- much of it spent re-deriving procedures that are shared across episodes of the same domain. We show this recurring cost can be amortized: a coding agent analyses a small corpus of existing trajectories from a training split and compiles a compact natural-language skill that is injected into the non-reasoning model's system prompt. Across four agentic benchmarks (ALFWorld, tau$^2$-bench telecom and retail, and SpreadsheetBench-Verified), skills recover 55%-100%+ of the reasoning gap for GPT-5.4-mini on held-out tasks -- exceeding the reasoning mode outright on two of four -- while emitting 2.7-6x fewer output tokens and zero reasoning tokens. Notably, reasoning traces are not a prerequisite: skills distilled from non-reasoning trajectories alone remain competitive with skills distilled from paired reasoning/non-reasoning corpora, with domain-dependent differences between the two sources. We interpret these results through a search lens: test-time reasoning is deep search inside a single episode, re-paid at every deployment, while corpus distillation is wide search across episodes, paid once. The two recover overlapping procedural knowledge, and width over cheap trajectories is often the better buy -- with the residual gap on some domains (telecom, SpreadsheetBench) delineating where genuinely per-instance deep search remains necessary.

## Metadata
- **Published**: 2026-08-08T03:22:31Z
- **Authors**: Agamdeep Singh, Srishti Gautam, Priyanshu Gupta, Nikita Mehrotra, Tanmay Bakshi, Sumit Gulwani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07885v1)
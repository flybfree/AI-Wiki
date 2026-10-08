---
title: Humanize: Judgement Engineering for Agentic Coding
published: 2026-10-06T17:54:42Z
authors: Sihao Liu, Ligeng Zhu, Zijian Zhang, Dongyun Zou, Zhengyang Zhang, Changye Li, Song Bian, Song Han, Tony Nowatzki
url: http://arxiv.org/abs/2610.08900v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Humanize: Judgement Engineering for Agentic Coding

## Abstract
Agentic coding makes code generation cheap, but reliable completion remains difficult: the agent that writes the code is a weak judge of whether it is done.   We present Humanize, a multi-agent orchestration workflow for agentic coding built around judgement engineering: explicit, mechanically enforced decisions at the boundaries between planning, implementation, review, and learning. A human approves a plan contract, a builder agent implements it in rounds, and a reviewer agent from another vendor decides completion; deterministic hooks, not a model, route work between these roles and enforce 72 mechanical gates. Viewed as a Markov chain over repository states, alternating builder and reviewer samples jointly from two models, so a defect survives only if both miss it. We study Humanize through its deployment, 118 public postmortems of real loops, and its applications. Over 68 versions in 108 days, it gathered 1,468 GitHub stars.   Applications include a 567-file gem5 build-system migration under upstream review; Kernel Design Agents, which extend the loop with a kernel knowledge base and profiling feedback and placed in the top three of all three Full-Agent tracks of the MLSys 2026 FlashInfer contest; and, through Humanize Olympiad Agents (HOA), full scores in IOI 2026, IMO 2026, IPhO 2026, and IBO 2024, 418.5/437 in IChO 2026 (gold-medal). Humanize also achieves 672/672 on PutnamBench and ranks first (251/303) on Lean-Eval's leaderboard even competiting with professional mathematicians. The postmortems show that independent review catches unsupported builder claims, but stopping remains a key weakness. In reports that separate rounds by phase, two thirds of rounds occurred after implementation was accepted. This evidence is observational, not a controlled comparison of workflows.

## Metadata
- **Published**: 2026-10-06T17:54:42Z
- **Authors**: Sihao Liu, Ligeng Zhu, Zijian Zhang, Dongyun Zou, Zhengyang Zhang, Changye Li, Song Bian, Song Han, Tony Nowatzki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08900v1)
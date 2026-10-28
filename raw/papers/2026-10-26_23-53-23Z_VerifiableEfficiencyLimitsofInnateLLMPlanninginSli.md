---
title: Verifiable Efficiency Limits of Innate LLM Planning in Sliding Puzzles
published: 2026-10-26T23:53:23Z
authors: Yezhou Cheng, Charles Ling
url: http://arxiv.org/abs/2610.36415v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verifiable Efficiency Limits of Innate LLM Planning in Sliding Puzzles

## Abstract
Tool-assisted planning success can reflect external search and verification, leaving a model's unaided planning ability unresolved. We isolate innate planning through complete plans generated in one response without tools or execution feedback. We propose a verifiable framework that decomposes success-weighted plan efficiency as $\mathrm{SPE}=R\times Q\times E$: execution reliability, planning coordination among legal plans, and action economy among completed plans. Trajectory replay and certified optima verify these factors; the joint score includes unsuccessful attempts. We evaluate 8,400 full-plan outputs from seven model conditions on $4\times4$ sliding puzzles, controlling exact horizon and obstacle count in the primary cohort. Models that complete every trial still become less economical at longer horizons, while higher efficiency among completed plans can coexist with poor goal attainment. SPE separates the overall capability hierarchy, while its factors distinguish coordination failure from inefficient completion. The framework makes long-horizon limitations in unaided planning quantitatively verifiable.

## Metadata
- **Published**: 2026-10-26T23:53:23Z
- **Authors**: Yezhou Cheng, Charles Ling
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36415v1)
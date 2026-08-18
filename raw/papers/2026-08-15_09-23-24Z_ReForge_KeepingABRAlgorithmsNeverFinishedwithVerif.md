---
title: ReForge: Keeping ABR Algorithms Never Finished with Verified Large Language Model Edits
published: 2026-08-15T09:23:24Z
authors: Zhiqiang He, Zhi Liu
url: http://arxiv.org/abs/2608.15138v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReForge: Keeping ABR Algorithms Never Finished with Verified Large Language Model Edits

## Abstract
Designing an ABR algorithm for one network scenario takes an engineer months, and large language models now do this work in hours, matching or beating hand-built designs. But either way, the design fits only the world visible at its birth, and fails on the world that arrives after. We ask whether an ABR algorithm can keep pace with the world, redesigned in minutes as each scenario arrives, with every change proven harmless to every scenario already served. In this work, we propose ReForge, a continual heuristic learning framework that adapts to continuously changing scenarios. ReForge runs that routine with a large language model (LLM) in the loop. Each round the LLM reads where the current design falls short and proposes one small edit, and a replay over every network served so far decides. Specifically, what it edits is a single page of fuzzy rules that routes every decision to one of a frozen pool of pre-trained policies. The LLM writes the first page from measurements alone, then keeps improving it on its own. Each round it reads where the current rules fall short and proposes one small edit, and a replay over every network served so far decides whether the edit lands. We evaluate ReForge on nine real-world network families arriving one at a time as 3G, 4G, then 5G. A few edits per arrival lift mean QoE from 1.23 to 1.74, past the best single policy at 1.66 and to 94\% of an oracle, and even repair families the loop never saw, one rising from 0.30 to 0.80. All code, data, and experiment records will be open-sourced upon cleanup.

## Metadata
- **Published**: 2026-08-15T09:23:24Z
- **Authors**: Zhiqiang He, Zhi Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15138v1)
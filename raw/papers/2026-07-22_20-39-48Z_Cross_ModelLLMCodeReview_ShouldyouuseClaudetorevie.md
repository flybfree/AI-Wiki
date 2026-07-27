---
title: Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?
published: 2026-07-22T20:39:48Z
authors: Zuodong Xiang, Yike Zhang, YueMing Zhang, Hailu Xu
url: http://arxiv.org/abs/2607.21656v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?

## Abstract
Developers increasingly use two coding agents together: one writes a draft, and the other reviews it. However, it is not clear whether the pairing is worth its cost and time, or whether the order of the pairing matters. We run a controlled experiment on 116 recent hard and medium lcb tasks with Claude and Codex across six conditions to approximate a software practitioner's workflow: both solo baselines, both cross-model orderings, and both same-model orderings. The reviewer sees the problem and the writer's draft but cannot execute tests, which approximates a code review step. Claude review raises Codex drafts from 71.6% to 89.7% ($p_{BH}=.001$); Codex self review raises them to 84.5% ($p_{BH}=.022$). The reverse direction does not pay off: Codex reviewing Claude drafts drops the pass rate from 91.4% to 82.8% ($p_{BH}=.046$), and Claude self review leaves the 91.4% baseline unchanged. Our evaluation indicates that the useful pairing is asymmetric: use Claude to review Codex, not the other way around.

## Metadata
- **Published**: 2026-07-22T20:39:48Z
- **Authors**: Zuodong Xiang, Yike Zhang, YueMing Zhang, Hailu Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21656v1)
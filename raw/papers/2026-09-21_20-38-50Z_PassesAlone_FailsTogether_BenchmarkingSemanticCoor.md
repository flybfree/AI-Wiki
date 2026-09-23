---
title: Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development
published: 2026-09-21T20:38:50Z
authors: Haocheng Xia, Eugene Wu, Yongjoo Park
url: http://arxiv.org/abs/2609.25396v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development

## Abstract
Parallel coding agents can produce patches that work alone but fail when merged. This happens when one agent changes an interface or rule that another agent still relies on. We study these failures with stale, a benchmark for semantic coordination. Our evaluation runs the same tests on each patch alone and on their combination, counting only failures introduced by combining the patches. We use three tiers: synthetic tasks with controlled interface changes, pairs of merged pull requests, and constructed tasks that use real Django helpers. Among 834 runs on 417 mined Django pairs, only one showed interference after correcting the grading procedure. On constructed tasks using 12 Django helpers, interference occurred in 97% of runs. A message describing the completed concurrent change recovered 82% of runs. Reviewed pull requests may contain few unresolved parallel changes, even when agents fail on controlled tasks using real code. The constructed failure rates do not estimate how often these problems occur in practice.

## Metadata
- **Published**: 2026-09-21T20:38:50Z
- **Authors**: Haocheng Xia, Eugene Wu, Yongjoo Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25396v1)
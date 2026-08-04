---
title: Shared Prefixes, Better Credit: Adaptive Routing for Multi-Agent Reasoning
published: 2026-08-03T14:22:23Z
authors: Yiqing Liu, Zihao Wang, Hantao Yao, Wu Liu, Yongdong Zhang
url: http://arxiv.org/abs/2608.02291v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Shared Prefixes, Better Credit: Adaptive Routing for Multi-Agent Reasoning

## Abstract
Multi-agent reasoning (MAR) improves reasoning reliability through iterative solution exchange and refinement. Existing adaptive MAR methods typically learn routing decisions from query-level labels or trajectory-level returns, but such coarse supervision cannot accurately estimate the state-conditioned utility of individual operators in multi-step collaboration. We propose TreeCredit, a shared-prefix credit assignment framework for efficient adaptive MAR. Its core insight is to estimate operator utility through state-matched downstream comparisons, rather than directly attributing trajectory-level outcomes to preceding decisions. TreeCredit constructs shared-prefix collaboration trees by expanding candidate operators from the same intermediate state and assigns each state--operator pair a correctness-prioritized suffix credit based on the terminal correctness and cumulative additional cost of its complete continuation. These structured credits are converted into state-local operator preferences to train a lightweight pairwise state router, which dynamically selects the next admissible operator during inference. Experiments on six reasoning benchmarks show that TreeCredit modestly improves accuracy while substantially reducing inference cost, achieving a better accuracy--cost trade-off than representative MAR methods.

## Metadata
- **Published**: 2026-08-03T14:22:23Z
- **Authors**: Yiqing Liu, Zihao Wang, Hantao Yao, Wu Liu, Yongdong Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02291v1)
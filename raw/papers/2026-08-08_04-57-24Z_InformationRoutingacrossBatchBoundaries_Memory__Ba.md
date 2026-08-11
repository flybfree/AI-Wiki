---
title: Information Routing across Batch Boundaries: Memory--Batch Tradeoffs in Lipschitz Bandits
published: 2026-08-08T04:57:24Z
authors: Zicheng Lyu, Zengfeng Huang
url: http://arxiv.org/abs/2608.07922v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Information Routing across Batch Boundaries: Memory--Batch Tradeoffs in Lipschitz Bandits

## Abstract
Adaptive learning needs both a state that preserves what observations imply and opportunities to act on that state. We study this width--depth tradeoff in stochastic Lipschitz bandits. After each pull, the learner retains at most $W$ bits of live reward-dependent state and organizes its pulls into at most $B$ committed batches. For $W\gtrsim_d\log(eT)$, we characterize minimax expected pseudo-regret up to logarithmic factors; the lower bounds hold for every $W$. Besides the classical sequential and unrestricted-memory batch costs, the frontier contains the new penalty \[   T^{\frac{d+2}{d+3}}   \bigl(1+(B-1)W\bigr)^{-\frac1{d(d+3)}}, \] proving that state width and update depth are not interchangeable. The interaction is an information-routing constraint: at regional scale $s$, low regret forces the committed action transcript to encode $Θ_d(s^{-d})$ regional decisions, while the collected boundary states carry at most $(B-1)W$ bits of entropy. Matching policies stream and erase verification statistics while retaining a mask of a safe active set, either in memory or fragment by fragment. The theorem recovers the full-dimensional worst-case batch-only frontier and logarithmic-memory achievability in the fully sequential specialization; static batch boundaries match predictable adaptive ones.

## Metadata
- **Published**: 2026-08-08T04:57:24Z
- **Authors**: Zicheng Lyu, Zengfeng Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07922v1)
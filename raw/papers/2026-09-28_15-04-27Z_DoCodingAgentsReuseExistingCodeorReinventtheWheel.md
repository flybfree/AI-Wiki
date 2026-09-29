---
title: Do Coding Agents Reuse Existing Code or Reinvent the Wheel?
published: 2026-09-28T15:04:27Z
authors: Dongsheng Ma, Sizhe Wang, Xinyi Huang, Zhengren Wang, Yuhan Wang, Luyang Si, Xincheng Wei, Wentao Zhang
url: http://arxiv.org/abs/2609.35357v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Coding Agents Reuse Existing Code or Reinvent the Wheel?

## Abstract
Coding agents are increasingly deployed for iterative development on real repositories, yet existing evaluation barely answers a basic question: \emph{do coding agents reuse existing code or reinvent the wheel?} The question matters: every duplicated implementation is a fix applied twice and agents produce code far faster than humans can audit, so redundancy accumulates unsupervised. Thus, we present \textbf{RepoReuse}, a multi-turn benchmark for auditing code reuse in real repositories, where requirements are revealed turn by turn and the workspace accumulates across turns. It is built by a fully automated pipeline combining AST-based dependency graphs, guided evidence collection, and execution-verified task synthesis, and scales readily to new repositories. Beyond pass rates, we measure the reuse rate together with recall and cross-turn structural redundancy. An audit over 3{,}000 turns shows that agents progressively stop exploring relevant repository code, reuse their own history less even when it is fully in the workspace, and leave duplicated logic in 50.8\% of task chains by turn~5---all while pass rates barely move. Such deficiencies are invisible to pass rates, underscoring the need to evaluate code generation beyond functional correctness.

## Metadata
- **Published**: 2026-09-28T15:04:27Z
- **Authors**: Dongsheng Ma, Sizhe Wang, Xinyi Huang, Zhengren Wang, Yuhan Wang, Luyang Si, Xincheng Wei, Wentao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35357v1)
---
title: SymStep: Symbolic Step Verification for Logical Reasoning
published: 2026-07-25T05:46:17Z
authors: Aida Usmanova, Rui Gao, Dilshod Azizov, Ricardo Usbeck, Zangir Iklassov
url: http://arxiv.org/abs/2607.23055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SymStep: Symbolic Step Verification for Logical Reasoning

## Abstract
Chain-of-thought (CoT) prompting can fail severely on constraint-dense logical reasoning tasks, where unverified errors accumulate silently across steps. We introduce SymStep: an LLM makes one atomic claim at a time (DEDUCE: Alice, pet, Cat), then a lightweight constraint propagator checks the claim for consistency with prior accepted deductions, rejects contradictions, and cascades implied facts automatically. SymStep+G additionally provides MRV guidance after each accepted step, directing the LLM toward the most constrained unresolved variable. On a 35-puzzle retained subset of ZebraLogicBench, a benchmark of 1,000 Einstein-style logic puzzles, Direct and CoT both achieve 0%, while SymStep+G reaches 97%. On AR-LSAT analytical reasoning problems, SymStep achieves 100% vs. CoT's 87%. On LGP-14, SymStep+G achieves 100% vs. 0% for CoT and Logic-LM, the strongest prior symbolic+LLM baseline we compare against. Ablation studies reveal that MRV guidance is a key mechanism for reducing directionless cycling, while consistency checking provides a safety net against explicit contradictions. Across six benchmarks spanning five task domains, SymStep variants match or exceed every baseline on constraint-dense and arithmetic tasks. Experiments on AQUA-RAT algebra confirm the advantage is constraint-density-specific.

## Metadata
- **Published**: 2026-07-25T05:46:17Z
- **Authors**: Aida Usmanova, Rui Gao, Dilshod Azizov, Ricardo Usbeck, Zangir Iklassov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23055v1)
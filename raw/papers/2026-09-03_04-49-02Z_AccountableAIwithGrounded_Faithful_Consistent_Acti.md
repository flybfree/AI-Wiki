---
title: Accountable AI with Grounded, Faithful, Consistent, Actionable Rationales: A Case Study in Clinical Trial Matching with VERDICT
published: 2026-09-03T04:49:02Z
authors: Zikai Zhou, Yufei Jin, Yilin Xu, Yu-Chiang Wang, Chieh-Ju Chao, Monica S. Lam
url: http://arxiv.org/abs/2609.03366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Accountable AI with Grounded, Faithful, Consistent, Actionable Rationales: A Case Study in Clinical Trial Matching with VERDICT

## Abstract
Accountability means a decision can be examined, justified, and contested. LLMs make this hard: fluent output may be ungrounded, incomplete, or unfaithful to the decision process. Achieving accountability requires verified rationales (how was the decision reached), assumptions (what was assumed rather than known), policy consistency (the same treatment for the same facts), and pivotal conditions (what would change the outcome). We introduce self-faithfulness as an automatic test of accountability: changing the pivotal conditions should change the decision.   We examine accountable AI through clinical trial matching, a high-stakes task central to evidence-based medicine. Although LLM-based matchers match patients to trials reasonably accurately, they apply decision policies inconsistently and produce rationales that are unfaithful to their own decisions.   We introduce VERDICT, an LLM-based agent that translates a decision task, its constraints, and its policy into Satisfiability Modulo Theories (SMT), then derives the decision with SMT and MaxSMT solvers -- so policies are applied consistently and decisions are accountable by construction.   Across a SIGIR 2016-derived dataset and TREC 2021, VERDICT achieves the strongest decision accuracy among LLM-only and neurosymbolic baselines, applies policies with perfect consistency, and produces clinician-preferred rationales grounded in explicit assumptions and pivotal conditions, with improved counterfactual self-faithfulness.

## Metadata
- **Published**: 2026-09-03T04:49:02Z
- **Authors**: Zikai Zhou, Yufei Jin, Yilin Xu, Yu-Chiang Wang, Chieh-Ju Chao, Monica S. Lam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03366v1)
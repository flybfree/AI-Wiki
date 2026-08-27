---
title: FLARE: Verifying MILP Reformulations with LLM-Based Theorem Proving
published: 2026-08-25T23:19:41Z
authors: Henry Robbins, Connor Lawless, Madeleine Udell, Ellen Vitercik
url: http://arxiv.org/abs/2608.25220v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FLARE: Verifying MILP Reformulations with LLM-Based Theorem Proving

## Abstract
Mixed-Integer Linear Programming (MILP) is a fundamental tool for combinatorial optimization with extensive real-world applications. A central challenge is designing computationally efficient MILP formulations. Large Language Models (LLMs) offer new opportunities to automate the modeling process, from deriving formulations to strengthening them. Reliable automation requires robust methods for verifying that proposed formulations preserve the underlying optimization problem. However, existing approaches evaluate formulations numerically and fail to reason about general problem instances. We resolve this limitation by introducing a constructive definition of MILP reformulation that can be formalized in Lean and machine-checked. We develop FLARE (Formulation-Level Automated Reformulation Evaluation), a method that uses an LLM-based agent and the Lean proof assistant to verify proposed reformulations against a reference formulation. To evaluate our approach, we introduce FormulationBench, a challenging dataset of 20 problems and 109 formulations. FLARE outperforms existing methods, with 100% accuracy on the NP-hard subset of FormulationBench. Furthermore, FLARE produces a machine-checkable certificate for every reformulation it accepts. For cases where formal guarantees are not necessary, we introduce FLARE-NL, a fast and cheap LLM proxy that matches FLARE's accuracy but produces no certificate. These methods enable reliable verification in automated optimization modeling.

## Metadata
- **Published**: 2026-08-25T23:19:41Z
- **Authors**: Henry Robbins, Connor Lawless, Madeleine Udell, Ellen Vitercik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25220v1)
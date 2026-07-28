---
title: What Can Be Enforced? A Theory of Certified Runtime Safety for Tool-Using Agents
published: 2026-07-24T19:14:26Z
authors: Shawn Ray
url: http://arxiv.org/abs/2607.22868v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Can Be Enforced? A Theory of Certified Runtime Safety for Tool-Using Agents

## Abstract
Runtime guardrails act before irreversible tool calls, but their guarantees depend on what policy state is representable, what a judge observes, and whether intervention changes future behavior. We separate three questions. First, relative to fixed oracle predicates, a deterministic gate enforces exactly the nonempty safety policies whose good prefixes its register model recognizes; policy nontriviality is undecidable with two decrementable counters but in PSPACE for a separable monotone fragment. Second, under a fixed exogenous law, Neyman-Pearson gives the exact false-block/miss frontier and conformal calibration gives a finite-sample marginal certificate, possibly via block-all. Third, once blocking changes future proposals, static scores and ungated trajectories need not identify the closed-loop frontier; a specified finite controlled model instead yields an occupancy program. Bounded representation attacks add a robustness margin, so benign calibration alone does not transfer. Experiments target these distinctions through static diagnostics, controlled-model enumeration, representation rewrites, and paired closed-loop reruns.

## Metadata
- **Published**: 2026-07-24T19:14:26Z
- **Authors**: Shawn Ray
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22868v1)
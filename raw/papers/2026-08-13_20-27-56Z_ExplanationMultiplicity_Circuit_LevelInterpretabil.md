---
title: Explanation Multiplicity: Circuit-Level Interpretability Evidence Does Not Survive Defensible Analytic Variation
published: 2026-08-13T20:27:56Z
authors: Ajay Pravin Mahale
url: http://arxiv.org/abs/2608.13754v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explanation Multiplicity: Circuit-Level Interpretability Evidence Does Not Survive Defensible Analytic Variation

## Abstract
The EU AI Act requires providers of high-risk systems to file technical documentation describing how the system reaches its decisions. Mechanistic interpretability is the obvious source of such evidence, and circuit discovery is its most developed instrument. We ask whether that evidence survives the condition under which it would be relied upon: two competent analysts, the same system, the same tool, different defensible settings.   We pre-registered a crossed grid of seven analytic axes, every level taken from a published implementation, and mapped each discovered circuit through a deterministic claim map to a structured Annex IV statement. Across 15,840 pre-registered specifications on GPT-2 small and the indirect object identification task, of which 7,561 produced a claim, the derived statement flips across 73.2% of specification pairs (95% CI 0.725 to 0.738) and the modal claim commands 41.1% of the space. The evidence fails a filability criterion at every tolerance a conformity assessment body would plausibly accept.   Standardising the single most influential choice, the evaluation metric, leaves the flip rate at 59.4%. Removing circuit size from the claim entirely and holding it fixed leaves 27.1% (95% CI 0.255 to 0.286), still above the pre-registered threshold. The circuits underlying these claims are structurally near-disjoint, median pairwise Jaccard overlap 4%, and functionally uncorrelated at Cohen's kappa 0.015, so the instability is not one mechanism described in different words.   We give the filability criterion as a standalone protocol, and we report that one of the seven documented discovery objectives does not execute at all on the library's own canonical task. The study covers one model and one task, and whether the conclusion holds at scale is untested.

## Metadata
- **Published**: 2026-08-13T20:27:56Z
- **Authors**: Ajay Pravin Mahale
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13754v1)
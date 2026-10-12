---
title: Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus but Not Agreement with Humans
published: 2026-10-09T09:49:31Z
authors: Sangdo Han, Moonsoo Kim
url: http://arxiv.org/abs/2610.13303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus but Not Agreement with Humans

## Abstract
LLM judges are increasingly deployed as panels, and disagreement among panel members is often read as a symptom of an unclear rubric. We test a label-free procedure that turns this disagreement into rubric repairs. The procedure decomposes each rubric into sub-criteria, ranks them by cross-judge disagreement on a development split, and has an editor model rewrite only the most contested ones. An additional stage that moves text-checkable sub-criteria to deterministic checkers transferred none in our evaluation. Human labels are never used to select or edit clauses; they are used only to evaluate the outcome. We pre-specified four hypotheses in a version-controlled protocol and evaluated six rubric conditions with a panel of five judges from three providers on SummEval, the HealthBench meta-evaluation, and USR Topical-Chat, for a total of 129,770 judge requests, excluding retries. On SummEval, the procedure raised inter-judge Krippendorff's $α$ by 0.069 (95% CI 0.046 to 0.092) over the original rubric and by 0.074 over a control that applied the same edits to an equal number of randomly chosen clauses that were not selected. Agreement with expert ratings showed no detectable change (Kendall $τ$ difference -0.007, 95% CI -0.037 to 0.021). On HealthBench and USR, neither inter-judge agreement nor human agreement met the preregistered effect criteria. In a preregistered secondary comparison, human agreement after editing the contested clauses was lower than after editing the control clauses on all three datasets in point estimate, although no interval excluded zero. Selecting clauses by disagreement makes judges agree with each other more than editing arbitrary clauses does, but in our setting the added consensus did not bring the judges closer to human annotators. We will release code, frozen rubrics, item identifiers, and judge scores.

## Metadata
- **Published**: 2026-10-09T09:49:31Z
- **Authors**: Sangdo Han, Moonsoo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13303v1)
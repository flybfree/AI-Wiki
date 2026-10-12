---
title: Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus but Not Agreement with Humans
url: http://arxiv.org/abs/2610.13303v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_09-49-31Z_AgreementWithoutAlignment_Label_FreeRubricClarific.md
generated_at: 2026-10-11 21:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether using disagreement among LLM judges to identify and repair ambiguous rubric criteria can improve both inter-judge consensus and alignment with human evaluators. The authors propose a label-free procedure that decomposes rubrics into sub-criteria, ranks them by cross-judge disagreement, and has an editor model rewrite only the most contested clauses. While the procedure successfully increases agreement among LLM judges (raising Krippendorff's α by 0.069 on SummEval), it produces no detectable improvement in agreement with expert human ratings, revealing a critical gap between machine consensus and human alignment.

## Key Takeaways
- The label-free rubric repair procedure increased inter-judge Krippendorff's α by 0.069 (95% CI 0.046 to 0.092) over the original rubric on SummEval, and by 0.074 over a control that applied identical edits to randomly chosen non-contested clauses, demonstrating that targeting disagreement specifically is more effective than arbitrary editing for building judge consensus.
- Despite improved inter-judge agreement, agreement with expert human ratings showed no detectable change (Kendall τ difference of -0.007, 95% CI -0.037 to 0.021), and on HealthBench and USR Topical-Chat, neither inter-judge agreement nor human agreement met the preregistered effect criteria, indicating the consensus gains did not translate into human alignment.
- In a preregistered secondary comparison, human agreement after editing contested clauses was actually lower than after editing control clauses on all three datasets in point estimate, suggesting that the procedure may inadvertently steer judges toward a shared but human-divergent interpretation of the rubric.

## Context
LLM judges are increasingly deployed in panels for automated evaluation of model outputs, and disagreement among panel members is commonly interpreted as evidence of poorly written rubrics. This paper directly addresses that assumption by testing whether mechanically repairing contested rubric clauses resolves the underlying problem. The work is situated within the broader challenge of building reliable automated evaluation pipelines for language models, where rubric design and judge calibration remain open problems. The use of a pre-specified, version-controlled protocol with four hypotheses and six rubric conditions across three benchmark datasets represents a methodologically rigorous approach to a field often criticized for ad hoc evaluation practices.

## Implications
For practitioners deploying LLM judge panels, this finding warns that increasing inter-judge agreement is not a proxy for evaluation validity, and that rubric repair strategies targeting disagreement may produce consensus around interpretations that diverge from human judgment. The result challenges the intuitive pipeline of "detect disagreement, fix the rubric, achieve better evaluation" and suggests that alignment with human annotators requires fundamentally different interventions than those that promote machine-to-machine agreement. The authors' commitment to releasing code, frozen rubrics, item identifiers, and judge scores provides a reproducible foundation for future work to explore alternative approaches to rubric design that actually improve human alignment rather than merely reducing panel disagreement.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13303v1)

---
title: CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search
url: http://arxiv.org/abs/2609.15164v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-14_07-47-47Z_CITECHOICE_ACausalAuditofHowDocumentPresentationRe.md
generated_at: 2026-09-14 22:20
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces CITECHOICE, a causal audit examining how document presentation influences citation allocation in multi-turn agentic search systems. By analyzing authentic query transcripts and conducting controlled reordering experiments, the authors demonstrate that structured rendering significantly concentrates visible citation credit on target documents without increasing overall citation counts or diminishing competitor visibility. The study further reveals that observational rank effects substantially outweigh controlled formatting interventions, while highlighting inherent stochasticity in how models evaluate and cite sources.

## Key Takeaways
- Structured document rendering causally redistributes citation credit, increasing the average number of citations per answer by 0.50 (95% CI [+0.20, +0.84]) without inflating total citations or reducing competitor attribution, though it does not reliably increase the likelihood of a source being cited at all.
- Natural observational position effects dominate controlled experimental manipulations: the citation-rate gap between rank 1 and rank 5 documents spans 42.3 percentage points, far exceeding the modest +7.9 percentage point shift observed during structured reordering trials.
- Citation evaluation exhibits a significant noise floor, with fresh model decoding altering 15 percent of binary citation decisions and accounting for approximately 45 percent of variance in single-generation family effects, underscoring the stochastic nature of source attribution.

## Context
As agentic search systems increasingly mediate information access, understanding how retrieval ranking and document formatting influence downstream citation behavior is critical for ensuring equitable knowledge distribution. This research bridges causal inference methodologies with large language model evaluation, addressing a gap in how AI systems allocate credit among competing sources when multiple documents support identical claims.

## Implications
The findings suggest that developers should prioritize transparent ranking mechanisms and mitigate positional bias rather than relying solely on formatting adjustments to influence source visibility. Practitioners designing search interfaces must account for inherent model stochasticity when evaluating citation fairness, recognizing that presentation changes alone cannot guarantee reliable source admission. Ultimately, these insights inform more robust evaluation frameworks for AI-driven information retrieval systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15164v1)

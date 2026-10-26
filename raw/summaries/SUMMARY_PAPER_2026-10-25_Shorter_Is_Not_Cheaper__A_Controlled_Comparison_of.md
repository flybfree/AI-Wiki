---
title: Shorter Is Not Cheaper: A Controlled Comparison of Declarative Animation Specifications and Free-Form Code for LLM-Generated Explanations
url: http://arxiv.org/abs/2610.32129v1
type: paper-summary
date: 2026-10-25
source_paper: 2026-10-23_03-56-19Z_ShorterIsNotCheaper_AControlledComparisonofDeclara.md
generated_at: 2026-10-25 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper challenges the widely held assumption that declarative animation specifications (as opposed to free-form HTML/JavaScript code) produce cheaper, faster, and more reliable outputs from large language models. Through controlled comparisons across three Claude models and the open-weight Qwen3-14B, the author demonstrates that while declarative specifications are 25–48% shorter in raw output tokens, reasoning models compensate by generating substantially more reasoning tokens before producing the specification, negating any cost savings. Furthermore, declarative formats proved significantly less reliable than free-form code, particularly for smaller models.

## Key Takeaways
- Although declarative specifications reduced answer tokens by 25–48% across all tested models, total output (including reasoning traces) fell significantly only for the largest Claude model, and no model generated faster in the declarative format. The Claude models shifted dramatically toward exploratory reasoning before writing specifications, with the two larger models spending 85–88% of their generation budget on reasoning compared to 15–20% for free-form code. Qwen3-14B, by contrast, reasoned about equally in both formats, and its shorter answers were overwhelmed by a reasoning trace more than twice as long as the answer itself.
- Reliability strongly favored free-form code. HTML/JavaScript pages achieved validity after a single repair round in 95–100% of jobs across every model, whereas Qwen3-14B produced valid declarative specifications in only 33% of jobs and passed all semantic correctness tests in just 17% of cases (compared to 62% for HTML/JavaScript). This suggests that a format learned primarily in context, rather than through fine-tuning, can actively degrade reliability.
- The study was methodologically rigorous: hypotheses and analysis plans were frozen before runs, a custom observation contract made every generated explanation programmatically inspectable, and pacing-agnostic checkers scored 20 explanation requests across five domains, ensuring results were not artifacts of post-hoc analysis.

## Context
As chat assistants increasingly embed interactive, animated explanations directly into their responses, the field has gravitated toward declarative specification formats under the assumption that constrained, shorter outputs reduce token costs and improve reliability. This paper directly interrogates that assumption using a pre-registered experimental design spanning multiple model families and reasoning configurations, providing one of the first controlled comparisons of these two generation strategies. It matters because the choice of output format is a foundational architectural decision for any product team building LLM-powered educational or explanatory tools, and the findings overturn a widely accepted heuristic.

## Implications
For practitioners building LLM-driven explanation systems, the findings caution against adopting declarative formats solely for perceived cost savings, since reasoning models may inflate their total token consumption to compensate, and smaller or open-weight models may produce unreliable specifications. Industry teams should prioritize robustness of free-form code generation with repair loops over constrained declarative pipelines, especially when using models that have not been specifically fine-tuned on the target specification language. More broadly, the paper highlights that format constraints interact non-trivially with reasoning behavior, a consideration that should inform future model training, tool design, and evaluation benchmarks in the growing space of LLM-generated interactive content.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.32129v1)

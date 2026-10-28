---
title: Verifiable Efficiency Limits of Innate LLM Planning in Sliding Puzzles
url: http://arxiv.org/abs/2610.36415v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_23-53-23Z_VerifiableEfficiencyLimitsofInnateLLMPlanninginSli.md
generated_at: 2026-10-27 22:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a verifiable framework for measuring the innate planning ability of large language models by isolating their performance from external tool assistance and execution feedback. The authors evaluate seven model conditions on 4×4 sliding puzzles using 8,400 complete plan outputs generated in a single response, decomposing success-weighted plan efficiency into three multiplicative factors: execution reliability, planning coordination among legal plans, and action economy among completed plans. The central finding is that even models capable of completing every trial degrade in action economy as puzzle horizons lengthen, and that high efficiency among completed plans can coexist with poor overall goal attainment, revealing distinct failure modes in unaided planning.

## Key Takeaways
- The proposed SPE framework (SPE = R × Q × E) provides a quantitative decomposition of planning performance into execution reliability (R), coordination quality among legal plans (Q), and action economy among completed plans (E), enabling researchers to distinguish whether a model fails because it cannot coordinate legal moves or because it completes plans inefficiently, rather than conflating these distinct failure modes into a single success metric.
- Even models that achieve 100% trial completion exhibit measurable degradation in action economy at longer planning horizons, demonstrating that innate planning capability is not a binary capability but a graded resource that erodes with problem complexity, and that this erosion is quantitatively verifiable through trajectory replay and certified optimal solutions.
- The framework reveals that high efficiency scores among completed plans can mask poor overall goal attainment, meaning that evaluating only successful completions overstates a model's planning capability; the joint score that includes unsuccessful attempts is essential for an honest assessment of unaided planning ability.

## Context
This work addresses a persistent methodological gap in LLM evaluation: tool-assisted planning benchmarks conflate a model's internal reasoning capacity with the external scaffolding provided by search algorithms, code execution, or iterative feedback loops. By requiring complete plans in a single response with no tools or execution feedback, the authors create a controlled experimental setting where planning failures can be attributed directly to the model's internal architecture. The sliding puzzle domain is deliberately chosen for its verifiable optimality guarantees, allowing certified comparisons against known optimal solutions rather than heuristic scoring.

## Implications
For practitioners deploying LLMs in autonomous planning tasks such as robotics, logistics, or multi-step reasoning pipelines, this framework provides a diagnostic tool to determine whether a model's apparent planning competence is genuine or an artifact of external tool scaffolding. Industry teams selecting models for planning-heavy applications can use the SPE decomposition to identify whether a candidate model suffers from coordination failures or inefficient action selection, guiding targeted fine-tuning or tool-integration strategies. The finding that long-horizon degradation is universal across model conditions suggests that current architectures have fundamental limits in unaided sequential planning that cannot be overcome by scale alone, reinforcing the practical necessity of external verification and search infrastructure in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36415v1)

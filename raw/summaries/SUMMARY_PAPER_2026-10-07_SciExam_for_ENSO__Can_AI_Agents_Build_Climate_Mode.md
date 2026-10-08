---
title: SciExam for ENSO: Can AI Agents Build Climate Models?
url: http://arxiv.org/abs/2610.10513v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_17-52-52Z_SciExamforENSO_CanAIAgentsBuildClimateModels.md
generated_at: 2026-10-07 22:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SciExam for ENSO introduces a benchmark that evaluates whether language-model agents can build valid low-order stochastic models of El Niño-Southern Oscillation from real observational data, without access to a known correct answer. Across twelve agent systems tested within a six-hour budget, six produced models that outperformed a published human-developed model, particularly in reconstruction and forecasting capabilities, while the resulting model structures independently aligned with competing scientific explanations of ENSO's warm-cold asymmetry.

## Key Takeaways
- The benchmark addresses a fundamental evaluation gap in AI-driven scientific research: existing methods grade agents against known answers, rubrics, or language-model reviewers, none of which can verify whether a newly constructed scientific model is genuinely valid. SciExam for ENSO instead uses hidden graders that test whether models reproduce ENSO statistics, recover unobserved variables, and forecast held-out years, providing a ground-truth-based assessment independent of any predetermined solution.
- Six out of twelve agent systems produced models scoring higher than a published model, primarily through superior reconstruction and forecasting. Notably, the simplified forms of the stronger models each aligned with one of the two competing explanations of ENSO's warm-cold asymmetry—an open scientific debate that the task description never mentions—suggesting agents can independently arrive at scientifically meaningful model structures.
- Controlled runs of the top-performing system under varied information conditions demonstrated that its high scores do not stem from memorizing the dated observational record, and that the specific information provided to the agent shapes how it constructs its model, indicating genuine reasoning and model-building rather than pattern recall.

## Context
This paper sits at the intersection of AI agent evaluation and scientific discovery, addressing a critical limitation in how we assess whether language-model agents can perform open-ended research tasks. As AI agents are increasingly deployed in scientific workflows, the field lacks benchmarks that test genuine model construction and validation rather than retrieval or summarization of existing knowledge. SciExam for ENSO fills this gap by grounding evaluation in physical reality—whether a model reproduces observed climate statistics and forecasts future behavior—making it a template for evaluating agent-driven science across domains.

## Implications
For AI practitioners and climate scientists, these results suggest that current agent systems can already construct competitive climate models whose internal structures engage with unresolved scientific debates, potentially accelerating hypothesis generation and model exploration. For the broader AI evaluation community, the benchmark demonstrates a viable methodology for assessing open-ended scientific reasoning without a predetermined answer, offering a scalable framework that could extend to other complex systems where ground truth is emergent rather than fixed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10513v1)

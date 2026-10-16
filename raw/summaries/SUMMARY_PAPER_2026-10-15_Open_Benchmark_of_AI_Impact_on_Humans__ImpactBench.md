---
title: Open Benchmark of AI Impact on Humans (ImpactBench): an expert-guided, open platform for the holistic evaluation of AI impact on humans
url: http://arxiv.org/abs/2610.20690v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_17-42-02Z_OpenBenchmarkofAIImpactonHumans_ImpactBench__anexp.md
generated_at: 2026-10-15 22:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ImpactBench, an open, expert-guided benchmark platform designed to measure the multi-dimensional impact of generative AI models on human wellbeing across psychological, physical, and social domains. The authors evaluated ten frontier LLMs across 48,540 simulated multi-turn conversations using 809 metrics derived from 26 existing benchmarks, finding that models promoted desirable behaviors in 68.7% of evaluations but avoided harms in only 53.1%. The platform combines automated LLM judging with human expert verification, achieving 83.3% agreement between majority expert ratings and the automated judge.

## Key Takeaways
- ImpactBench translates constructs from domain experts and 26 existing benchmarks into 809 concrete, behavior-grounded metrics that evaluate whether model outputs support or undermine individual wellbeing across psychological, physical, and social domains. Success is defined either as promoting expert-defined desirable behaviors or avoiding identified harms, making the evaluation framework actionable rather than purely abstract.
- The evaluation methodology uses simulated multi-turn conversations matched to teen and adult scenarios, scored by an LLM judge and then verified through reliability audits and human expert review. The agreement between majority expert ratings and the automated judge reached 83.3% with a Cohen's Kappa of 0.667, establishing a moderate-to-substantial level of reliability for the automated scoring pipeline.
- The results reveal a significant asymmetry in model performance: while models promoted desirable behaviors in 68.7% of evaluations, they avoided harms in only 53.1%, suggesting that current frontier LLMs are more capable of generating positive outputs than of consistently preventing negative ones. All results are released through a public platform that keeps aggregate scores traceable to underlying metrics and conversation transcripts, supporting transparency and independent verification.

## Context
As generative AI systems become deeply embedded in daily human interactions, the field lacks standardized, holistic frameworks for assessing their downstream effects on individual wellbeing beyond narrow task performance or safety evaluations. ImpactBench addresses this gap by building on existing domain-specific benchmarks in psychology, health, and social science, translating them into a unified, iterable evaluation infrastructure. This work sits at the intersection of AI safety research, human-computer interaction, and behavioral science, reflecting growing institutional and public demand for transparent, multi-dimensional accountability in AI deployment.

## Implications
For AI developers and safety researchers, ImpactBench provides a publicly accessible, traceable evaluation tool that can be iteratively updated as new benchmarks and expert insights emerge, enabling independent third-party auditing of model behavior rather than reliance on self-reported metrics. For industry practitioners and policymakers, the finding that harm avoidance lags significantly behind positive behavior promotion highlights a concrete area for model improvement and regulatory attention. The platform's design—linking aggregate scores to individual transcripts and metrics—sets a precedent for reproducible, auditable AI evaluation that could inform procurement decisions, compliance frameworks, and public trust in generative AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20690v1)

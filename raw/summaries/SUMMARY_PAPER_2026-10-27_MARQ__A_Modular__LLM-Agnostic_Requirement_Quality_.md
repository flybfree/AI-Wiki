---
title: MARQ: A Modular, LLM-Agnostic Requirement Quality Assessor Infused with Systems Engineering Knowledge
url: http://arxiv.org/abs/2610.36234v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_20-12-11Z_MARQ_AModular_LLM_AgnosticRequirementQualityAssess.md
generated_at: 2026-10-27 22:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MARQ, a modular and LLM-agnostic prototype system that augments large language models with expert-derived systems engineering knowledge to improve automated requirement quality assessment. By operationalizing INCOSE requirement quality criteria into a criterion-specific knowledge stack, MARQ significantly outperforms off-the-shelf LLM baselines across multiple models, achieving median F1 scores of 0.80, 0.62, and 0.53 for Claude Opus 5, GPT-5.6 Sol, and Gemma 3 12B respectively, compared to baselines of 0.55, 0.52, and 0.18. The study demonstrates that infusing domain-specific SE knowledge into LLM pipelines is a viable and model-agnostic strategy for strengthening trustworthy requirements engineering support.

## Key Takeaways
- MARQ's knowledge stack operationalizes INCOSE requirement quality criteria into modular, criterion-specific components that supplement any underlying LLM, yielding substantial F1 improvements across all three tested models (Claude Opus 5, GPT-5.6 Sol, and Gemma 3 12B) evaluated over 100 executions each on an expert-labeled NASA requirement set, confirming that domain knowledge infusion is a generalizable enhancement pathway rather than a model-specific trick.
- The nature of performance gains is model-dependent: Claude Opus 5 benefits primarily through improved defect detection and false-alarm control, GPT-5.6 Sol gains detection capability and execution-level consistency but at the cost of increased false alarms, and Gemma 3 12B reaches the performance level of off-the-shelf proprietary models while remaining highly variable across runs, indicating that knowledge infusion interacts differently with each model's existing capabilities.
- Criterion-level analysis reveals that gains are concentrated in Correctness and Conformance criteria, with trade-offs between missed defects and false alarms within individual criteria, underscoring that a one-size-fits-all prompt augmentation is insufficient and that criterion-specific interventions are necessary to address the uneven performance across quality dimensions.

## Context
Requirements engineering is a foundational discipline within systems engineering, and defects in requirements propagate downstream to adversely affect development outcomes, safety, and cost. Prior research has shown that off-the-shelf LLMs miss a large share of expert-identified requirement defects, perform unevenly across quality criteria, and produce inconsistent results across repeated executions. This paper addresses a critical gap in the AI-assisted engineering literature by systematically testing whether structured domain knowledge can close the performance gap between general-purpose LLMs and expert-level requirement evaluation, using a rigorous experimental design with multiple models, multiple executions, and expert-labeled ground truth from NASA requirements.

## Implications
For systems engineering practitioners and requirements engineers, MARQ demonstrates that trustworthy LLM-based requirement quality assessment is achievable without proprietary model lock-in, enabling organizations to leverage open-weight models like Gemma 3 12B at performance levels previously reserved for commercial proprietary systems. The findings strongly advocate for human-in-the-loop review workflows, since even augmented models exhibit model-dependent trade-offs between false alarms and missed defects, and criterion-specific interventions remain necessary. For the broader AI research community, this work establishes a reproducible, model-agnostic methodology for injecting domain knowledge into LLM pipelines, offering a template applicable beyond requirements engineering to other safety-critical engineering domains where expert knowledge must be operationalized for reliable AI-assisted decision support.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36234v1)

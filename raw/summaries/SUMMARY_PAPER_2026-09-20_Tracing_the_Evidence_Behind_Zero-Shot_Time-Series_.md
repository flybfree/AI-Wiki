---
title: Tracing the Evidence Behind Zero-Shot Time-Series Forecasting: A Source-First Taxonomy and Audit Framework
url: http://arxiv.org/abs/2609.21425v1
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-18_07-38-58Z_TracingtheEvidenceBehindZero_ShotTime_SeriesForeca.md
generated_at: 2026-09-20 20:11
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper addresses the ambiguity of "zero-shot" in time-series forecasting (TSF), arguing that current definitions—which focus solely on a lack of target-specific parameter updates—fail to specify what evidence or knowledge the system actually utilizes. The authors propose a source-first taxonomy and an audit framework to evaluate zero-shot TSF based on how it accesses information, ensuring that benchmark progress reflects true transferable capability rather than hidden changes in context or resources.

## Key Takeaways
- Current definitions of zero-shot TSF are insufficient because they do not distinguish between different types of evidence usage; for example, a frozen language model with serialized values, a pre-trained time-series model, and a retrieval-augmented system might all avoid parameter updates but rely on fundamentally different sources of transferable knowledge.
- The authors propose a source-first taxonomy that categorizes zero-shot evidence into three primary categories: frozen LLM prior reuse, parametric time-series pretraining, and retrieval-augmented external memory, separating these sources from the specific architectures used to implement them.
- To ensure fair evaluation, the paper introduces an audit framework consisting of four additional dimensions: task interface, forecast object and scoring, prediction-time context, and resource budget; this prevents researchers from inflating performance scores by using larger contexts or higher compute budgets without improving the model's actual generalization capabilities.

## Context
As the field moves toward foundation models for time-series forecasting, there is a growing need to distinguish between "learning" and "retrieving." This paper matters because it identifies a flaw in current evaluation metrics that allows different types of inference techniques to be conflated as "zero-shot," preventing a clear understanding of which technologies actually offer better generalization.

## Implications
For researchers and practitioners, this framework provides a standardized methodology for reporting and auditing zero-shot performance, allowing for more honest comparisons between models. By establishing these boundaries, the industry can move toward identifying truly transferable forecasting capabilities, which is critical for deploying reliable AI in diverse real-world applications like logistics, energy demand, and financial planning where data distribution shifts are common.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.21425v1)

---
title: Evaluating Local Language Model Agents for Reproducible Data Engineering: An Empirical Software Engineering Study of Mobility Workflows
url: http://arxiv.org/abs/2610.11482v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_08-26-46Z_EvaluatingLocalLanguageModelAgentsforReproducibleD.md
generated_at: 2026-10-08 21:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a benchmark of fifteen mobility-workflow tasks to evaluate whether locally deployable, open-weight language model agents can produce correct and reproducible data-engineering artifacts such as scripts, tables, structured files, figures, and reports. The authors test ten local model configurations across one-shot and closed-loop workspace conditions, finding that the closed-loop workspace condition substantially improves artifact-level success rates by 26.7 to 52.0 percentage points among models exceeding two billion parameters, with the strongest configuration achieving 85.3% success.

## Key Takeaways
- The closed-loop workspace condition, where agents can inspect and repair intermediate artifacts, yields pass-rate improvements of 26.7 to 52.0 percentage points over one-shot generation for models larger than two billion parameters, demonstrating that iterative feedback loops are critical for producing valid engineering artifacts rather than merely plausible text or code snippets.
- A quantized 9-billion-parameter model achieves 69.3% artifact-level success while requiring only approximately 6.5 GB of memory on a consumer-grade GPU, showing that meaningful data-engineering assistance is feasible without cloud-scale infrastructure, though reliability remains contingent on model capability and task verifiability.
- The benchmark evaluates complete engineering artifacts using deterministic checkers across data discovery, connector construction, transport-feed processing, semantic enrichment, feature engineering, validation, visualization, and reporting, moving beyond prior evaluations that focus on textual responses or isolated code generation, and providing a reproducible methodology for assessing full agent configurations before deployment in engineering workflows.

## Context
The broader AI landscape has seen rapid adoption of LLM agents as software and data-engineering assistants, yet most evaluations rely on proprietary cloud models and assess outputs at the level of text or single code snippets rather than end-to-end engineering deliverables. This gap is significant because real-world data pipelines require validated scripts, reproducible tables, correct visualizations, and coherent reports, not just syntactically valid code. By focusing on local, open-weight models and complete artifact validation, this study addresses a practical deployment question for organizations that need on-premises, privacy-preserving, and cost-controlled AI assistance for data engineering.

## Implications
For practitioners and industry teams, the findings suggest that local open-weight agents can meaningfully support a subset of software-intensive data-engineering work, but adoption decisions must account for model scale, quantization trade-offs, runtime constraints, and the verifiability of each task. The benchmark and deterministic validation methodology provide a reproducible evaluation framework that engineering teams can use before integrating agent-based workflows into production pipelines, reducing the risk of deploying agents that produce plausible but incorrect artifacts. The results also highlight that tool use and closed-loop inspection are not optional enhancements but essential components for achieving reliable engineering outputs from local models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11482v1)

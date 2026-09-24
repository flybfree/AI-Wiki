---
title: An Open Pipeline and Dashboard for Systemic-Risk Evidence under the EU AI Act's Code of Practice
url: http://arxiv.org/abs/2609.28335v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_16-13-36Z_AnOpenPipelineandDashboardforSystemic_RiskEvidence.md
generated_at: 2026-09-23 22:09
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces the Systemic Risk Index, an open evaluation pipeline and interactive dashboard designed to provide transparent, traceable evidence regarding AI model risks according to the EU's GPAI Code of Practice. By evaluating 18 models across four critical risk categories—CBRN, cyber offense, harmful manipulation, and loss of control—the research demonstrates how different aggregation methods can significantly alter the perceived safety profile of a model.

## Key Takeaways
- The Systemic Risk Index organizes 19 public benchmarks into four specific categories defined by the EU's regulatory framework: CBRN (Chemical, Biological, Radiological, and Nuclear), cyber offense, harmful manipulation, and loss of control. This provides a structured way to evaluate high-risk AI behaviors rather than relying on vague safety claims.
- The research highlights a critical discrepancy in how risk is reported; when switching from average to worst-case aggregation, model scores dropped by 14 to 37 points. This finding suggests that standard "average" metrics may hide significant safety risks or outlier behaviors that are crucial for identifying systemic threats.
- The study validates the reliability of automated evaluation methods, showing that LLM judges achieved a high level of agreement with human graders (kappa scores of 0.78–0.82). Furthermore, a blind audit confirmed that 83% of the sampled transformations preserved the original harm, proving that these evaluations are robust enough to serve as reliable evidence for safety audits.

## Context
As global regulations like the EU AI Act move toward enforcement, there is an urgent need for objective, reproducible metrics to evaluate systemic risk rather than relying on subjective qualitative assessments. This paper addresses a critical gap in AI safety by providing a standardized framework that allows both regulators and the public to scrutinize model behavior under specific, high-stakes scenarios.

## Implications
For practitioners and policymakers, this work provides a blueprint for creating "audit-ready" evaluation pipelines that move beyond abstract safety claims toward verifiable evidence. By enabling users to explore different deployment contexts and aggregation methods, it empowers organizations to identify hidden vulnerabilities before deployment while providing the public with a clearer, more nuanced picture of AI risks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.28335v1)

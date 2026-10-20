---
title: When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories
url: http://arxiv.org/abs/2610.26394v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_13-39-42Z_WhenCodingAgentsOutpaceReview_EvaluatingPRD_Driven.md
generated_at: 2026-10-20 00:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PACE, a benchmark designed to evaluate how well coding agents fulfill complete Product Requirement Documents (PRDs) in mature enterprise repositories, rather than merely resolving isolated issues or generating code from scratch. Across 11 model-scaffold configurations tested on 43 enterprise tasks with 750 expert-audited Code Points, most agents score between 52.1 and 78.1, with GPT-5.6-Sol achieving the highest complete-delivery rate of only 14.0%. The study identifies incomplete implementation and missing integration as the principal bottlenecks, demonstrating that producing individual components does not guarantee a complete, coherent delivery.

## Key Takeaways
- PACE uniquely measures incremental PRD fulfillment in mature enterprise codebases, combining requirement reconstruction, criterion construction, and evidence-based evaluation to connect delivery gaps directly to agent behavior, addressing a critical blind spot in existing benchmarks that focus on issue resolution or from-scratch development.
- Even the top-performing configuration (GPT-5.6-Sol) achieves only a 14.0% complete-delivery rate, and scores cluster between 52.1 and 78.1, revealing that coding agents systematically struggle with integration and completeness rather than isolated component generation, which fundamentally limits their enterprise readiness.
- The evaluation methodology achieves 95.2% agreement with expert consensus and shows lower case-level variation across judging records than repeated agent executions, establishing a reliable and reproducible evaluation framework. Additionally, the benchmark provides actionable feedback for harness refinement: successive harness releases raised mean performance from 59.4 to 63.0 using the same model and task suite, demonstrating that targeted diagnostic improvements can yield measurable gains without model changes.

## Context
As coding agents transition from toy benchmarks and isolated coding challenges into production enterprise environments, the gap between generating syntactically correct code and delivering a complete, integrated product feature remains poorly understood. Existing benchmarks such as SWE-bench focus on bug fixes or single-issue resolution, while from-scratch generation tasks ignore the incremental, multi-component nature of real product development. PACE fills this critical evaluation gap by grounding assessment in actual PRDs and enterprise codebases, providing the field with a realistic measure of whether agents can handle the complexity of mature software systems where integration, consistency, and completeness matter as much as individual code correctness.

## Implications
For industry practitioners deploying coding agents in enterprise settings, this research signals that current agents cannot be trusted to deliver complete product features autonomously, and that human oversight remains essential for integration and completeness verification. The benchmark's diagnostic capability—linking specific delivery failures to agent behavior—offers a practical pathway for teams to iteratively improve agent harnesses and scaffolding without retraining models, potentially accelerating safe adoption of AI-assisted development. For the research community, PACE establishes a reproducible, expert-validated evaluation standard that shifts the conversation from "can an agent write code?" to "can an agent deliver a product?", which is the question that actually determines enterprise viability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26394v1)

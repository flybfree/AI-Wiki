---
title: Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses
url: http://arxiv.org/abs/2610.36114v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_18-25-42Z_ContextIsaPipeline_NotaWindow_InformationAttrition.md
generated_at: 2026-10-27 20:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how LLM agent harnesses silently destroy information before the model ever processes it, arguing that context should be understood as a pipeline rather than a window. Through 720 real runs of a fault-diagnosis agent reading Linux kernel traces, the authors demonstrate that despite the context window being nearly empty (5.75% utilization), one-third of all tool results were truncated by fixed-length JSON slicing, causing systematic data loss that correlated directly with diagnostic accuracy. The work models agent context as a five-stage pipeline, replays production tool results, and runs controlled experiments showing that truncation primarily increases computational cost rather than immediately producing wrong answers.

## Key Takeaways
- The agent harness truncated 3,827 of 11,189 tool results by slicing JSON text at a fixed character length, producing broken JSON in every cut result. This truncation was not uniform: one field appeared in only 4.7% of calls while another field in the same results appeared in 99.3% of calls, depending on where the relevant data sat in the JSON structure. The agent's diagnosis accuracy tracked this exact split, meaning the harness's arbitrary cut point determined which evidence the model could access.
- A controlled experiment revealed that the truncation's primary cost is not immediate accuracy loss but inflated workload: 43% more tool calls, twice the computation, and yield dropping from 0.61 to 0.31. The agent compensated by finding alternative paths to the correct answer, but at substantially higher resource cost. A production trace replay showed a shipped cut deleting all 128 records of a fault's evidence entirely.
- A survey of seven agent frameworks found two that employ the same unsafe fixed-length truncation strategy for tool output, suggesting this is a widespread and underappreciated failure mode in current agent infrastructure. Whether data loss truly causes the accuracy drop remains an open question the authors explicitly leave unresolved.

## Context
LLM agent research has largely focused on maximizing context window size and benchmarking end-to-end task accuracy, treating the model's input as a static window of tokens. This paper challenges that framing by showing that the agent harness—the software layer that assembles prompts from tool outputs—acts as a lossy pipeline that can discard critical information before the model ever sees it. The finding matters because it shifts attention from model capability to infrastructure engineering, revealing that agent failures may stem from data handling bugs rather than model reasoning limitations.

## Implications
For practitioners building agentic systems, this work warns that fixed-length truncation of tool outputs is a silent correctness hazard that inflates cost and can eliminate the very evidence needed for diagnosis, even when the context window appears underutilized. Framework developers should adopt structured, field-aware truncation strategies rather than naive character slicing, and evaluation pipelines should measure information survival at each pipeline stage rather than only final-answer accuracy. The open question of whether truncation directly causes accuracy degradation or merely increases search effort also signals that current benchmarks may underestimate the true fragility of agent pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36114v1)

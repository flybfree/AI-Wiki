---
title: Measuring and Reducing Unusable Replies of LLM Agents
url: http://arxiv.org/abs/2610.19659v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_06-35-49Z_MeasuringandReducingUnusableRepliesofLLMAgents.md
generated_at: 2026-10-14 21:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "reply usability" as a new evaluation dimension for LLM agents, measuring whether a human requester can actually understand and act upon the final reply an agent produces after completing a multi-step task. The authors develop a reader model that simulates the requester's perspective and find that 54% of 480 replies across eight models fail usability checks, with the best-performing model still failing 30% of the time. They demonstrate that appending explicit reply requirements or routing the output through a secondary rewriting model can reduce failure rates to 43% and 36% respectively.

## Key Takeaways
- The authors define reply usability as a distinct property from task completion or report faithfulness, operationalized through a reader model that tests three criteria: whether the reply can be interpreted from information the requester has actually seen, whether it is written in the requester's language, and whether it directly answers the original request. The reader model's agreement with a majority vote of five human annotators falls within the inter-annotator agreement range, validating its reliability as an automated proxy.
- Across eight models spanning seven model families, 54% of 480 agent replies fail the usability test, and even the top-performing model fails 30% of the time. The dominant failure modes involve referencing material the requester never saw (such as internal tool outputs or intermediate reasoning steps) and using labels or terminology the agent coined during its own workflow, making the reply opaque to the human who delegated the task.
- Two practical interventions reduce failure rates: stating explicit requirements for the reply format and content in the agent's instructions lowers failures from 52% to 43% while also reducing errors and omissions, and a secondary model that rewrites the agent's output into requester-friendly language further reduces failures to 36%, a result confirmed by human annotators in a blind comparison study.

## Context
Current LLM agent evaluation pipelines focus on whether the agent completes the underlying task and whether its final report is factually faithful to the work it performed, but they largely ignore whether the human who delegated the task can actually parse, trust, and act on the reply. This gap matters because agents are increasingly deployed in workplace and consumer settings where the end user interacts only with the final message, not with the agent's internal reasoning, tool calls, or intermediate artifacts. The paper fills a critical blind spot in agent evaluation by formalizing a user-facing quality metric and providing reproducible failure taxonomies.

## Implications
For practitioners deploying LLM agents in production, the findings suggest that simply prompting an agent to "summarize your work" is insufficient; explicit instructions about what the requester has already seen, what language to use, and what format to adopt can meaningfully reduce unusable outputs at near-zero cost. For the research community, the reader-model evaluation framework and the secondary-rewriting pipeline offer a lightweight, automatable way to audit agent outputs alongside existing task-success benchmarks, potentially becoming a standard component of agent evaluation suites and a practical safeguard in agent-to-human interaction pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19659v1)

---
title: AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses
url: http://arxiv.org/abs/2610.18090v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_10-11-05Z_AM_Bench_UnderstandingAgentsunderTaskUnderspecific.md
generated_at: 2026-10-14 00:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AM-Bench introduces a benchmark of 48 tasks derived from Terminal-Bench 2.0 and Harness-Bench to systematically evaluate how language-model agents respond to underspecified task instructions across different models and execution harnesses. Through 20,160 evaluation runs spanning five models and four harnesses, the authors demonstrate that different types of information gaps—missing or ambiguous goals, context, and constraints—produce distinct failure modes, and that agent performance rankings shift dramatically depending on the model-harness pairing and the evaluation criterion used.

## Key Takeaways
- Different categories of underspecification produce qualitatively distinct execution deficits: goal gaps directly hinder task completion, context gaps inflate token consumption without necessarily blocking completion, and constraint gaps weaken compliance while still allowing partial task completion. Furthermore, outright missingness consistently degrades success rates more severely than mere ambiguity across all three information domains, suggesting that agents struggle more with absent information than with unclear information.
- Under complete task specifications, a model-harness pairing may appear superior, but these advantages do not persist when tasks are underspecified. Rankings across models and harnesses become highly sensitive to the specific combination of model and harness, as well as to whether the evaluation criterion measures completion, success, or repeat consistency. This means benchmark results obtained under fully specified conditions can be misleading when deployed in real-world scenarios with incomplete instructions.
- The authors estimate, using observed clarification requests and matched fully specified runs, that targeted clarification could recover unfinished work caused by goal or context gaps, but would leave most constraint violations unresolved. This finding motivates a two-pronged strategy: agents should proactively clarify unresolved requirements before taking dependent actions, and evaluation frameworks should test agents jointly across model-harness pairings under varying information conditions rather than in isolation.

## Context
As large language models are increasingly deployed as autonomous agents in software engineering, data analysis, and operational workflows, real-world task instructions are rarely fully specified. Existing agent benchmarks such as Terminal-Bench and Harness-Bench assume complete task descriptions, leaving a significant gap in understanding how agents behave when users provide incomplete, ambiguous, or partially missing instructions. AM-Bench fills this gap by creating a controlled, reproducible evaluation environment that isolates the effects of specific information gaps, enabling researchers to move beyond aggregate success scores and understand the mechanistic ways underspecification degrades agent behavior.

## Implications
For practitioners deploying agentic systems in production, this work underscores that model selection and harness configuration cannot be optimized in isolation from the quality of task specifications users provide. Organizations should invest in structured task-authoring pipelines that minimize missing information and in agent architectures that detect underspecification and request targeted clarification before executing dependent actions. For the research community, AM-Bench provides a standardized, open-source evaluation framework that encourages joint model-harness benchmarking across information conditions, pushing the field toward more realistic and robust assessments of agent reliability in the messy, incomplete task environments agents will actually encounter.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18090v1)

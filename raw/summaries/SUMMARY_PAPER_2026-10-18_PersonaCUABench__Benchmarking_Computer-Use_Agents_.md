---
title: PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas
url: http://arxiv.org/abs/2610.22990v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_06-14-55Z_PersonaCUABench_BenchmarkingComputer_UseAgentsServ.md
generated_at: 2026-10-18 20:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
PersonaCUABench introduces a benchmark that evaluates computer-use agents not on fixed task instructions but on how well they serve diverse user personas who may omit requirements, add constraints, or require approval before consequential actions. Across 74 tasks in 11 domains and 44 personas, the benchmark demonstrates that mean task completion drops by 36% when agents must interact with persona agents rather than receiving clean specifications, revealing a critical gap between benchmark performance and real-world user satisfaction.

## Key Takeaways
- The benchmark holds 74 tasks across 11 domains fixed while varying only the requester, using a persona agent that plays one of 44 personas in four groups to rewrite instructions in natural user language and answer follow-up questions, while the CUA sees only the dialogue and never the original profile or instruction, simulating realistic ambiguity in user-agent interactions.
- Across nine model backbones and 3,330 evaluation runs, task completion falls by 36% relative to original requests. The losses decompose into two distinct failure modes: 59.9% of point-losing cells involve the agent engaging with what the user asked for but still getting it wrong, while 11.2% represent stops or constraints the user explicitly requested that the automated checker scores as failures, highlighting both comprehension and constraint-adherence failures.
- Even when a persona request is fully completed according to the checker, the user persona gives the top satisfaction rating in only 62.7% of cells compared to 84.1% for original requests, demonstrating that task completion metrics alone are insufficient proxies for user satisfaction and that agents frequently satisfy specifications while failing to meet implicit user expectations.

## Context
Computer-use agents have been rapidly advancing in their ability to operate software, navigate interfaces, and complete multi-step tasks, with benchmarks like OSWorld and WebArena driving progress. However, these benchmarks typically provide fully specified task instructions, creating an evaluation environment far removed from how real users interact with agents—users are vague, add constraints mid-conversation, expect approval gates, and express preferences implicitly. PersonaCUABench addresses this gap by introducing a persona-driven evaluation layer that tests whether agents can elicit requirements, respect constraints, and satisfy users who do not provide complete specifications, shifting the evaluation paradigm from task execution to user service.

## Implications
For practitioners building and deploying computer-use agents, these findings indicate that strong benchmark scores on fixed specifications do not translate into reliable user-facing performance, and that evaluation pipelines must incorporate persona-based interaction testing, constraint adherence scoring, and user satisfaction metrics alongside traditional completion rates. For the broader AI research community, the 36% performance drop and the satisfaction gap between completed tasks and user approval suggest that future agent training should incorporate conversational requirement elicitation, explicit constraint handling, and approval-seeking behaviors as core capabilities rather than optional features, fundamentally reshaping how agents are trained, evaluated, and deployed in production settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22990v1)

---
title: Do Coding Agents Still Need a Debugger? Frontier-Model-Based Fault Localization at the Accuracy Ceiling
url: http://arxiv.org/abs/2610.36015v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_17-20-31Z_DoCodingAgentsStillNeedaDebugger_Frontier_Model_Ba.md
generated_at: 2026-10-27 20:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether frontier coding agents (Sol 6.1, Luna 6, and Qwen 3.8) still benefit from interactive debugger assistance for fault localization, or whether their static reasoning capabilities have advanced sufficiently to localize faults from source code alone. The authors seeded 610 single-line faults into 144 LeetCode solutions, applied behavior-preserving transformations to stress-test the agents, and measured localization accuracy with no, optional, or encouraged debugger use. The central finding is that current frontier agents already localize 96.7–99.9% of faults without any tools, and debugger assistance provides only marginal additional gains at a substantial token cost.

## Key Takeaways
- Without any tool assistance, the three frontier agents localized 98.2 to 99.9% of faults in original programs and 96.7 to 99.9% in transformed programs. Accuracy degradation was concentrated specifically where transformation recipes restructured loops and conditions, indicating that the remaining errors are narrow and structural rather than general reasoning failures.
- Encouraged debugger assistance removed 63% and 61% of Luna 6's and Qwen 3.8's remaining transformed errors, yielding gains of only +2.1 and +1.3 percentage points respectively, but at a cost of 14.7 to 27.0 times the token usage. Sol 6.1 maintained 99.9% accuracy regardless of whether assistance was offered, suggesting it already operates at the practical accuracy ceiling for this task.
- When debugger use was optional rather than mandated, Luna 6 and Qwen 3.8 still gained +1.5 and +1.3 points, yet the agents actually invoked the interactive debugger in only 0.2 to 6.2% of runs. The agents overwhelmingly preferred executing the program over stepping through it interactively, yet retained most of the accuracy benefit from that minimal tool use.

## Context
This work sits at the intersection of automated program repair, fault localization, and agentic coding systems, a rapidly growing area where LLM-based coding agents are increasingly deployed in software engineering pipelines. Earlier research established that coding agents struggled with both static execution tracing and interactive debugger operation, making tool-assisted fault localization a necessary crutch. This paper directly tests whether that crutch is still needed by frontier models, using a rigorous experimental design with 610 seeded faults, 144 programs, and five behavior-preserving transformation recipes to probe robustness. It contributes a concrete accuracy-ceiling measurement that challenges the assumption that tool augmentation is always beneficial for modern coding agents.

## Implications
For practitioners building agentic coding pipelines, the findings suggest that mandating debugger integration for fault localization on short, precisely specified programs may be unnecessary and wasteful, since frontier agents already achieve near-perfect accuracy from source code alone and the marginal gains come at 15–27× token cost. For the research community, the paper highlights that the remaining failure modes are narrowly tied to loop and condition restructuring, pointing toward targeted improvements in program-structure reasoning rather than broad tool-access strategies. Industry teams deploying coding agents should weigh the token economics of optional versus encouraged tool use, as the data shows agents self-select minimal tool invocation while still capturing most of the available accuracy benefit.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36015v1)

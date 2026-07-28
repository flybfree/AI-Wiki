---
title: SQBench: A Benchmark for Evaluating Task Delivery by Language-Model Agents in Production-Oriented Workflows
published: 2026-07-25T09:55:31Z
authors: Summer Sun
url: http://arxiv.org/abs/2607.23123v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SQBench: A Benchmark for Evaluating Task Delivery by Language-Model Agents in Production-Oriented Workflows

## Abstract
Existing evaluations of large language models cover knowledge, reasoning, coding, and tool use, but they rarely treat a verifiable deliverable produced within a constrained workflow as the unit of evaluation. We introduce SQBench, a benchmark for evaluating production-oriented task delivery by language-model agents. SQBench v1.0 contains 220 standardized tasks organized into L1 atomic capabilities, L2 composite skills, and L3 business scenarios. Each task requires an agent to process input assets, use available tools, and produce an explicitly specified deliverable. The evaluation first computes functional Completion and then derives Risk Penalty and Performance from independently evidenced triggers in a 10D Risk Matrix. A Strict Pass requires Completion = 1 and Risk Penalty = 0. We evaluate 27 model configurations under a common protocol, with one run per configuration-task pair. The highest prespecified Weighted Pass@1 is 60.5%. Mean Strict Pass@1 on L3 is 18.5%, and every configuration performs worse on L3 than on both L1 and L2, indicating that delivery under domain constraints is a shared weakness within the current task set. Of 2,348 results with Completion = 1, 113 (4.8%) fail the Strict Pass criterion because of risks such as unverifiable citations, inappropriate resource use, or format violations. These results show that functional completion alone does not fully characterize delivery quality and that risk determinations should be reported separately.

## Metadata
- **Published**: 2026-07-25T09:55:31Z
- **Authors**: Summer Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23123v1)
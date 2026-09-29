---
title: Beyond Token Savings: A Systematic Study of Context Compression in LLM Agents
published: 2026-09-26T21:46:40Z
authors: Ritul Satish, Prasoon Sinha, Akiho Kawada, Neeraja J. Yadwadkar
url: http://arxiv.org/abs/2609.32961v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Token Savings: A Systematic Study of Context Compression in LLM Agents

## Abstract
As LLM agents tackle longer tasks, they increasingly compress growing histories of reasoning, actions, and tool outputs. Compression can reduce token use, but it also changes the information available for later decisions. Existing agentic harnesses bundle decisions about what to compress, when to compress, and how much to remove into fixed policies. A systematic characterization is needed to disentangle these decisions and reveal how each affects task success and execution cost. We systematically vary these decisions across three open-weight models on SWE-bench Verified and Terminal-Bench 1.0. Across nearly 35,000 agent runs, we measure task success, token use, end-to-end latency, and estimated cost. We find that fewer tokens need not mean faster or cheaper execution: on Terminal-Bench with Qwen, policies using roughly one-third as many tokens can take 20-80% longer than the uncompressed agent. Policies with similar overall success can solve different tasks, while the same policy can perform quite differently across models. Our results motivate evaluating compression by its effects on agent execution and tailoring policies to the task, model, and workload.

## Metadata
- **Published**: 2026-09-26T21:46:40Z
- **Authors**: Ritul Satish, Prasoon Sinha, Akiho Kawada, Neeraja J. Yadwadkar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32961v1)
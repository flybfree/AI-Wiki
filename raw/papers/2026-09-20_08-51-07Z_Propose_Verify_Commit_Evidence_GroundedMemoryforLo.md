---
title: Propose, Verify, Commit: Evidence-Grounded Memory for Long-Horizon Multi-Actor Conversations
published: 2026-09-20T08:51:07Z
authors: Zihao Lu, Zhihang Yuan, Lei Shi
url: http://arxiv.org/abs/2609.23465v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Propose, Verify, Commit: Evidence-Grounded Memory for Long-Horizon Multi-Actor Conversations

## Abstract
Long-horizon conversational memory is especially challenging in multi-actor settings, where relevant evidence is distributed across participants and contexts and previously established information may later be revised. We introduce EGMEMORY, which formulates long-horizon multi-actor memory as a searchable state machine that separates persistent message-level evidence from an explicit active state. At write time, adaptive state resolution and an evidence-grounded propose-verify-commit protocol govern how this state evolves. At read time, adaptive evidence navigation iteratively resolves the state and supporting evidence required for a query, using conversational structure to narrow the search space and lexical-semantic relevance to rank candidates. The system operates through prompting and tool use without memory-specific policy training. EGMEMORY achieves 68.2% on GroupMemBench and 77.9% on EverMemBench, outperforming the strongest evaluated baselines by 22.7 and 21.4 percentage points, respectively. It further reaches 73.6% on the dyadic LoCoMo benchmark, demonstrating generalization beyond multi-actor conversations. We will release the codebase upon formal publication.

## Metadata
- **Published**: 2026-09-20T08:51:07Z
- **Authors**: Zihao Lu, Zhihang Yuan, Lei Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23465v1)
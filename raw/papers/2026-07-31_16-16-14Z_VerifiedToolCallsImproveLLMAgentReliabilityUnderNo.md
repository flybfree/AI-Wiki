---
title: Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures
published: 2026-07-31T16:16:14Z
authors: Isham Kalappurackal Mansoor, Abhishek Phadke, Pratip Rana
url: http://arxiv.org/abs/2608.02645v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures

## Abstract
Large Language Model (LLM) agents rely on external tools to perform multistage tasks. Existing agent frameworks typically assume that tool calls are atomic and return binary success or failure signals. However, real-world systems exhibit non-atomic behaviors such as timeouts after dispatch, delayed visibility, and partial state updates. These mismatches lead to reliability issues including duplicate actions, task success, and unnecessary tool executions. A lightweight, verification-aware tool wrapper is introduced that augments tool calls with postcondition verification, verify-before-retry logic, and idempotency keys. The approach is evaluated in a controlled simulated environment with injected non-atomic failures across multiple task templates. The results demonstrate that the proposed method significantly reduces duplicate actions, while maintaining comparable task success rates. Overall, the findings suggest that strengthening tool interaction semantics is a promising direction for improving LLM agent reliability without requiring modifications to the underlying language model.

## Metadata
- **Published**: 2026-07-31T16:16:14Z
- **Authors**: Isham Kalappurackal Mansoor, Abhishek Phadke, Pratip Rana
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02645v1)
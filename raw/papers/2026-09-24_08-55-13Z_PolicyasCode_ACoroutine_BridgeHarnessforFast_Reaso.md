---
title: Policy as Code: A Coroutine-Bridge Harness for Fast-Reasoning Reliability on CAR-bench
published: 2026-09-24T08:55:13Z
authors: Ivan Matveev
url: http://arxiv.org/abs/2609.29251v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Policy as Code: A Coroutine-Bridge Harness for Fast-Reasoning Reliability on CAR-bench

## Abstract
CAR-bench evaluates whether tool-using agents stay reliable under real-world uncertainty, executing every tool inside the evaluator so that each tool-result exchange is a separate agent round-trip. A conventional next-action agent can batch parallel tool calls, but a chain of dependent calls costs it one model call per round of results. We present a coroutine-bridge harness in which the model's only action is to emit a Python program that blocks and resumes in place across evaluator tool exchanges. This decouples model invocation from tool round-trips: on the public test split the agent uses a median of two model calls against seven agent turns per task, resolving a full multi-turn task in a median of 1.8 s of model latency on Cerebras gpt-oss-120b. Because the action surface is executable code, deterministic CAR-bench policies are encoded directly as logic in the tool layer rather than as prompt rules, enforcing compliance at zero reasoning cost. On the official hidden evaluation the harness won Track 2 with 60.0% Pass^3, 4.5x the organizer baseline, at the lowest estimated cost and the fastest median task latency (3.14 s) of any entry scoring above that baseline; the same unchanged harness reproduced an identical 60.0% Pass^3 on GPT-5.5 in the Open track, matching frontier-model agents. A single static prompt, appended with per-task state at the tail, stays byte-identical across calls and across tasks: the frozen submission prompt served 78% of input tokens from cache (86.6% across its warm tail), against 73% over a three-week development corpus in which prompt edits repeatedly reset the cache. This compounds the few-call design into a small fraction of nominal input compute.

## Metadata
- **Published**: 2026-09-24T08:55:13Z
- **Authors**: Ivan Matveev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.29251v1)
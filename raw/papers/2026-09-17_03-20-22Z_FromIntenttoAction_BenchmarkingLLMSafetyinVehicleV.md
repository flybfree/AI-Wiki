---
title: From Intent to Action: Benchmarking LLM Safety in Vehicle Voice Command Authorization
published: 2026-09-17T03:20:22Z
authors: Diba Afroze, Xingli Zhang, Yazhou Tu, Xiali Hei
url: http://arxiv.org/abs/2609.19630v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Intent to Action: Benchmarking LLM Safety in Vehicle Voice Command Authorization

## Abstract
Large language models (LLMs) are increasingly integrated into vehicle voice assistants. But linking natural-language requests to vehicle functions creates a safety-critical authorization problem. Before executing a command, the system must choose whether to execute, refuse, clarify, require confirmation, defer to manual control, trigger an emergency response, or make no tool call. To our knowledge, prior evaluations do not isolate this pre-action decision across speaker role, authentication status, vehicle state, and tool availability. We introduce a 202-scenario benchmark with Reference Decisions under a seven-class taxonomy. We evaluate two local open-weight models and three API-based LLMs using Decision Alignment and safety-specific error metrics. Alignment ranges from 40.1% for Llama 3.2 3B to 89.1% for Gemini 3.1 Pro Preview. The API-based models score between 83.2% and 89.1%, with no statistically significant differences among them. Even these models produce two to three False Executes among 161 non-execution scenarios, and persistent errors remain in confirmation and manual-control decisions. A controlled Llama 3.2 3B ablation increases alignment to 40.1% under the structured authorization policy, versus 28.2-29.2% under schema-only and generic-safety baselines, but it does not eliminate False Executes. Structured LLM decisions are therefore insufficient as a standalone safety mechanism, and deployment requires an independent enforcement layer that verifies tool permissions and vehicle-state constraints before invoking any vehicle function.

## Metadata
- **Published**: 2026-09-17T03:20:22Z
- **Authors**: Diba Afroze, Xingli Zhang, Yazhou Tu, Xiali Hei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19630v1)
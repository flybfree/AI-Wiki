---
title: Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents
published: 2026-10-19T11:59:57Z
authors: Zhenyu Zhang, Kewei Fu, Yongqi Tong, Chenzhi Zheng, Wei Wu, Jiang-Ming Yang, Jianshe Li
url: http://arxiv.org/abs/2610.26233v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents

## Abstract
Tool-using voice agents often leave users waiting after speech ends, even when actionable information arrives earlier in the request. Speculative approaches begin work during speech, but chunk-bounded or interrupt-on-update generation can truncate a tool call before its arguments are complete. This couples computation time to speech updates, limiting useful work completed in advance. We introduce Heartbeat Thinking, which handles updated input through new Thinker invocations while allowing ongoing invocations and dispatched tools to finish. Periodic invocations read the latest partial transcript and a shared record of completed reasoning and tool results. These results help resolve missing arguments and initiate dependent calls, allowing preparation to progress across speech updates. Across SpeechFCEval, FDBench v3, and AudioCRAG, Heartbeat improves aggregate speculative tool coverage or retrieval reuse over a SHANKS-style windowed baseline, with benchmark-dependent effects on final task quality. On FDBench v3, it increases tool coverage by 16 percentage points and reduces mean final-response latency by 36.4\%. The results show that heartbeat thinking paradigm preserving ongoing computation during speech can turn listening time into reusable preparation for faster and more capable voice-agent responses.

## Metadata
- **Published**: 2026-10-19T11:59:57Z
- **Authors**: Zhenyu Zhang, Kewei Fu, Yongqi Tong, Chenzhi Zheng, Wei Wu, Jiang-Ming Yang, Jianshe Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26233v1)
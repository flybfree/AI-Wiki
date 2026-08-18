---
title: AstronOS: A Unified Execution Model and Runtime for Long-Horizon Agentic Systems
published: 2026-08-17T10:33:28Z
authors: Zhenhang Nie, Gui Zheng, Xudong Sun, Tailong Zhu, Bin Zhang
url: http://arxiv.org/abs/2608.16381v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AstronOS: A Unified Execution Model and Runtime for Long-Horizon Agentic Systems

## Abstract
Agentic systems often organize execution and state around a single conversation, model invocation, or agent instance, even when real work spans many calls and stages. We introduce a unified execution model that maintains a work item's persistent identity and versioned authoritative state across calls. Each step receives input scoped to a specific state version and new material; a result advances state only after validation and recording. We implement selected paths of this model in AstronOS using Cases, Tasks, and Scenario Packs across central and local execution. We compare five complete strategies for carrying an established software-version update plan into a fresh model session: rereading original materials, replaying full history, deterministic text summary, deterministic JSON, and the AstronOS runtime-mediated handoff. Ten controlled tasks are run under all five strategies with three repetitions, yielding 150 included executions. On the single-stage reference family, strategies perform similarly. In the primary three-stage A-C batch, AstronOS passes the frozen scorer in 14 of 15 executions, compared with 0 of 15 for rereading and 2 of 15 for full-history replay; later non-interleaved summary and JSON batches each pass 0 of 15. AstronOS has lower attempt-accounted model-token cost per passing execution, while requiring more execution-window time per attempt. These results associate the complete AstronOS condition with higher end-to-end pass rates across fresh sessions in this benchmark, at a measurable time cost.

## Metadata
- **Published**: 2026-08-17T10:33:28Z
- **Authors**: Zhenhang Nie, Gui Zheng, Xudong Sun, Tailong Zhu, Bin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16381v1)
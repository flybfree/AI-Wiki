---
title: FusionML: Prefill, Not Decode - Mechanism and Boundaries of CPU+GPU Co-Execution on Unified-Memory Apple Silicon
published: 2026-07-24T11:42:17Z
authors: Om Mohite
url: http://arxiv.org/abs/2607.22785v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FusionML: Prefill, Not Decode - Mechanism and Boundaries of CPU+GPU Co-Execution on Unified-Memory Apple Silicon

## Abstract
Apple-Silicon SoCs share CPU, GPU, and Neural Engine over one unified memory system, raising the question of whether transformer inference can be accelerated by splitting single operators across units. Prior attempts, including our own, failed or produced precision-confounded wins. We identify the cause: MLX's lazy-graph scheduler \emph{serializes} cross-stream work whenever a CPU-stream operation consumes an unmaterialized GPU result inside one evaluation graph, so a row-split matmul that runs \x{1.38} faster with materialized inputs runs \x{0.66} slower than GPU-only inside a lazy graph; an eager materialization boundary restores concurrency (\x{1.34}). \sys{} implements a per-layer, contention-aware CPU+GPU row split for transformer prefill built on this fix. Evaluated across five chips and three Apple-Silicon generations, community-replicated, the split accelerates Llama-shaped decoder-block prefill by \x{1.15}--\x{1.38}, unchanged at full 32-block depth, and reaches \x{1.18}--\x{1.25} faster time-to-first-token on a real Qwen2.5-7B checkpoint served through stock MLX-LM, with token-identical outputs and unchanged decode throughput. We characterize the boundaries equally carefully: decode cannot benefit, bound by shared bandwidth co-execution does not add; precision-matched training loses \x{0.86}--\x{0.97} on all five chips; ANE dispatch overhead excludes it at layer granularity; and a no-regression runtime gate becomes self-defeating under memory pressure, where probing an alternative mode evicts the active mode's working set. Code, raw results, and generation transcripts are released.

## Metadata
- **Published**: 2026-07-24T11:42:17Z
- **Authors**: Om Mohite
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22785v1)
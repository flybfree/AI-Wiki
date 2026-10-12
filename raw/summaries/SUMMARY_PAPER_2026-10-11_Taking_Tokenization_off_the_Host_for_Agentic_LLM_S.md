---
title: Taking Tokenization off the Host for Agentic LLM Serving
url: http://arxiv.org/abs/2610.13325v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_10-05-09Z_TakingTokenizationofftheHostforAgenticLLMServing.md
generated_at: 2026-10-11 20:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces GraphTok, a GPU-based tokenizer that executes the full encoding pipeline—including pre-tokenization, byte-pair encoding merging, and token-ID assembly—as a single replayable CUDA graph, eliminating tokenization as a CPU bottleneck in agentic LLM serving. The authors demonstrate that GraphTok reproduces reference token IDs bit-for-bit across multiple model families while delivering 4.7–6.0x speedup over the strongest CPU tokenizer (gigatoken) and enabling a single frontend to sustain the load of 56 GPUs, compared to 296 requests/s with gigatoken and only 18.5 with the default tokenizer.

## Key Takeaways
- Tokenization has become the dominant contributor to time-to-first-token (TTFT) in agentic workloads, even when prefix caching skips most prefill computation, because every request must still be fully tokenized before the cache can be consulted. This shifts a previously negligible CPU stage into the critical path for serving latency.
- GraphTok encodes one million GPT-2 tokens in 1.7–3.2 ms including data transfers, is 2.6–3.9x faster than gigatoken on single-request benchmarks, and up to 18.1x faster than TokTier. In vLLM with cached prefixes, it reduces mean TTFT by 2.1–2.4x, and within a 2-second P99 target, a single Dynamo frontend with GraphTok sustains 518 requests/s of 121k-token traffic—equivalent to the busiest-hour load of 56 GPUs.
- The system is designed for practical deployment: it handles short inputs by routing them to a CPU engine where the GPU cannot win, plugs into unmodified vLLM and NVIDIA Dynamo, and maintains bit-for-bit correctness across GPT-2, Llama 3, Qwen 2.5, DeepSeek-V3, and Gemma 3, ensuring no accuracy trade-offs.

## Context
As agentic AI systems proliferate, workloads increasingly resend long, nearly identical contexts across sequential tool calls, making prefix caching essential for efficiency. However, the tokenization step remains a serial CPU operation that gates access to cached KV states, creating a hidden scalability ceiling for serving infrastructure. This paper addresses a gap in the systems literature where attention has focused on GPU compute and memory optimization while overlooking the CPU-side preprocessing pipeline that now dominates end-to-end latency in high-throughput agentic serving stacks.

## Implications
For practitioners deploying agentic LLM services at scale, GraphTok demonstrates that moving tokenization onto the GPU can multiply effective serving capacity by 1.75–2.5x without any changes to model weights, inference engines, or serving frameworks, directly reducing hardware costs and tail latency. For the broader field, this work signals that CPU-bound preprocessing stages—long assumed to be negligible—must be re-evaluated as first-class optimization targets in the era of long-context, multi-turn agentic inference, potentially reshaping how serving architectures are designed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13325v1)

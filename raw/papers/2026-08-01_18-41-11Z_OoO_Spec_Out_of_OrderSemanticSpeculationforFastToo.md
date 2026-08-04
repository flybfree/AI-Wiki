---
title: OoO-Spec: Out-of-Order Semantic Speculation for Fast Tool Calling
published: 2026-08-01T18:41:11Z
authors: Zhiheng Zhang, Mujie Xu, Feiyu Sun, Zhixin Zhang
url: http://arxiv.org/abs/2608.00814v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OoO-Spec: Out-of-Order Semantic Speculation for Fast Tool Calling

## Abstract
LLMs generate tool calls token by token, even though the function choice and argument values can often be predicted in parallel from the request and tool schema. ToolSpec reduces this cost by drafting schema tokens and retrieving earlier calls, but cannot propose request-specific values absent from either source. We present OoO-Spec, which computes these missing semantics out of order. At request arrival, a Qwen3-0.6B sidecar predicts the function choice and all schema-defined argument slots in one parallel request-level wave while the target begins ToolSpec decoding. The runtime joins the slot values, renders the resulting call as text, and exposes it to subsequent candidate-construction rounds. The target polls without blocking, re-tokenizes a ready hint with its own tokenizer, and remains the sole verifier and commit authority. The sidecar is trained once with LoRA on Qwen2.5-32B teacher traces and used unchanged across Qwen2.5, Qwen3, and Llama targets, without target-specific drafter training. Across seven fully ranked targets and three benchmarks under greedy batch-one decoding, OoO-Spec is fastest among all evaluated methods in all 21 target-benchmark cells, reaching 2.46x-5.34x over autoregressive decoding with an unweighted mean of 3.89x, versus 2.95x for ToolSpec. It also outperforms every evaluated released learned drafter in each comparable cell. Across Qwen3-4B, 8B, 14B, and 32B targets, the same sidecar improves on ToolSpec by 34.1% on average. Its compact semantic payload averages 85 bytes per request excluding protocol metadata, supporting effective split-GPU overlap.

## Metadata
- **Published**: 2026-08-01T18:41:11Z
- **Authors**: Zhiheng Zhang, Mujie Xu, Feiyu Sun, Zhixin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00814v1)
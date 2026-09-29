---
title: Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs
url: http://arxiv.org/abs/2609.32259v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_05-30-18Z_Prefill_FreeCross_FamilyKVCacheTransferforHeteroge.md
generated_at: 2026-09-28 20:43
model: qwen3.6-35b-a3b
---

## Summary
The authors propose HeteroFold, a novel method that enables prefill-free key-value cache transfer between heterogeneous large language model families in multi-agent systems. By keeping both sender and receiver models frozen while aligning structures and calibrating representations, the approach eliminates redundant text-based prefilling without degrading performance. Experimental results demonstrate substantial latency reductions across long-context benchmarks while maintaining parity with standard communication methods.

## Key Takeaways
- HeteroFold solves cross-family KV cache transfer challenges by aligning model structures and mapping the sender's cache into the receiver's space, then calibrating it to preserve the receiver's internal behavior without requiring either model to be fine-tuned or unfrozen.
- The method achieves state-of-the-art performance across six transfer directions, outperforming baselines like Dense Latent and KV Ridge on long-context benchmarks and matching text-based communication accuracy on multi-agent evaluation tasks.
- At a 32K context length, the Llama-3.1-8B to Ministral-3-14B transfer direction yields a 10.7x speedup over native prefilling and remains 1.18x to 1.47x faster than existing prefill-free techniques, highlighting significant efficiency gains.

## Context
As multi-agent LLM architectures increasingly deploy specialized heterogeneous models, the bottleneck of redundant context processing via text-based communication becomes a critical scalability issue. Existing cache reuse mechanisms often fail when transferring between different model families due to mismatches in tokenization, depth, and representation spaces, limiting interoperability in complex agent ecosystems.

## Implications
This work allows practitioners to build more efficient multi-agent systems by drastically reducing inference latency and compute overhead when agents share context across diverse model backends. The ability to reuse cached representations without prefilling enables real-time interactions between heterogeneous models, facilitating the deployment of scalable, cost-effective AI agent networks in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32259v1)

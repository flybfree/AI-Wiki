---
title: KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse
url: http://arxiv.org/abs/2610.13060v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_06-17-10Z_KV_Repurpose_ATestbedforEvaluatingNon_PrefixKV_Cac.md
generated_at: 2026-10-11 20:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
KV-Repurpose is an open-source, vLLM-based testbed designed to evaluate segment-wise KV-cache reuse in large language model serving, moving beyond the conventional limitation of exact prompt-prefix matching. The authors demonstrate that their approach achieves a dramatically higher token-level cache hit rate (63.9% versus 3.3% for prefix caching at 30 GB capacity) under realistic RAG-style workloads, while also identifying clear quality limitations in cross-document reasoning tasks.

## Key Takeaways
- The system integrates cache-aware segment scheduling, prompt construction, capacity management, workload generation, and runtime monitoring into a unified open-source framework, enabling researchers to systematically study KV-cache reuse strategies that go beyond exact prefix matching. This modular design allows practitioners to isolate and evaluate individual components of non-prefix cache reuse in controlled experimental settings.
- Under a Zipfian RAG-style workload where only 20% of requests share a fixed prefix, KV-Repurpose achieves a 63.9% token-level cache hit rate at 30 GB cache capacity compared to just 3.3% for standard prefix caching. Even when prefix caching is given a 1 TB cache capacity, it only reaches a 17.9% hit rate in the same workload, highlighting a fundamental structural limitation of prefix-only approaches when retrieved documents appear after varying system prompts, conversation histories, or dynamic metadata.
- Naive segment reuse largely preserves output quality for single-document question answering and summarization tasks on long-context benchmarks, but the authors explicitly expose clear limitations in cross-document reasoning, indicating that segment-wise reuse is not a universal solution and that task-specific evaluation is necessary before deployment.

## Context
KV-cache management is a critical bottleneck in serving large language models at scale, particularly in retrieval-augmented generation pipelines where the same retrieved document may appear across many requests with different surrounding context. Current production systems like vLLM restrict cache reuse to exact prompt prefixes, which severely limits hit rates in realistic multi-tenant and RAG workloads. KV-Repurpose addresses this gap by providing a reproducible, open-source experimental platform that enables the research community to rigorously evaluate alternative cache reuse strategies before they are adopted in production serving stacks.

## Implications
For practitioners deploying RAG pipelines or multi-tenant LLM services, the results suggest that prefix-only caching leaves the vast majority of KV-cache computation unexploited, and segment-wise reuse strategies could substantially reduce time-to-first-token and serving costs even at modest cache capacities. For the research community, the explicit identification of quality degradation in cross-document reasoning provides a concrete evaluation benchmark and a caution that cache reuse strategies must be validated per task type rather than assumed to be universally safe. The Apache-2.0 licensed codebase lowers the barrier for follow-up work on cache scheduling algorithms, capacity planning, and quality-preserving reuse policies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13060v1)

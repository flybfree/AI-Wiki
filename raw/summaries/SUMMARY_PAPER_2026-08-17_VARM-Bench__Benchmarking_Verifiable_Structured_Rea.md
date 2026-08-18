---
title: VARM-Bench: Benchmarking Verifiable Structured Reasoning in Chinese Abusive Speech Moderation
url: http://arxiv.org/abs/2608.15600v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_07-52-31Z_VARM_Bench_BenchmarkingVerifiableStructuredReasoni.md
generated_at: 2026-08-17 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
VARM-Bench introduces a benchmark for Chinese abusive‑speech moderation that focuses on verifying the deterministic rationales behind moderation decisions. The authors demonstrate that strong label‑level performance can mask serious errors in full moderation records, highlighting a gap between surface classification and complete record integrity.

## Key Takeaways
- Each instance includes a concise natural‑language rationale with explicit anchors for six decision categories: target, target type, target explicitness, author stance, harmfulness label, and fine‑grained category.  
- The deterministic protocol evaluates field correctness, target alignment, output validity, complete‑record agreement, and hidden record errors without using an LLM judge.  
- Results reveal that models can achieve high label accuracy while committing substantial errors in the overall moderation record.

## Context
This work addresses a critical limitation in existing Chinese abuse‑speech benchmarks, which lack a unified representation for verifiable reasoning. By providing a field‑anchored benchmark, VARM-Bench enables systematic comparison of model outputs across different families and prompting strategies.

## Implications
For practitioners developing moderation systems, the findings stress the need to audit full records rather than rely solely on label scores. The benchmark can guide research toward more reliable, auditable moderation pipelines in Chinese social media contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15600v1)

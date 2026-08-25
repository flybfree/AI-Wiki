---
title: OVIBench: Benchmarking Online Video Question Answering under Interruption
url: http://arxiv.org/abs/2608.22279v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_08-12-08Z_OVIBench_BenchmarkingOnlineVideoQuestionAnsweringu.md
generated_at: 2026-08-24 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces OVIBench, a benchmark for online video question answering that explicitly models interruptions such as cancellation, false triggers, and correction requests. The authors demonstrate that existing VLMs often fail to handle these realistic disruptions, while fine‑tuned models on the newly created OVI‑Train dataset achieve substantial improvements.

## Key Takeaways
- OVIBench categorizes interruptions into four types—cancellation, false trigger, correction, and supports both open‑ended and multiple‑choice tasks.  
- The benchmark uses a unified temporal simulation protocol to reproduce interruption timing across generations, enabling reproducible evaluation of interruption understanding.  
- Fine‑tuning on the OVI‑Train set yields significant gains, validating that interruption awareness is trainable.

## Context
Current video QA research typically assumes offline, uninterrupted interactions, which does not reflect how users actually engage with visual language models. This limitation hampers the development of robust systems for real‑world applications where interruptions are common.

## Implications
For practitioners, OVIBench provides a standardized way to test and improve interruption handling, guiding model design toward more user‑friendly behavior. The released dataset and evaluation code will accelerate research in interactive video understanding across industry and academia.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22279v1)

---
title: TELLER: Non-intrusive Cross-Layer Root-Cause Analysis for LLM Inference
url: http://arxiv.org/abs/2608.01975v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_09-39-11Z_TELLER_Non_intrusiveCross_LayerRoot_CauseAnalysisf.md
generated_at: 2026-08-03 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
TELLER is a non‑intrusive framework that enables root‑cause analysis of large language model inference by combining NVTX/CUPTI traces with service logs without altering binaries. It reconstructs per‑request call‑chain trees, aligns log lines to execution steps, and compresses this information using a trace pair encoding tokenizer. Experiments demonstrate that moderate compression reduces trace length by over 80 % while preserving diagnostic quality across both horizontal and vertical views.

## Key Takeaways
- TELLER reconstructs per‑request call‑chain trees from NVTX/CUPTI traces and logs, aligning each log line with the corresponding execution step.  
- The Trace Pair Encoding (TPE) tokenizer compresses slices into compact token sequences that retain parent‑child structure, depth, and duration attributes.  
- A moderate TPE vocabulary cuts trace length by more than 80 % yet achieves the best overall performance on both horizontal and vertical root‑cause analyses.

## Context
LLM inference is increasingly deployed as a continuous service where failures can span multiple layers including model code, backend services, CUDA kernels, and distributed communication. Traditional profilers provide raw timelines that lack request‑level semantics, making cross‑layer diagnosis challenging. This work addresses the need for a unified, non‑intrusive method to capture and compress this multi‑layer execution context.

## Implications
For practitioners deploying LLM services at scale, TELLER offers a practical triage tool that reduces diagnostic overhead while preserving evidence locality. Its compression‑accuracy trade‑off enables faster triage without sacrificing root‑cause insight, supporting more reliable monitoring and rapid incident response in AI inference pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01975v1)

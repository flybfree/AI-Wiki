---
title: Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe
url: http://arxiv.org/abs/2609.05395v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_17-44-52Z_Multi_StepTool_CallingoverKoreanOpenPublicAPIs_ABe.md
generated_at: 2026-09-06 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KOPA-Bench, a benchmark of 145 tasks using Korean government APIs, and EDGE, a data‑synthesis method that builds executable multi‑step tool‑calling graphs by verifying links against live calls. Fine‑tuned with GRPO, the 9B model matches performance of the larger 27B model on both KOPA-Bench and BFCL.

## Key Takeaways
- The benchmark quantifies the gap between open‑source LLMs and multi‑step tool use across real public APIs.
- EDGE generates a dynamic graph that only retains successful tool links, enabling reliable synthesis of executable pathways.
- Fine‑tuning with GRPO on this synthetic data lets a 9B model achieve near parity with a 27B model.

## Context
Open‑source LLMs are required to operate within strict data‑sovereignty rules by using local government APIs. Existing benchmarks lack realistic multi‑step evaluation, limiting progress in deploying compliant agents.

## Implications
This work provides a practical benchmark and synthesis pipeline that can be adopted by developers building on‑premise AI agents for public services. It reduces reliance on proprietary models while improving performance through verified tool chaining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05395v1)

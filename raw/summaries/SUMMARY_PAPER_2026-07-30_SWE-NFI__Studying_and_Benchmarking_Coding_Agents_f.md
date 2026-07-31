---
title: SWE-NFI: Studying and Benchmarking Coding Agents for Non-Functional Improvements
url: http://arxiv.org/abs/2607.27409v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_19-28-32Z_SWE_NFI_StudyingandBenchmarkingCodingAgentsforNon_.md
generated_at: 2026-07-30 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SWE-NFI, a benchmark designed to measure coding agents’ ability to make behavior‑preserving non‑functional improvements beyond functional correctness. The authors evaluate state‑of‑the‑art agents on 188 tasks derived from real pull requests and find that all agents lag behind human developers in overall NFI capability.  

## Key Takeaways
- The benchmark quantifies NFIs through 92 executable rules, showing a clear gap between agent performance (0.0–1.3) and human reference scores (up to 1.5).  
- Despite high functional correctness rates around 70 %, agents fail to achieve comparable non‑functional gains, especially in structural code improvements.  
- The study demonstrates that existing evaluation tools focus on functional tasks, leaving NFIs under‑explored.  

## Context
Current AI research on coding agents concentrates on functional accuracy and benchmark scores such as HumanEval, which ignore the quality aspects developers prioritize. This limitation hampers progress toward truly useful code assistants that can enhance software without altering observable behavior.  

## Implications
For industry practitioners, SWE‑NFI provides a reproducible metric to assess whether coding agents deliver real‑world value beyond correctness. Researchers can use it to guide model training and evaluation, fostering tools that improve maintainability, readability, and performance without breaking functionality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27409v1)

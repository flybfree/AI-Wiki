---
title: From General Agents to RCA Experts: A Self-Evolving Harness for Root Cause Analysis
url: http://arxiv.org/abs/2608.25661v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_11-43-17Z_FromGeneralAgentstoRCAExperts_ASelf_EvolvingHarnes.md
generated_at: 2026-08-26 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents OpsHarness, a self‑evolving harness that leverages the strong general capabilities of modern large language models for automated root cause analysis. Quantitative experiments show that OpsHarness outperforms both bare LLMs and custom RCA agents across two public benchmarks and an industrial deployment, achieving 59.0 % top‑1 accuracy—an improvement of 63.4 % over a general agent alone.

## Key Takeaways
- OpsHarness reuses the existing capabilities of a general LLM instead of building a new RCA model from scratch, thereby gaining speed and cost benefits.
- The harness self‑evolves by converting diagnostic successes and failures into atomic proposals that are verified through a dual‑gate process to avoid overfitting or regression.
- Its layered data plane combines operational knowledge with an idea‑card tool library while the control plane manages setup, diagnosis, evolution, and verification.

## Context
The rapid advancement of general purpose LLMs has shifted research focus from creating specialized diagnostic agents to optimizing how these models are integrated into workflows. This study highlights that harness design is a critical bottleneck limiting LLM performance in production RCA tasks.

## Implications
For practitioners, OpsHarness offers a practical path to higher accuracy without the overhead of full model retraining, encouraging adoption of modular harnesses over monolithic agents. In industry, such self‑evolving frameworks can continuously improve diagnostic quality, reducing downtime and maintenance costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25661v1)

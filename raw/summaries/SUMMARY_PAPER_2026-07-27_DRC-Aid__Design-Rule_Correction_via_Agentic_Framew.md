---
title: DRC-Aid: Design-Rule Correction via Agentic Framework utilizing Inference-Time Large Language Models
url: http://arxiv.org/abs/2607.22761v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-23_21-22-36Z_DRC_Aid_Design_RuleCorrectionviaAgenticFrameworkut.md
generated_at: 2026-07-27 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DRC‑Aid, an agentic framework that automates local design rule violation repair by integrating verification tools with a large language model. It achieves high success rates on complex layouts, reducing violations dramatically compared to baseline methods.

## Key Takeaways
- The deterministic Rule Engine translates verification‑reported DRVs into a bounded set of geometric edits, limiting the search space.
- An off‑the‑shelf LLM selects edits using depth‑first search with backtracking, guided by immediate feedback from Calibre nmDRC/nmLVS to ensure compliance and avoid topology loss.
- A global Memory Bank prevents revisiting previously explored solutions, and the system reaches DRC‑clean, LVS‑equivalent repairs in about 92.5% of cases while cutting total violations by roughly 98%.

## Context
This work demonstrates how large language models can be repurposed for precise geometric reasoning within manufacturing pipelines, moving beyond natural‑language tasks to real‑world engineering constraints.

## Implications
For semiconductor fabrication and PCB design teams, DRC‑Aid offers a scalable way to automate costly manual fixes, improving yield without sacrificing electrical integrity. The approach also sets a benchmark for integrating AI with deterministic rule engines in constrained optimization problems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22761v1)

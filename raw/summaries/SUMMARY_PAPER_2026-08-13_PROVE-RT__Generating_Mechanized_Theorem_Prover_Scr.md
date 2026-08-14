---
title: PROVE-RT: Generating Mechanized Theorem Prover Scripts for Real-Time Systems using LLMs
url: http://arxiv.org/abs/2608.12762v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_03-12-17Z_PROVE_RT_GeneratingMechanizedTheoremProverScriptsf.md
generated_at: 2026-08-13 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PROVE‑RT, an LLM‑assisted framework that generates mechanized theorem prover scripts for PROSA/ROCQ to certify real‑time system schedulability. By using dependency‑aware informal sketches and retrieval of processed documentation, the method produces valid proofs with a success rate of 44.7% on a curated set, outperforming direct prompting of state‑of‑the‑art LLMs.

## Key Takeaways
- The framework combines dependency information from informal sketches with retrieved PROSA documentation to guide LLM generation and achieve reliable script creation.
- Direct prompting of large language models fails to generate valid mechanizations because they lack the specialized PROSA knowledge required for correct abstraction usage.
- Staged skeleton generation combined with proof completion yields a measurable improvement, demonstrating that retrieval‑guided assistance is effective.

## Context
Real‑time systems verification often relies on handcrafted proofs that are hard to automate. While LLMs excel at many natural language tasks, they typically lack domain‑specific technical knowledge needed for formal theorem provers. This work bridges that gap by tailoring LLM prompting with structured provenance data.

## Implications
Practitioners can adopt PROVE‑RT to accelerate schedulability analysis without extensive proof engineering expertise. The approach offers a scalable pathway toward fully automated verification, reducing reliance on manual verification and supporting faster system certification pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12762v1)

---
title: ClinTraceBench: Source-Verifiable Longitudinal Clinical Reasoning over EHR-Derived Dialogues
url: http://arxiv.org/abs/2609.01111v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_11-51-37Z_ClinTraceBench_Source_VerifiableLongitudinalClinic.md
generated_at: 2026-09-01 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ClinTraceBench, a benchmark for evaluating long-term clinical reasoning in large language models using verified EHR dialogues. It tests eight history representation strategies across four model backbones on 6,271 questions and finds that compressed representations lose critical relational information and suffer from higher error rates.

## Key Takeaways
- Controlled T3 injection probes show compression-induced relation loss where only a few injected positives are recovered by Mem0, A-Mem, and llm-summary. - Compressed strategies incur an aggregation tax on multi-visit trends and cross-patient comparisons. - The blind-to-full gap ranges from +29.8% to +62.7% performance drop between GPT-4o-mini and Haiku.

## Context
Longitudinal clinical reasoning is essential for patient care but current LLM implementations rely on compact representations that may obscure temporal signals. Benchmarking these representations helps identify trade‑offs before deployment.

## Implications
Practitioners must prioritize full‑context histories to avoid hidden errors, especially when comparing models across different backbones. The findings guide resource allocation toward maintaining relational fidelity in compressed memory systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01111v1)

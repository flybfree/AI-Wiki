---
title: Investigating Linear Probe Robustness to Linguistic Register, Medical Specialty, and Corpus Shifts in Medical QA
url: http://arxiv.org/abs/2609.01361v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-01-47Z_InvestigatingLinearProbeRobustnesstoLinguisticRegi.md
generated_at: 2026-09-01 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how linear probes trained on LLM hidden states detect factual errors in medical question‑answering, focusing on whether the “truth direction” remains stable when input varies across writing style (register), medical specialty, or dataset source. The study builds a benchmark of MedQA entries rewritten into four styles and grouped with two other exam corpora to test probe transfer. Results show that the truth direction is largely robust to register and specialty shifts but degrades more sharply under corpus changes.

## Key Takeaways
- The mean AUROC loss due to writing style (Δ_register ≈ 0.10) indicates that linear probes are only mildly affected by register differences, suggesting a stable signal in hidden states despite stylistic variation.  
- Medical specialty contributes an even smaller impact (Δ_specialty ≈ 0.03), implying that the probe’s performance is not strongly tied to domain‑specific knowledge alone.  
- Corridor shifts cause larger AUROC drops: MMLU‑medical loses about 0.12 AUROC while MedMCQA suffers a 0.21 loss, roughly twice the register effect, revealing that dataset structure may dominate probe stability.

## Context
Linear probes are widely used to extract interpretable features from LLMs for tasks like error detection, yet their reliability across different data sources remains unexamined. This work isolates three common input shifts in medical QA and demonstrates that probe performance is not uniformly affected, highlighting a need for careful evaluation of dataset‑specific biases.

## Implications
For researchers, the findings suggest that linear probes can be used as reliable error detectors within a single medical corpus but may misbehave when applied to heterogeneous datasets. Practitioners should therefore validate probe outputs across varied sources and consider dataset structure when interpreting probe results.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01361v1)

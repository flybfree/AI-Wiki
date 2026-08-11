---
title: Do All LLMs Know When They're Being Harmful? A Reproducibility Study of Latent-Space Safety Probes Across Model Families
url: http://arxiv.org/abs/2608.08029v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_09-34-22Z_DoAllLLMsKnowWhenThey_reBeingHarmful_AReproducibil.md
generated_at: 2026-08-10 22:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether lightweight MLP probes can reliably detect harmful prompts across different large language models, reproducing results from a single 8B model study. It finds that the probe architecture works similarly on other architectures and scales, with F1 scores within a point of the original LLaMA‑3.1‑8B performance, and that inference non‑determinism does not affect the outcome.

## Key Takeaways
- The lightweight MLP probes achieve F1 scores comparable to guard models 1000 times larger when applied to other model families such as Gemma‑4‑E4B, Mistral‑7B‑v0.3, and Qwen2‑7B across WildJailbreak, BeaverTails, and AEGIS 2.0 benchmarks.
- Reproducing the original pipeline yields F1 scores within 0.37 percentage points of the reported LLaMA values on average and within 0.2 points specifically for BeaverTails, indicating strong reproducibility.
- The final token latent vectors remain identical across seeds, showing that non‑deterministic inference does not introduce variance in probe outputs.

## Context
This work addresses a growing need for efficient safety mechanisms in LLMs, where deploying large guard models is costly and impractical. By demonstrating that simple probes can match the performance of massive models, it highlights a scalable alternative for real‑world deployment.

## Implications
For industry practitioners, these findings suggest that small, trainable detectors can be integrated into existing LLM pipelines without major overhead. Researchers may explore further generalizations to even larger model families and more complex safety benchmarks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08029v1)

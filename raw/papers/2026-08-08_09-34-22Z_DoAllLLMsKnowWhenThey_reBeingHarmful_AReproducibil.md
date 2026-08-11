---
title: Do All LLMs Know When They're Being Harmful? A Reproducibility Study of Latent-Space Safety Probes Across Model Families
published: 2026-08-08T09:34:22Z
authors: Alizishaan Khatri, Dun Li Chan
url: http://arxiv.org/abs/2608.08029v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do All LLMs Know When They're Being Harmful? A Reproducibility Study of Latent-Space Safety Probes Across Model Families

## Abstract
Khatri et al. (2026) [DOI: 10.1109/DSN-W70714.2026.00027] show that lightweight MLP probes on final-layer activations of a single 8B model (LLaMA-3.1-8B) detect harmful prompts at F1 competitive with guard models 1000x larger, using one probe per benchmark. We reproduce this pipeline end-to-end and extend it along two axes the original study leaves open. First, we test whether the result generalizes across other model architecture and scale by training identical probes on activations from models like Gemma-4-E4B, Mistral-7B-v0.3, and Qwen2-7B, using the three benchmarks (WildJailbreak, BeaverTails, AEGIS 2.0). Second, we test how much of the reported performance is affected by non-determinism during inference by repeating extraction under five random seeds and measuring the variance of F1 scores. Our results reproduce the original LLaMA model benchmarks within 0.37 percentage points of the original F1 scores (and within 0.2 points on BeaverTails). We find that the original MLP probe architecture extends to other model families with F1 scores within a point of the values reported for LLaMA-3.1-8B. Our experiments varying seed values reveal an interesting observation: final token latent vectors remained the same for all tested architectures irrespective of the seed values used.

## Metadata
- **Published**: 2026-08-08T09:34:22Z
- **Authors**: Alizishaan Khatri, Dun Li Chan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08029v1)
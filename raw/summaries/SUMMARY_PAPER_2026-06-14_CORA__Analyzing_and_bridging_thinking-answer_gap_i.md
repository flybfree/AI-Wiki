---
title: CORA: Analyzing and bridging thinking-answer gap in Multimodal RLVR via Consistency-Oriented Reasoning Alignment
url: http://arxiv.org/abs/2606.14691v1
type: paper-summary
date: 2026-06-14
source_paper: 2026-06-12_17-54-59Z_CORA_Analyzingandbridgingthinking_answergapinMulti.md
generated_at: 2026-06-14 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates thinking‑answer inconsistency in reinforcement learning with verifiable rewards (RLVR) for large vision‑language models, demonstrating that the mismatch persists both during training and inference. The authors introduce Consistency‑Oriented Reasoning Alignment (CORA), a lightweight consistency reward model combined with Hybrid Reward Advantage Splitting (HRAS), which improves task performance while reducing semantic gaps between reasoning traces and final answers.

## Key Takeaways
- CORA adds a semantic consistency reward that penalizes deviations between the generated reasoning trace and its output, directly addressing the under‑explored inconsistency problem.  
- The hybrid reward splitting strategy stabilizes optimization by balancing task‑specific rewards with consistency penalties, preventing the model from sacrificing task performance for consistency.  
- Experiments across multimodal benchmarks show that CORA yields higher accuracy and more faithful reasoning traces compared to baseline methods.

## Context
The rise of large vision‑language models has enabled them to perform complex reasoning tasks when combined with verifiable rewards, yet existing solutions focus mainly on visual trace quality without ensuring logical coherence. This gap limits the reliability of multimodal AI systems that must produce trustworthy explanations alongside actions.

## Implications
For practitioners, CORA offers a practical plug‑and‑play framework to embed consistency checks into RLVR pipelines, enhancing model transparency and user confidence. In industry, integrating such alignment mechanisms can reduce costly errors in safety‑critical applications where reasoning accuracy directly impacts outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.14691v1)

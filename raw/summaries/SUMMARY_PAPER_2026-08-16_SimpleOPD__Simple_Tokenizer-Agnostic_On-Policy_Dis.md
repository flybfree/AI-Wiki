---
title: SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context Reasoning
url: http://arxiv.org/abs/2608.14277v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_12-57-02Z_SimpleOPD_SimpleTokenizer_AgnosticOn_PolicyDistill.md
generated_at: 2026-08-16 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SimpleOPD, a tokenizer‑agnostic on‑policy distillation method that transfers proof‑reasoning from the long‑context teacher SU‑01 to short‑context student models. It solves challenges such as tokenizer mismatch and response length explosion by aligning only overlapping text spans and using a KL loss with special termination tokens. Experiments show Intern‑S2‑Preview gains 21.2 points on ProofBench, exceeding Gemini‑2.5‑Pro, and improves science benchmarks.

## Key Takeaways
- The method aligns only tokens that occupy identical text spans under the student and teacher tokenizers to handle tokenizer mismatch.
- It uses a student reference KL loss and masks special termination tokens to limit excessive generation length and reduce truncation issues.
- Intern‑S2‑Preview achieves 55.2 points on ProofBench, surpassing Gemini‑2.5‑Pro by 21.2 points.

## Context
Long‑context reasoning is essential for tasks requiring deep logical inference, yet most student models are short‑context limited, creating a gap in practical deployment. SimpleOPD bridges this gap by enabling efficient transfer without costly fine‑tuning or large data.

## Implications
Practitioners can adopt SimpleOPD to quickly upgrade existing student models with reasoning capabilities from larger teacher models, reducing development time and cost. This approach supports scalable AI systems that combine long‑term knowledge with short‑context efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14277v1)

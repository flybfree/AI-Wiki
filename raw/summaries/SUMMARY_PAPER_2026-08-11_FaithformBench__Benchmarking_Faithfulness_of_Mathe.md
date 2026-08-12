---
title: FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation
url: http://arxiv.org/abs/2608.10916v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_13-36-52Z_FaithformBench_BenchmarkingFaithfulnessofMathemati.md
generated_at: 2026-08-11 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FaithformBench, a benchmark for evaluating the faithfulness of autoformalisation systems that translate natural language reasoning into formal statements in proof assistants like Lean. It shows that existing methods often miss cases where invalid inputs are silently corrected and rely on costly or uncertain human annotations.

## Key Takeaways
- The benchmark automatically generates perturbed reasoning steps designed to be invalid, allowing evaluation of both validity preservation on unperturbed examples and invalidity preservation on perturbed ones without requiring expensive ground truth.
- Many autoformalisation systems exhibit sycophancy, meaning they transform clearly wrong inputs into provable statements, indicating a trade‑off between preserving correctness and preserving incorrectness.
- The most valid fine‑tuned models also show the highest levels of sycophancy, suggesting that improving one aspect may degrade the other.

## Context
Autoformalisation aims to bridge natural language reasoning with formal verification, but current evaluation methods are limited by reliance on scarce annotated data or black‑box LLM judges. This work provides a lightweight alternative that can be applied broadly across diverse mathematical datasets and systems.

## Implications
For researchers, FaithformBench offers a practical tool to compare AF implementations under realistic conditions. For practitioners in AI safety, the findings highlight the need for safeguards against silent correctness injection in automated reasoning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10916v1)

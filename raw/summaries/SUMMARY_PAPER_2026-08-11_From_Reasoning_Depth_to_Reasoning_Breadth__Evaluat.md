---
title: From Reasoning Depth to Reasoning Breadth: Evaluating Multi-Point Associative Reasoning in Large Language Models
url: http://arxiv.org/abs/2608.10444v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_03-58-23Z_FromReasoningDepthtoReasoningBreadth_EvaluatingMul.md
generated_at: 2026-08-11 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MPAR-Bench to evaluate reasoning breadth in large language models by measuring multi-point associative reasoning where a model must infer a hidden target from diverse clues. It finds that while reasoning depth improves accuracy, reasoning breadth is not automatically enhanced and remains vulnerable to perturbations across English and Chinese tasks.

## Key Takeaways
- The benchmark shows that accuracy drops 9–18 percentage points in English and 5–12 in Chinese when perturbations such as clue masking or order shuffling are applied, indicating brittleness of breadth. - Thinking mode improves standard-setting accuracy especially in English but does not consistently reduce sensitivity to these perturbations. - Extended reasoning can overturn an initially correct hypothesis, revealing that depth alone does not guarantee robust breadth.

## Context
Current AI research focuses on extending reasoning depth through longer chains, yet few benchmarks test the ability to process multiple semantic directions simultaneously. This gap limits understanding of how models integrate diverse clues into a coherent answer.

## Implications
Practitioners should design evaluation frameworks that explicitly probe reasoning breadth rather than assuming it scales with depth. Future model development must balance both capabilities to produce reliable and versatile outputs in multilingual settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10444v1)

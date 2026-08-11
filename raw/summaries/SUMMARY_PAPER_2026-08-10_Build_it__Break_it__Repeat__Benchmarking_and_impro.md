---
title: Build it, Break it, Repeat: Benchmarking and improving LLM-manipulated disinformation detection in social media posts
url: http://arxiv.org/abs/2608.09510v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_12-13-41Z_Buildit_Breakit_Repeat_BenchmarkingandimprovingLLM.md
generated_at: 2026-08-10 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new iterative framework called Build it, Break it, Repeat (BiBiR) to test how large language model detectors handle adversarial transformations of disinformation posts. Over five rounds the best breakers achieved a 95% label flip rate while keeping meaning intact and the best builder reached 72.68% accuracy, beating baselines by fifteen points.

## Key Takeaways
- The adaptive iterative method reveals detector weaknesses that static benchmarks miss because it repeatedly applies back‑translation and persona‑based rewrites to evade classification.
- Breakers combine back‑translation with LLM persona rewriting to flip labels at 95% while preserving original meaning, showing that semantic stability can be maintained under heavy transformation.
- The top builder uses a dynamic anchor switching (DASS) triplet contrastive model achieving 72.68% accuracy, surpassing fine‑tuned e5‑small LoRA by fifteen percentage points on the most robust breakers.

## Context
Current AI safety research focuses on static evaluation of detectors against fixed datasets, which fails to capture real‑world adversarial tactics that evolve as models improve. This work bridges that gap by simulating continuous evasion attempts, providing a more realistic stress test for LLM‑based disinformation detection systems.

## Implications
For industry practitioners, the BiBiR framework offers a practical way to continuously benchmark detector robustness against evolving manipulation techniques. Practitioners should integrate iterative testing into their pipelines and also conduct semantic preservation analysis to avoid false positives caused by meaningful claim changes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09510v1)

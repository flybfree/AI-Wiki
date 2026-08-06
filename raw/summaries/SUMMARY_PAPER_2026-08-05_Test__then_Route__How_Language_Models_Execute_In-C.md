---
title: Test, then Route: How Language Models Execute In-Context Conditional Rules Across Models and Languages
url: http://arxiv.org/abs/2608.04183v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_19-40-30Z_Test_thenRoute_HowLanguageModelsExecuteIn_ContextC.md
generated_at: 2026-08-05 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models implement conditional rules given in prompts by examining whether the model builds a separate test and routing mechanism. Experiments using activation patching across multiple models and languages reveal that the predicate is localized to a specific residual layer while the answer routing occurs elsewhere, supporting modular execution.

## Key Takeaways
- The predicate’s truth value is confined to a mid‑stack residual band, and altering it flips the output with near‑perfect accuracy. - The router operates as a token‑bound mechanism that does not transfer its learned pattern to new rule pairs outside the original set. - In Gemma‑3‑4B the routing transfers at high fidelity across languages, indicating language‑independent execution.

## Context
Large language models are expected to follow arbitrary in‑context conditionals without explicit hardware changes, yet their internal mechanisms remain opaque. This study provides empirical evidence that such behavior is achieved through localized signal propagation rather than a universal abstract module.

## Implications
Understanding the modular nature of rule execution can guide more efficient model design and debugging. Practitioners may leverage this insight to isolate failures in conditional logic without retraining entire networks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04183v1)

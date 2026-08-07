---
title: FOCUS: Decoupling Expert Personas in LLMs to Enhance Domain Expert Capabilities
url: http://arxiv.org/abs/2608.05611v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_05-13-59Z_FOCUS_DecouplingExpertPersonasinLLMstoEnhanceDomai.md
generated_at: 2026-08-06 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FOCUS, a method that decouples expert personas within large language models to improve domain expertise without causing cross-domain interference. Experiments on financial, legal, medical and cross‑domain tasks show higher accuracy than prior approaches. The authors demonstrate that orthogonal decomposition and gated activation reduce unwanted persona coupling.

## Key Takeaways
- FOCUS extracts expert persona vectors from LLMs then applies orthogonal decomposition to separate domain‑specific personas.
- A gating module dynamically activates the correct persona based on task context, preventing aggressive behavior in high‑caution domains or excessive conservatism in risk‑sensitive ones.
- The two‑stage training with a gated selection regularizer enables accurate performance on both single‑domain and cross‑domain benchmarks.

## Context
Current LLM applications often suffer from persona leakage where knowledge from one domain contaminates another, limiting reliability. Decoupling experts is needed to tailor models for specialized fields while maintaining safety and efficiency.

## Implications
This work provides a scalable framework that can be integrated into existing persona control pipelines, offering practitioners more controllable and trustworthy AI assistants across regulated industries such as healthcare and finance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05611v1)

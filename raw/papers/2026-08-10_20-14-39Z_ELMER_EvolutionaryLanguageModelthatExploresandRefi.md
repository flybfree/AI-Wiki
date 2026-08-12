---
title: ELMER: Evolutionary Language Model that Explores and Refines
published: 2026-08-10T20:14:39Z
authors: Matthew Siper, Ahmed Khalifa, Julian Togelius
url: http://arxiv.org/abs/2608.10196v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ELMER: Evolutionary Language Model that Explores and Refines

## Abstract
Program evolution can measure whether a mutation helped, but it rarely controls how far the mutation moves in behavior space. Syntactic edit size is an unreliable proxy: a small code change can alter nearly every action, while a larger rewrite can preserve the same execution trace. We introduce an Evolutionary Language Model that searches over natural-language policy descriptions and compiles typed programs for execution. A fully fine-tuned Qwen3-8B model learns three task-conditioned operations: conditional semantic mutation, natural language to domain-specific language (GPTL) compilation, and GPTL to natural language translation. The model is fine-tuned with conditional input on the mutation strength (low, medium, high) using Direct Preference Optimization (oDPO). Across 252 fixed-budget evolutionary searches, oDPO improves both behavioral calibration and finite-budget search efficiency. Natural-language attains the highest observed held-out fitness. Our analysis shows that the condition input (mutation strength) systematically changes semantic edit composition and that language mutations preserve more parent fitness at matched small-to-moderate behavioral displacement. These results show that language can serve as a steerable, execution-grounded search representation over executable program space.

## Metadata
- **Published**: 2026-08-10T20:14:39Z
- **Authors**: Matthew Siper, Ahmed Khalifa, Julian Togelius
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10196v1)
---
title: SDARE-Bench: Evaluating Large Language Models on Conversational Stigma Detection and Response in Dyadic and Group Dialogue
url: http://arxiv.org/abs/2609.01548v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_17-15-22Z_SDARE_Bench_EvaluatingLargeLanguageModelsonConvers.md
generated_at: 2026-09-01 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SDARE‑Bench, a novel benchmark that evaluates large language models on detecting stigma and generating open‑ended responses in both dyadic and group dialogue settings. The study finds that LLMs consistently miss stigma components, especially in group conversations, and produce more stigmatizing advice when social pressure is simulated.

## Key Takeaways
- LLM detection of stigma is weak across 8 models, with the lowest scores on group dialogues where stigma expression is most prevalent.  
- Open‑ended response generation shows higher stigma levels in group settings compared to dyadic interactions, indicating a failure to resist socially harmful advice.  
- Under constructed pressure scenarios, stigma expression rates reach an average of 97.5%, highlighting a critical safety vulnerability.

## Context
Current AI evaluations often rely on static prompts and ignore the dynamic nature of everyday conversations where audience size and social context shift. This gap leaves models vulnerable to producing harmful or stigmatizing content in real‑world advice scenarios, undermining trust and safety.

## Implications
For developers, SDARE‑Bench underscores the need for benchmarks that capture conversational complexity and group dynamics to guide safer model design. Industry practitioners must prioritize these evaluation criteria to prevent AI systems from amplifying stigma in sensitive advisory contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01548v1)

---
title: From Textual Requirements to Microservice Architectures - A Comprehensive Evaluation of LLM-Based Design Synthesis
url: http://arxiv.org/abs/2607.28307v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_14-45-18Z_FromTextualRequirementstoMicroserviceArchitectures.md
generated_at: 2026-07-30 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates whether a large language model can generate complete microservice architectures directly from textual requirements, moving beyond code‑centric decomposition methods. Using OpenAI o3 with zero‑shot and few‑shot prompting on two small systems (Bookstore and PetClinic), the study shows that few‑shot prompts improve both structural agreement and expert perception of quality compared to zero‑shot outputs.

## Key Takeaways
- Few‑shot prompting yields higher precision, recall, and F1 scores for service identification (0.79 vs 0.61) than zero‑shot prompting.
- Communication recovery is more difficult under zero‑shot conditions, producing dense architectures with high recall but low precision.
- Expert assessments confirm that few‑shot generated architectures are perceived as more modular, coherent, and plausible.

## Context
The rapid adoption of microservice architectures in modern software engineering creates a need for automated design synthesis tools. Large language models offer a promising approach to bridge the gap between natural‑language requirements and system designs, yet empirical evidence on their reliability remains scarce. This work contributes one of the first systematic evaluations under realistic prompting conditions.

## Implications
Practitioners can leverage few‑shot examples to guide LLM‑driven architecture synthesis, improving alignment with textual specifications without extensive code input. The findings suggest that prompt engineering is as critical as model capability for delivering usable microservice designs in early design phases.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28307v1)

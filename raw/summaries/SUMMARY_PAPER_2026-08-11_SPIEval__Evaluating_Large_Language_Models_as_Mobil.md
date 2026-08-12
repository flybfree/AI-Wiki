---
title: SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Personal Information
url: http://arxiv.org/abs/2608.10692v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_09-14-53Z_SPIEval_EvaluatingLargeLanguageModelsasMobileAssis.md
generated_at: 2026-08-11 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SPIEval, a human‑curated benchmark that tests large language models as mobile assistants using personal information scattered across ten apps. The study evaluates nine LLMs on 250 tasks and finds the top model GPT‑5.5 (xhigh) reaches only 57.3 % accuracy, while the weakest performs at 16.4 %, highlighting substantial performance gaps.

## Key Takeaways
- 79 % of failures arise from inaccurate information localization; models commit plausible but incorrect details instead of continuing retrieval for verification.
- Fewer than 2 % of retrieval actions use advanced search methods, and search efficiency varies widely across the evaluated models.
- The best‑performing model still scores below 60 %, underscoring that current LLMs cannot reliably handle complex multi‑app personal data tasks.

## Context
The rapid deployment of large language models in mobile assistants creates a need to evaluate their ability to integrate fragmented user data. Existing benchmarks are scarce, making it difficult to benchmark these capabilities against each other or against real‑world performance expectations.

## Implications
These findings reveal fundamental limitations in LLM‑based mobile assistants and call for research into more robust retrieval verification strategies and advanced search techniques. Practitioners should prioritize models that can correctly locate and validate personal information before responding.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10692v1)

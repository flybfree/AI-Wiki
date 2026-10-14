---
title: Reliable Text-to-SQL in Resource-Constrained Settings with Small LLMs via Iterative Retry Workflows
published: 2026-10-12T18:59:25Z
authors: Bilel Abderrahmane Benziane, Xavier Schepler
url: http://arxiv.org/abs/2610.17305v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reliable Text-to-SQL in Resource-Constrained Settings with Small LLMs via Iterative Retry Workflows

## Abstract
Large Language Models (LLMs) have recently improved Text-to-SQL generation, but their computational cost can hinder deployment in resource-constrained settings. This paper evaluates the Text-to-SQL capabilities of small and medium open-source LLMs (1B-8B parameters) under a controlled inference budget, focusing on how model specialization and prompt formulation affect performance. Using the Spider benchmark, we compare multiple prompt representations and assess the accuracy of generated queries. Our results show that SQL-specialized models are consistently more reliable than general-purpose and chat-oriented models at small scales, and that performance can vary substantially depending on the prompt used. To reduce this variability without resorting to larger models, we introduce three lightweight inference workflows that automatically retry with alternative prompts and/or models when failures occur, including an optional syntax-correction step. These workflows significantly improve end-to-end success rates, with a trade-off in additional inference calls. These results demonstrate a practical path to stronger Text-to-SQL performance with small LLMs, by trading modest additional inference cost for higher reliability.

## Metadata
- **Published**: 2026-10-12T18:59:25Z
- **Authors**: Bilel Abderrahmane Benziane, Xavier Schepler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17305v1)
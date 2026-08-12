---
title: REAP: Relation-Aware Elicitation and Parsing for Closed-Book Knowledge Base Construction from LLMs
url: http://arxiv.org/abs/2608.10963v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_14-28-50Z_REAP_Relation_AwareElicitationandParsingforClosed_.md
generated_at: 2026-08-11 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The REAP system is designed to build closed‑book knowledge bases from large language models without fine‑tuning, respecting a 32 billion‑parameter budget. On the AKBC Shared Task 2026 test set it achieves a macro‑F1 of 0.62, with notable strengths on specific relation types such as countryLandBordersCountry (F1 = 0.95), companyTradesAtStockExchange (F1 = 0.73) and hasArea (F1 = 0.77). The approach integrates chain‑of‑thought reasoning, relation‑specific query strategies, and a reasoning gate that filters out invalid inferences.

## Key Takeaways
- REAP constructs parametric knowledge from Mistral‑Small‑24B‑Instruct‑2501 using only inference without any model fine‑tuning, staying within the 32 billion‑parameter limit.  
- The system’s chain‑of‑thought prompting combined with a reasoning gate yields high F1 scores on relation‑specific tasks, especially for geographic and financial relations.  
- Code for REAP is publicly released at https://github.com/yammdd/AKBC-Shared-Task-2026, enabling reproducibility and further research.

## Context
This work addresses the challenge of extracting structured knowledge from language models in a closed‑book setting where model parameters cannot be expanded. It demonstrates that reasoning‑driven prompting can produce high‑quality JSON outputs without costly fine‑tuning, aligning with trends toward efficient, parameter‑constrained AI applications.

## Implications
For industry practitioners, REAP offers a practical method to generate relational knowledge bases from existing LLMs, reducing development time and cost. The results suggest that reasoning‑based extraction strategies can be scaled to larger models while maintaining strict budget constraints, potentially enabling automated data enrichment for diverse domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10963v1)

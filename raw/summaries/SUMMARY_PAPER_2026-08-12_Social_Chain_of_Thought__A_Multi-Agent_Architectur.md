---
title: Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology
url: http://arxiv.org/abs/2608.11420v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_20-38-03Z_SocialChainofThought_AMulti_AgentArchitectureGroun.md
generated_at: 2026-08-12 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Social Chain of Thought (SCoT), a multi-round pipeline that structures medical differential diagnosis as a deliberative collaboration among specialized language models. Experiments show SCoT achieves higher recall than monolithic inference and one‑agent pipelines, especially in the hardest diagnostic cases where multiple specialist rounds help converge on correct diagnoses.

## Key Takeaways
- SCoT delivers superior recall compared to single‑agent baselines by enabling iterative reasoning across agents.
- The advantage is not observed when using a monolithic LLM that performs all reasoning internally.
- Multi‑round specialist interaction is most beneficial for complex, high‑stakes cases where ground‑truth diagnosis is hard to recover.

## Context
Medical diagnostic reasoning remains a critical application of large language models, yet current systems often lack transparency and reliability. This work contributes to the growing body of research on multi‑agent architectures that mimic human collaborative problem solving in specialized domains.

## Implications
For healthcare AI developers, SCoT suggests that modular, agent‑based designs can outperform monolithic solutions when diagnostic complexity demands diverse expertise. Practitioners should consider deploying such pipelines for high‑risk medical queries to improve recall and trustworthiness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11420v1)

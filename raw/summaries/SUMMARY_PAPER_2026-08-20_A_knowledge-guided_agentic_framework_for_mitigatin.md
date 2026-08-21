---
title: A knowledge-guided agentic framework for mitigating patient-context ambiguity in health queries
url: http://arxiv.org/abs/2608.19875v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_10-36-23Z_Aknowledge_guidedagenticframeworkformitigatingpati.md
generated_at: 2026-08-20 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a knowledge‑guided agentic framework that resolves patient‑context ambiguity in health queries before feeding the query to a downstream language model. By constructing hypotheses from a task‑specific knowledge graph and asking targeted follow‑up questions, the system improves answer quality compared with direct prompting or simple rephrasing.

## Key Takeaways
- The framework uses a task‑specific knowledge graph to generate plausible hypotheses for underspecified queries such as symptom diagnosis retrieval and dietary safety classification.  
- It identifies missing patient‑context variables needed to differentiate between those hypotheses and asks follow‑up questions, thereby enriching the prompt with real information.  
- Evaluation across five language models on two benchmarks showed a 57.1 percentage point increase in exact Top‑1 accuracy for diagnosis retrieval and a 77.7 percentage point rise in selective Recall@5.

## Context
This work addresses a persistent challenge in healthcare chatbots where short queries can be interpreted in multiple ways due to omitted patient data, leading to unreliable or unsafe responses. The approach aligns with recent efforts to integrate structured knowledge into generative AI pipelines to improve factual grounding and reduce hallucinations.

## Implications
For clinicians and developers, the framework offers a practical method to enhance chatbot reliability by surfacing needed context before model inference. It can be deployed in clinical decision support tools to lower error rates and build trust with patients relying on automated advice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19875v1)

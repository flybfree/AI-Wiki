---

title: "A Deterministic Agentic Workflow for HS Tariff Classification: Multi-Dimensional Rule Reasoning with Interpretable Decisions"
url: http://arxiv.org/abs/2605.14857v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-14_14-04-46Z_ADeterministicAgenticWorkflowforHSTariffClassifica.md
generated_at: "2026-06-11 10:40"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces a deterministic agentic workflow that maps free‑form product descriptions to HS tariff codes by applying multi‑dimensional rule reasoning, contrasting it with self‑planning large language models. The framework achieves 75 % top‑1 accuracy at four digits and 64 % top‑1 at six digits using Qwen3.6‑plus, while an open‑weight version reaches 84 % top‑1 agreement, highlighting the value of structured, interpretable decision pathways.

## Key Takeaways
- The workflow resolves competing priority rules across material, form, function, essential character, part‑versus‑whole boundaries, and listing versus residual headings through a fixed six‑stage pipeline.  
- Each stage outputs verbatim citations to chapter or section notes, ensuring decisions are interpretable by construction.  
- Offline knowledge engineering of Chinese HS tariff combined with online prompting yields higher performance than end‑to‑end prompting alone.

## Context
The General Interpretive Rules (GIR) require precise multi‑axis classification that current self‑planning LLMs often mishandle, leading to costly misclassifications in trade and customs. This work demonstrates how a deterministic pipeline can outperform frontier models on HSCodeComp benchmarks, offering a practical alternative for high‑stakes applications.

## Implications
For industry practitioners, the structured workflow reduces human review burden while maintaining compliance with GIRs. In AI research, it provides a template for building interpretable reasoning agents that respect hierarchical rule constraints across multiple dimensions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.14857v1)

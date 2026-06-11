---
title: Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning
url: http://arxiv.org/abs/2605.21127v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-20_12-58-01Z_Reasoning_TraceCollapse_EvaluatingtheLossofExplici.md
generated_at: 2026-06-11 10:44
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why explicit reasoning traces disappear after fine‑tuning models on instruction‑response data that lacks such traces. The authors demonstrate a phenomenon called reasoning‑trace collapse where models retain answer accuracy but lose structurally valid reasoning steps. Their framework quantifies trace validity alongside task performance, revealing that standard metrics hide this degradation.

## Key Takeaways
- Standard supervised fine‑tuning can rapidly suppress valid reasoning traces while keeping final answers plausible.  
- Answer‑only evaluation metrics obscure the loss of reasoning structure because they do not require explicit traces to be present.  
- Simple loss‑masking strategies can substantially reduce collapse without needing teacher‑generated reasoning traces.

## Context
The rise of open‑weight reasoning models has highlighted a gap between their training capabilities and downstream adaptation. When fine‑tuning ignores the original trace structure, models may appear competent yet fail to generate coherent intermediate steps, raising concerns about reliability in safety‑critical applications.

## Implications
Researchers and practitioners must adopt structural evaluation metrics alongside final‑answer scores when assessing reasoning models. Ignoring trace validity can lead to deceptive performance, undermining trust in AI systems that rely on explicit reasoning for decision making.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.21127v1)

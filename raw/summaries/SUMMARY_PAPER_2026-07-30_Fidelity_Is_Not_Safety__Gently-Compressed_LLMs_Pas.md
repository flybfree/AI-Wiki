---
title: Fidelity Is Not Safety: Gently-Compressed LLMs Pass Every Data-Free Quality Guard Yet Invent Procedure Steps in Agentic Execution
url: http://arxiv.org/abs/2607.28196v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_13-33-09Z_FidelityIsNotSafety_Gently_CompressedLLMsPassEvery.md
generated_at: 2026-07-30 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why gently-compressed large language models, which satisfy low perplexity, downstream accuracy, and data-free fidelity checks, still exhibit unsafe behavior when deployed as agents. It finds that these models invent procedure steps not present in the original instructions, a phenomenon tied to the coherence of compression errors multiplied by their rate rather than error magnitude alone.

## Key Takeaways
- Gently-compressed LLMs pass perplexity, MMLU, and data-free fidelity tests yet generate agentic steps absent from the SOP.  
- The effect is operator-specific: low-rank truncation induces it while magnitude pruning at identical perplexity does not.  
- A two‑axis statistic (coherent‑fraction and error‑rate) flags failing builds with fixed thresholds across architectures.

## Context
AI practitioners rely on cheap, data-free quality guards to certify model compression, but this study reveals a blind spot in those safeguards when models act as agents. The findings extend the safety discourse beyond static evaluation to dynamic execution contexts where compression artifacts can reshape behavior.

## Implications
For industry and researchers, the paper urges a new screening protocol that evaluates compression coherence before agent deployment rather than relying solely on perplexity or fidelity metrics. Ignoring this blind spot could lead to unintended operational risks in real‑world AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28196v1)

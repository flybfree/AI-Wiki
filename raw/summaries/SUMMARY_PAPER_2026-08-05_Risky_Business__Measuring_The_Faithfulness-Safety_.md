---
title: Risky Business: Measuring The Faithfulness-Safety Tension
url: http://arxiv.org/abs/2608.03745v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_14-38-06Z_RiskyBusiness_MeasuringTheFaithfulness_SafetyTensi.md
generated_at: 2026-08-05 01:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the trade‑off between faithfulness and safety in chain‑of‑thought reasoning models, showing that high faithfulness can coexist with low safety and vice versa. Experiments on a human‑written dataset called HazMart reveal that DeepSeek‑R1‑Llama‑70B is highly faithful but unsafe while QwQ‑32B is safer but less faithful. The authors introduce Targeted Reasoning Replacement (TRR) to intervene in the reasoning chain and replace unsafe thoughts, and demonstrate that representation steering can boost safety without harming performance.

## Key Takeaways
- DeepSeek‑R1‑Llama‑70B achieves 97.5% faithfulness but only 87.7% safety (12.3% unsafe rejection) indicating a strong faithfulness–safety tension.
- QwQ‑32B shows 74.7% faithfulness and 73.9% safety, revealing that robustness can be achieved at the cost of some faithfulness.
- Targeted Reasoning Replacement (TRR) directly edits unsafe thoughts in the chain, and representation steering raises safe behavior by nine percentage points while preserving base capabilities.

## Context
Chain‑of‑Thought prompting is widely used to improve model reasoning, yet monitoring depends on faithful output. The tension between accurate trace fidelity and rejection of harmful reasoning is a fundamental challenge for deploying large reasoning models in real applications.

## Implications
Understanding this trade‑off guides developers toward safer deployment strategies such as TRR and representation steering. Practitioners can prioritize safety without sacrificing core reasoning ability, aligning with ethical AI standards and regulatory expectations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03745v1)

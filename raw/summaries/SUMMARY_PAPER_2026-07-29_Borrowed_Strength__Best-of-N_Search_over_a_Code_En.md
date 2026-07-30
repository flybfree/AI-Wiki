---
title: Borrowed Strength: Best-of-N Search over a Code EncodingBreaks Self-Check Jailbreak Defenses
url: http://arxiv.org/abs/2607.26639v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_09-01-26Z_BorrowedStrength_Best_of_NSearchoveraCodeEncodingB.md
generated_at: 2026-07-29 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper demonstrates that the self‑check defense SAGE can be compromised when two seemingly harmless attacks — an existing code‑completion encoding and a best‑of‑N search — are combined. Together they achieve 67 % success on three open targets and persist at 15 % on a 70B model, while individual attacks stay below 4.7 %.  

## Key Takeaways  
- A self‑check defense can borrow its strength from the target: it asks the model to evaluate the request, causing the four targets to refuse between 32 % and 97 % of the time, which inflates defended coverage even though undefended reach is nearly identical.  
- The ordering of defended versus undefended reach depends on the type of defense; against transform defenses the code encoding retains more undefended reach than character search, whereas gate defenses invert this ordering.  
- A validity defect in our greedy‑decoding pipeline — where a deterministic attack lacks any best‑of‑N variation channel — was identified and repaired, with a one‑line diagnostic that detects it.  

## Context  
AI systems increasingly rely on self‑check mechanisms to curb harmful outputs, but defenses often assume isolated attacks. Understanding how multiple techniques interact is essential for robust security design in generative models.  

## Implications  
For practitioners, this research highlights the need to test defenses against compositional attacks and to validate pipelines for hidden deterministic behaviors that could undermine security guarantees.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26639v1)

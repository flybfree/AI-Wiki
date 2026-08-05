---
title: AutoSND: From Execution Evidence to Structural Policies for Automated Network Dismantling Heuristic Discovery
url: http://arxiv.org/abs/2608.03653v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_13-34-52Z_AutoSND_FromExecutionEvidencetoStructuralPoliciesf.md
generated_at: 2026-08-05 01:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
AutoSND introduces a three‑stage tree search framework that transforms raw execution evidence into structural policies for automated network dismantling. By archiving execution traces, generating local signal‑based policies, and applying them to continue the search, AutoSND discovers higher‑quality and faster disassembly programs than prior LLM‑driven methods.

## Key Takeaways
- Execution evidence is systematically stored across stages to guide later policy creation.  
- Structural policies are built from candidate records, focusing on local signals, neighborhood access, and limited state updates.  
- The final AutoSND‑Q/S candidates achieve superior search performance, stability, and produce interpretable structures using residual degree as a backbone.

## Context
Automated network dismantling remains a manual task despite the rise of large language models that can generate heuristics. This paper addresses the gap between candidate generation and structural guidance by integrating execution feedback into policy formation, highlighting how AI can evolve from output to actionable design principles.

## Implications
Practitioners can leverage AutoSND’s interpretable structure to automate vulnerability assessments without sacrificing efficiency. The approach demonstrates that AI‑driven heuristics can be refined through real‑world execution data, offering a scalable path toward robust system analysis tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03653v1)

---
title: MutMem: Cryptographically Authorized Mutation in Persistent Agent Memory
url: http://arxiv.org/abs/2608.02843v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_19-58-37Z_MutMem_CryptographicallyAuthorizedMutationinPersis.md
generated_at: 2026-08-05 01:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MutMem, a cryptographically authorized mutation protocol for persistent agent memory that records every weight change as a signed transition. It demonstrates high accuracy in long‑term retrieval tasks and robust resistance to poisoning attacks while preserving traceability of each update.

## Key Takeaways
- MutMem records each nontrivial weight change with a housekeeper‑authorized transition, embedding signer epoch, old and new quantized weights, and two domain‑separated SHA‑256 commitments.  
- Poison‑likely content is stored under signed revisable labels that serve as trust evidence during recall, preventing poisoned information from influencing top‑five answers.  
- Evaluation shows 91.8% correct answers on LongMemEval, 74.12% judged accuracy on LoCoMo, and zero injected poison in a 100‑test PoisonedRAG scenario.

## Context
Persistent agent memory must evolve as new evidence emerges without discarding earlier data, creating an attribution challenge between legitimate adaptation and database tampering. This work addresses that challenge by providing a verifiable mutation protocol within the HOM‑AIMOS framework.

## Implications
For practitioners developing long‑term AI agents, MutMem offers a way to guarantee that memory updates are traceable and authorized, reducing risk of hidden poisoning. It also sets a benchmark for integrity‑preserving retrieval systems in LLM applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02843v1)

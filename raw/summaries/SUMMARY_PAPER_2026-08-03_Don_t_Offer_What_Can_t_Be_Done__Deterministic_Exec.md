---
title: Don't Offer What Can't Be Done: Deterministic Executability Gating for LLM Skill Selection at Scale
url: http://arxiv.org/abs/2608.01050v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_07-32-49Z_Don_tOfferWhatCan_tBeDone_DeterministicExecutabili.md
generated_at: 2026-08-03 20:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces deterministic executability gating to prevent LLM skill selection from invoking skills that cannot run given the account state. The system combines semantic matching with a gate that filters out non‑executable candidates, reducing context size and improving efficiency. In production analysis it removed 59% of skill‑description tokens while keeping model behavior unchanged.

## Key Takeaways
- Semantic matching alone retains only 23.1% of messages but the executability gate removes an additional 59.4% of skill‑message pairs, cutting the total skill‑description context by 90.5%.  
- The gate operates on identical exit predicates as the LLM’s selection logic, ensuring that blocked skills never influence model choice when predicate parity is maintained.  
- Counterfactual testing shows a risk‑enriched cohort would have selected a production‑blocked skill in 7.8% of conversations, proving gating prevents non‑executable candidates from shaping outcomes.

## Context
LLM agents often expose many skills to every user query, inflating token usage and potentially causing failures when some skills are unavailable. This work addresses the mismatch between relevance and executability at scale, a recurring challenge in deployable AI systems.

## Implications
Practitioners can adopt deterministic gating to shrink context windows without sacrificing model performance, saving compute resources and improving reliability. The approach offers a template for other multi‑skill agents aiming to balance relevance with operational constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01050v1)

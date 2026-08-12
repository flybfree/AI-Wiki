---
title: ConVAWG: A Retrieval-Grounded Framework for Controlled Synthetic Dialogue Generation in Violence Against Women and Girls
url: http://arxiv.org/abs/2608.11200v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_17-57-34Z_ConVAWG_ARetrieval_GroundedFrameworkforControlledS.md
generated_at: 2026-08-11 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents ConVAWG, a retrieval‑grounded framework that creates CPS‑aligned synthetic dialogues depicting violence against women and girls (VAWG). By generating over 6,000 multi‑turn dialogue events across 200 scenarios with rich metadata, the work demonstrates that high‑quality, domain‑fidelity synthetic conversations are achievable without relying on scarce real data.

## Key Takeaways
- It constructs scenarios from persona seeds, demographic patterns reported by the UK Office for National Statistics, official crime definitions, and retrieved Domestic Homicide Review cases, converting them into hierarchical event timelines to model relational abuse over time.  
- The framework generates multi‑scene role‑play dialogues with targeted activation‑steered toxicity control applied only to appropriate utterances to maintain safety while preserving realism.  
- Evaluation shows strong dialogue quality and domain fidelity across human evaluation, LLM‑as‑Judge assessment, ablations, and downstream tasks.

## Context
Synthetic dialogue generation is increasingly used for studying sensitive domains where real data are hard to obtain or release. Existing approaches often focus on sentence‑level toxicity, overlooking the relational and temporally unfolding nature of abuse. ConVAWG addresses this gap by modeling VAWG as multi‑turn events with rich metadata.

## Implications
For researchers, ConVAWG provides a scalable resource that enables rigorous study of VAWG dynamics without compromising privacy or legal constraints. Practitioners can leverage the framework to develop safer AI systems and inform policy on digital safety for women and girls.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11200v1)

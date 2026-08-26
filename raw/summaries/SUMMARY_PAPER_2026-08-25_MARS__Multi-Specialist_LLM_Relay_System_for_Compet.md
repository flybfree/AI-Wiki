---
title: MARS: Multi-Specialist LLM Relay System for Competitive Programming
url: http://arxiv.org/abs/2608.23918v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_23-51-02Z_MARS_Multi_SpecialistLLMRelaySystemforCompetitiveP.md
generated_at: 2026-08-25 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary  
MARS is a prompt‑only framework that relays programming tasks among several specialized large language models each grounded in a different algorithmic domain such as dynamic programming or geometry. The system retrieves the most relevant specialists, starts with an initial C++17 solution, and iteratively refines it through sandbox testing before normalizing boilerplate in one final pass. On the CodeContests test split with Gemma 4, MARS achieves a 0.624 pass rate at only two pipeline stages, outperforming direct prompting by 14.4 percentage points.

## Key Takeaways  
- Retrieval selects a small team of topic specialists grounded by retrieval‑augmented generation over an algorithm‑theory corpus.  
- The starter writes the first C++17 draft; each turn runs the candidate against public examples in a sandbox, and the active specialist keeps, repairs, or hands off the draft, forwarding a structured packet to the next specialist.  
- A single infrastructure‑fixer pass normalizes boilerplate at the end of the pipeline.

## Context  
Competitive programming pipelines often rely on a single large language model that must decide both task decomposition and algorithmic technique, leading to high variance in token usage and performance. This paper introduces MARS as an alternative that leverages multiple domain‑specific LLMs to share expertise more effectively.

## Implications  
The framework reduces per‑task token spend and lowers wall‑clock cost compared with existing single‑LLM approaches such as CodeSIM, offering a scalable model for developers seeking reliable code generation at reduced expense. Practitioners can adopt MARS’s prompt‑only architecture to improve efficiency without additional infrastructure complexity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23918v1)

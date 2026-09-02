---
title: StateSwap: Probing Support-Elimination Hidden States in Multiple-Choice Questions
url: http://arxiv.org/abs/2609.01081v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_11-13-26Z_StateSwap_ProbingSupport_EliminationHiddenStatesin.md
generated_at: 2026-09-01 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why large language models answer multiple‑choice questions differently when the question is framed as requiring support versus elimination. By using a dual‑framing protocol with minimal prompt changes and an untrained [STATE] token, it shows that activations from these framings are distinct and located in intermediate layers. Swapping these activations alters predictions and improves agreement across framings, providing evidence that the activations drive behavior.

## Key Takeaways
- The dual‑framing protocol reveals separable [STATE] activation patterns that differ between support‑oriented and elimination‑oriented prompts while keeping the target question constant.  
- Interchanging these layer‑specific activations systematically changes model predictions, demonstrating their behavioral relevance beyond random instance substitution.  
- Mean‑difference steering directions derived from the framing contrast produce more bounded layer‑wise responses than matched activation addition directions under this protocol.

## Context
In AI research, probing internal representations with intervention tokens is a growing method to understand how models encode information and make decisions. This work extends that approach to multiple‑choice reasoning, where framing can subtly shift model behavior without altering the underlying task.

## Implications
Understanding these hidden state differences helps developers design more robust question generation systems that are consistent across different phrasings. Practitioners can leverage activation swapping to align model outputs with intended answer keys, improving reliability in educational and assessment applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01081v1)

---
title: Chemical Chain-of-Thought Functions as a Hallucination-Prone Molecular Scratchpad
url: http://arxiv.org/abs/2607.20935v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_05-30-45Z_ChemicalChain_of_ThoughtFunctionsasaHallucination_.md
generated_at: 2026-07-23 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how chain‑of‑thought (CoT) reasoning in chemical language models produces hallucinated structural claims that are often unrelated to the correct answer. Experiments across four model families and twelve tasks reveal a persistent pattern where fabricated SMILES drafts appear alongside accurate responses, indicating that CoT functions as a hallucination‑prone scratchpad rather than a faithful explanation.

## Key Takeaways
- The reasoning trace is causally load‑bearing: perturbing Chem‑R’s fragmented SMILES sketches degrades generation even when the verbal structural claim remains inert.  
- Hallucinations are largely independent of answer correctness, co‑existing with correct responses across diverse chemistry tasks.  
- Model‑specific scratchpad functions exist; Chem‑DFM‑R relies on scaffold, positional, and naming cues while ether‑0 uses SMILES drafts, showing that the same hallucination pattern can be expressed differently.

## Context
Chemical reasoning models are increasingly used to answer complex molecular questions, yet their reliance on chain‑of‑thought traces raises concerns about reliability. This work highlights a gap between surface‑level explanation and actual chemical understanding, prompting researchers to reconsider how CoT is evaluated in AI systems.

## Implications
Treating CoT as direct evidence of faithful reasoning can mislead both developers and users of chemistry AI tools. Process‑level supervision that addresses hallucination in the scratchpad layer will be essential for building trustworthy models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20935v1)

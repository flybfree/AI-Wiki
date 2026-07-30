---
title: Phoneme- vs. Character-Level Targets and Selective State-Space Models for Intracortical Brain-to-Text
url: http://arxiv.org/abs/2607.26751v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_10-46-08Z_Phoneme_vs_Character_LevelTargetsandSelectiveState.md
generated_at: 2026-07-29 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the choice of decoder architecture (GRU versus hybrid Mamba) and target representation (phoneme versus character) affect intracortical brain‑to‑text performance on the Brain-to-Text benchmark. A controlled 2×2 grid was trained with a CTC objective, revealing that GRUs still outperform Mamba hybrids both for phonetic and textual targets after language model rescoring. Error analysis highlights representation‑dependent confusions such as articulatory‑like phoneme errors versus lexical or word‑boundary mistakes.

## Key Takeaways
- The recurrent GRU decoder maintains the highest performance, achieving 12.62 % PER for phonetic targets and 21.19 % WER, compared to Mamba hybrids that do not surpass these scores.  
- Target representation matters: phoneme decoding yields lower word error rates than character decoding, even when using the same GRU architecture.  
- Architectural contributions are distinct; hybrid Mamba models improve on recurrent baselines but still fall short of the best GRU results.

## Context
Intracortical brain‑to‑text systems aim to translate neural activity into spoken language with minimal latency and error. Recent advances in state‑space models like Mamba promise faster training and longer context windows, yet their real‑world impact on clinical applications remains uncertain. This study provides empirical evidence that current recurrent decoders still dominate performance despite newer architectures.

## Implications
For researchers developing brain‑machine interfaces, the findings suggest focusing on hybrid approaches that combine the efficiency of state‑space models with the reliability of recurrent networks may be worthwhile. Clinicians and engineers should prioritize GRU‑based systems for now, reserving Mamba hybrids for scenarios where computational resources allow higher latency tolerance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26751v1)

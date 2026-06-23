---
title: Randomized YaRN Improves Length Generalization for Long-Context Reasoning
url: http://arxiv.org/abs/2606.23687v1
type: paper-summary
date: 2026-06-23
source_paper: 2026-06-22_17-59-53Z_RandomizedYaRNImprovesLengthGeneralizationforLong_.md
generated_at: 2026-06-23 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Randomized YaRN, a training method that boosts long‑context reasoning by mixing YaRN positional extrapolation with randomized positional encodings and a length curriculum. Experiments on BABILong and MRCR show consistent gains from 16K to 128K context lengths when the model is trained only on <8K data, outperforming standard fine‑tuning especially at far out‑of‑distribution lengths.

## Key Takeaways
- Randomized YaRN exposes short‑context tokens to OOD positional encodings sampled from a larger range, enabling better extrapolation.  
- The method improves reasoning performance across a wide spectrum of context lengths, with the largest improvements observed at very long sequences.  
- Compared to simple fine‑tuning, Randomized YaRN consistently yields higher scores on BABILong and MRCR benchmarks.

## Context
Current LLMs are limited by their reliance on short‑context pretraining, which hampers performance when handling extended inputs. This work addresses that limitation by designing a training paradigm that deliberately introduces out‑of‑distribution positional information, thereby enhancing the model’s ability to generalize beyond its original context window.

## Implications
For practitioners developing long‑form applications such as document analysis or multi‑turn dialogue systems, Randomized YaRN offers a low‑cost way to improve robustness without extensive additional data. The technique could become a standard component in pipelines targeting high‑scale reasoning tasks where context length is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.23687v1)

---
title: Compositional Failure in Audio-Visual LLMs: Late-Layer Prior Dominance Under Cross-modal Conflict
url: http://arxiv.org/abs/2608.27785v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-27_23-48-10Z_CompositionalFailureinAudio_VisualLLMs_Late_LayerP.md
generated_at: 2026-08-30 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why audio-visual language models fail when presented with conflicting visual and auditory evidence, finding that late-layer priors dominate over earlier layers. They observe near identical performance across three alignment configurations despite differing output priors, indicating a compositional failure mode called prior dominance. The analysis shows commitment to the preferred answer pattern is localized at 25.5 ±1 layers.

## Key Takeaways
- The models exhibit near‑identical exact‑string accuracy on AVHBench for three different audio‑video alignment setups, suggesting that late‑layer priors override input differences.
- A 32.3 % drop in InternVideo2’s cross‑modal conflict performance and a 17.3 % instruction‑following failure highlight the impact of prior dominance under incompatible evidence.
- Mechanistic inspection reveals answer bias is concentrated at ~25 layers, indicating that deeper layers lock in a weakly grounded pattern rather than integrating conflicting cues.

## Context
Audio‑visual language models aim to fuse synchronized modalities into coherent judgments, but real‑world data often contains mismatches. Understanding why such conflicts are mishandled informs the design of robust multimodal architectures and evaluation protocols.

## Implications
Practitioners must treat late‑layer priors as a potential source of systematic error rather than a sign of learning efficiency. Mitigating prior dominance could improve real‑world deployment where visual and auditory cues clash, reducing misclassification rates in safety‑critical applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27785v1)

---
title: Order Matters: LVLMs as Judges for Temporal Reasoning in Image Sequences
url: http://arxiv.org/abs/2608.10908v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_13-29-03Z_OrderMatters_LVLMsasJudgesforTemporalReasoninginIm.md
generated_at: 2026-08-11 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper argues that Large Vision‑Language Models (LVLMs) used to judge image sequences are structurally biased and collapse when required to discriminate temporal order between pairs of frames, despite performing reasonably well on isolated pointwise scores. It identifies primacy and recency effects as systematic positional asymmetries that dominate a model’s judgment.

## Key Takeaways  
- LVLMs achieve decent pointwise scores but fail catastrophically in pairwise discrimination tasks because their architecture biases favor certain frame positions over semantic content.  
- The collapse stems from architectural issues such as causal masking and rotary embeddings, which create positional asymmetries that amplify primacy or recency effects.  
- This is not a data‑scarcity problem; it is a structural limitation of current transformer‑based judges that treat frames as unordered snapshots.

## Context  
Current multimodal AI systems rely on LVLMs to evaluate visual narratives, assuming that each frame can be judged independently. However, these models are optimized for static or loosely connected images and lack mechanisms to enforce temporal continuity, leaving a gap in coherent story assessment.

## Implications  
Researchers must shift toward temporally‑aware evaluation paradigms that respect the logical order of frames rather than relying on snapshot metrics. Practitioners should adopt such frameworks to ensure AI systems generate and judge visual stories with genuine sequential coherence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10908v1)

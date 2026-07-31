---
title: RoguePrompt: Dual-Layer Encoding for Self-Reconstruction to Circumvent LLM Moderation
url: http://arxiv.org/abs/2607.27373v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_18-25-30Z_RoguePrompt_Dual_LayerEncodingforSelf_Reconstructi.md
generated_at: 2026-07-30 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces RoguePrompt, a two‑layer encoding technique that combines Vigenère and ROT13 encodings with natural‑language reconstruction instructions to bypass LLM moderation filters. Evaluated on 313 real‑world prompts, the pipeline achieves high success rates across three stages: filter bypass (93.93 %), instruction reconstruction (79.02 %), and execution (70.18 %). The results show where multistage jailbreaks typically fail within an observable black‑box interaction.

## Key Takeaways
- RoguePrompt’s layered encoding allows a prompt to be hidden behind Vigenère then ROT13, making automated filters miss the original content.
- Reconstruction accuracy is high because the natural‑language instructions guide users to decode and recover the concealed request.
- Execution success depends on the model’s ability to follow the reconstructed instruction after moderation bypass.

## Context
LLMs are increasingly used in applications where safety controls must be enforced without exposing users to complex security measures. Moderation systems rely heavily on automated filters, yet adversarial prompts can evade them through clever obfuscation. This work highlights a practical gap: while individual attack stages succeed, the overall pipeline’s effectiveness is uneven across different evaluation points.

## Implications
For developers, these findings suggest that modular moderation checks may need to be re‑evaluated at each stage of user input processing rather than treating them as a single binary pass. Practitioners should consider layered defenses and monitor reconstruction accuracy to prevent successful jailbreaks from reaching execution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27373v1)

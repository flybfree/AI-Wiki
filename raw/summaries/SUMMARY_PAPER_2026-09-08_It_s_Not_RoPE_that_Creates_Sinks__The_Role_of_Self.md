---
title: It's Not RoPE that Creates Sinks: The Role of Self-Concentration and Value-Non-Mixing in Attention
url: http://arxiv.org/abs/2609.09085v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_17-32-31Z_It_sNotRoPEthatCreatesSinks_TheRoleofSelf_Concentr.md
generated_at: 2026-09-08 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why attention layers in large language models often create sinks and massive activations at the first position of a sequence. It finds that these effects arise from self-concentration caused by the causal mask and subsequent value‑non-mixing in attention outputs, independent of the token present there.

## Key Takeaways
- Self-concentration of attention, resulting from the causal mask, leads to large activations at the first token.
- Value-non-mixing in attention outputs amplifies these activations, producing sinks and massive activations.
- These phenomena occur regardless of which token occupies the initial position.

## Context
Large language models are known for attention sink and massive activation issues that affect quantization and training stability. Understanding their internal causes helps improve model efficiency and reliability.

## Implications
Researchers can design better quantization schemes by targeting self-concentration mechanisms. Practitioners may reduce computational cost and memory usage, enabling deployment on low-bit hardware without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09085v1)

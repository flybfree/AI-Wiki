---
title: Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability
url: http://arxiv.org/abs/2608.15475v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_01-44-09Z_Bit_FlipAttacksonVision_Language_ActionModels_Acti.md
generated_at: 2026-08-17 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a bit‑flip attack targeting quantized vision‑language‑action (VLA) models, showing that targeted flips of model weights can completely break closed‑loop performance while random flips are ineffective. It demonstrates that the vulnerability depends on which action head is used and how many bits are altered.

## Key Takeaways
- A small number of gradient‑selected bit flips can reduce closed‑loop success to zero across VLA models, whereas hundreds of random flips have negligible effect.
- The attack concentrates in a few action‑generating layers, with direct regression and token policies being vulnerable at 1–5 flips, while flow‑matching policies require around 100–300 flips.
- Using a fixed‑direction manifold‑escape loss reduces the required budget from about 1000 to roughly 100 flips, proving the attack is not limited to all‑positive directions.

## Context
Quantized vision‑language‑action models are increasingly deployed in embodied AI systems where weight integrity directly impacts real‑world performance. This work highlights a previously overlooked security surface that could cause sudden failures under adversarial conditions.

## Implications
For practitioners, protecting model weights becomes essential for reliable operation of closed‑loop agents. The findings suggest that standard quantization safeguards may be insufficient against targeted bit‑flip attacks, urging the development of more robust weight integrity mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15475v1)

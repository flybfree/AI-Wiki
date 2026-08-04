---
title: Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration
url: http://arxiv.org/abs/2608.00831v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_19-15-17Z_AnticipatoryDigitalTwinsforOnlineHead_and_NeckAdap.md
generated_at: 2026-08-03 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a digital‑twin approach to predict head‑and‑neck anatomy for online adaptive proton therapy without new CT scans. Using a pretrained foundation‑model deformable registration network on a population database, it creates predicted planning CTs that align better with treatment‑day anatomy than static scans.

## Key Takeaways
- The method improves normalized cross‑correlation by 22.8% compared with the static planning CT alone.
- Dice scores for organ‑at‑risk structures increase by 20.2%, reducing misdosing risk.
- Computational error in CT numbers drops by 23.4%, especially benefiting patients whose anatomy changes significantly.

## Context
This work extends AI‑driven registration to anticipate treatment‑day deformations, moving beyond offline workflows that require repeated imaging and lengthy planning cycles. It demonstrates how cross‑patient motion transfer can reduce patient burden and accelerate adaptive therapy delivery in radiation oncology.

## Implications
Clinics could implement this prediction as a routine pre‑treatment step, lowering costs and improving safety margins for proton beams. The approach also sets a precedent for applying generative AI to medical imaging without patient‑specific fine‑tuning, opening pathways for personalized, real‑time treatment adaptation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00831v1)

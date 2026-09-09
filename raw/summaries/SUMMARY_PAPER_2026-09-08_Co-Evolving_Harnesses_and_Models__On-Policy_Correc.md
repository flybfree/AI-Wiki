---
title: Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails
url: http://arxiv.org/abs/2609.09134v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_17-53-49Z_Co_EvolvingHarnessesandModels_On_PolicyCorrectionH.md
generated_at: 2026-09-08 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how evolving agent harnesses and fine‑tuning lightweight models interact, showing that while harness evolution helps weaker models perform well, naive imitation of expert trajectories degrades performance. It introduces an on‑policy correction method that fixes only the failing turn using an expert, preserving the model’s planning style.

## Key Takeaways
- Evolving a harness around a weak model and then having a strong expert use it improves task success but training the weak model on the expert’s full trajectories under that harness causes performance to drop by 4–30 points across Qwen3‑Coder and Gemma 4. - The mismatch occurs because the weaker model adopts the expert’s planning strategy without the competence to execute it, breaking the fit between its native style and the evolved scaffold. - An on‑policy expert‑correction pipeline that rewrites only the failing turn restores compatibility and combines harness evolution with adaptation.

## Context
Agentic AI systems rely heavily on system prompts, tool sets, and execution scaffolding known as harnesses to guide models toward task success. As model capabilities diverge across enterprises, co‑evolving lightweight models with domain‑specific harnesses is a cost‑effective strategy that remains understudied.

## Implications
This work provides a practical recipe for integrating harness evolution with fine‑tuning without sacrificing compatibility, enabling smaller companies to deploy high‑performing agents affordably. Practitioners can adopt the on‑policy correction pipeline to maintain model style while leveraging expert guidance efficiently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09134v1)

---
title: Disease Burden over Skin Tone: Decomposing the Dermatology-AI Generalization Gap
url: http://arxiv.org/abs/2609.02111v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_04-55-23Z_DiseaseBurdenoverSkinTone_DecomposingtheDermatolog.md
generated_at: 2026-09-02 20:56
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why dermatology AI models fail to generalize across skin tones and disease types, comparing a cancer‑specific baseline with foundation models trained on diverse data. It finds that disease‑distribution shift is the dominant cause of poor performance, while within‑disease skin‑tone gaps are smaller but still problematic.

## Key Takeaways
- The cancer‑baseline model’s balanced accuracy drops from 0.62 to 0.21 when moved to unfamiliar clinical conditions, indicating a large disease‑distribution shift impact.
- Within‑disease skin‑tone performance varies between 0.10 and 0.18 balanced accuracy, showing a smaller but still significant representation gap.
- Label‑free analysis reveals that cancer‑specialized features poorly cluster unknown conditions (kNN purity lift +0.06), whereas dermatology‑pretrained features retain transferable structure (+0.23).

## Context
Dermatology AI models are increasingly deployed in low‑resource clinics where patient demographics differ from training data, yet few studies quantify the relative contributions of skin tone versus disease distribution to generalization failures.

## Implications
Understanding that disease distribution is a larger issue than skin tone guides future model design toward broader clinical coverage. The finding that ten labeled examples per category can recover most performance suggests efficient adaptation strategies for real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02111v1)

---
title: Model Confidence Under Answer-Preserving Attacks: An Informativeness-Manipulability Frontier
url: http://arxiv.org/abs/2608.06571v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_20-27-52Z_ModelConfidenceUnderAnswer_PreservingAttacks_AnInf.md
generated_at: 2026-08-09 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how confidence readouts behave when adversarial images are crafted to keep the generated answer byte‑identical, a scenario known as answer‑preserving attacks. It shows that a uniform amplitude certificate cannot guarantee adversarial discrimination and that coordinated attacks can flip many previously rejected answers into accepted ones, undermining confidence as an oversight signal.

## Key Takeaways
- A uniform amplitude certificate below a measurable threshold does not prevent adversarial discrimination; the ceiling of 0.617 accuracy is breached in all tested configurations.  
- Coordinated correctness‑label‑aware attacks can cause up to 84.8 % of wrongly rejected answers to be accepted, especially when transferred through hidden‑state gates.  
- No defense family provides a robust alternative under the specific evaluation conditions; confidence remains an integrity‑sensitive rather than intrinsically robust metric.

## Context
Vision‑language systems rely on confidence scores for gating responses, making robustness a critical research focus. This work extends that discussion by examining how answer‑preserving attacks can manipulate those scores without altering the textual output, revealing a gap between theoretical confidence robustness and practical deployment.

## Implications
For practitioners, the findings warn against treating confidence as an automatically reliable safeguard; instead, they suggest designing defenses that address representation‑level vulnerabilities. The results have broader implications for AI oversight, indicating that confidence thresholds must be calibrated to real‑world threat models rather than assumed intrinsic resilience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06571v1)

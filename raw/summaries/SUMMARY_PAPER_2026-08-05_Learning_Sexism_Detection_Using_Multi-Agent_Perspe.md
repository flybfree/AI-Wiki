---
title: Learning Sexism Detection Using Multi-Agent Perspectivist Preference Optimization
url: http://arxiv.org/abs/2608.04056v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_11-35-30Z_LearningSexismDetectionUsingMulti_AgentPerspectivi.md
generated_at: 2026-08-05 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Multi-Agent Perspectivist Preference Optimization (MAP‑PO) to preserve diverse annotator perspectives on sexism detection instead of collapsing them into a majority vote. Experiments on the EXIST 2024 dataset show that fine‑tuning individual agents per clustering group is essential, and that shared team‑level signals keep each agent calibrated while preventing over‑representation.

## Key Takeaways
- Without fine‑tuning the language models behave almost identically, indicating cluster‑specific training is necessary to capture distinct annotation styles.
- Training each agent only on its own cluster’s labels pushes agents far beyond their intended representation, showing the need for a team signal.
- Adding a shared team‑level reward consistently preserves each agent’s calibration to its cluster while improving overall performance.

## Context
Current NLP sexism detection systems often ignore annotator disagreement, treating it as noise and aggregating labels via simple majority voting. This approach can mask genuine differences in perception that are important for nuanced sentiment analysis. The study addresses this gap by modeling individual viewpoints within a multi‑agent framework.

## Implications
MAP‑PO offers a principled way to retain diverse annotator perspectives, which could improve fairness and robustness of bias detection tools. Practitioners may adopt similar agent‑level calibration techniques to avoid overfitting to majority opinions in real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04056v1)

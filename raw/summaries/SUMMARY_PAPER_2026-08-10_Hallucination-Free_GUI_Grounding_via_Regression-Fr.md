---
title: Hallucination-Free GUI Grounding via Regression-Free Layout-Aware Matching
url: http://arxiv.org/abs/2608.09654v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_14-29-07Z_Hallucination_FreeGUIGroundingviaRegression_FreeLa.md
generated_at: 2026-08-10 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a regression‑free framework for GUI grounding that separates instruction parsing from precise localization. By using a frozen multimodal language model to generate layout‑rich descriptions and a dedicated grounding model trained on binary Text/Icon labels, the system eliminates coordinate regression while suppressing hallucinations. Experiments show over 20% accuracy gains on ScreenSpot‑Pro and more than 15% improvements in success rate and element selection on Mind2Web.

## Key Takeaways
- The approach decouples abstract instruction parsing from layout‑aware localization, allowing the grounding model to rely solely on binary labels rather than learning coordinate regression.  
- A frozen MLLM creates a structured visual description rich with layout cues that guides the matching process without requiring fine‑tuning of the location parameters.  
- The method achieves significant performance gains across benchmark datasets by suppressing hallucinations through layout‑prior candidate matching.

## Context
GUI grounding remains a bottleneck for multimodal agents because end‑to‑end models must learn both perception and regression, leading to unreliable coordinates. This paper addresses that limitation by introducing a modular design that leverages existing visual understanding while focusing training on coarse labeling tasks.

## Implications
The results suggest that separating high‑level reasoning from low‑level localization can improve robustness in interactive AI systems. Practitioners may adopt this architecture to build more reliable screen‑interaction tools without the cost of extensive coordinate fine‑tuning, fostering broader adoption of visual AI in user interfaces.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09654v1)

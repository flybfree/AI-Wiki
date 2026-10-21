---
title: Attractive Faces Skew Text-to-Image Reward Models and Leaderboards
published: 2026-10-20T13:35:34Z
authors: Harvey Mannering, Zhiwu Huang, Adam Prügel-Bennett
url: http://arxiv.org/abs/2610.28195v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Attractive Faces Skew Text-to-Image Reward Models and Leaderboards

## Abstract
Human preference is now central to the evaluation, guidance, finetuning, and ranking of text-to-image models. However, the susceptibility of human preferences to bias in image generation remains underexplored. We identify a key observation: for human faces, perceived attractiveness overrides image quality in preference judgments, even when comparing real photographs of identical fidelity. In a controlled user study, annotators rank more attractive faces as higher quality, even when unattractive real faces are compared with attractive AI-generated ones. We examine the downstream consequences of this bias. Firstly, simulating Elo rankings from user study data shows attractiveness can invert a leaderboard's ranking, elevating synthetic attractive faces over real, unattractive ones. Secondly, the same bias reappears in the human preference models. Editing 40 annotated facial attributes in isolation, we find that attractiveness is the strongest correlate of score for four of five human preference models (PickScore, MPS, HPSv2.1, HPSv3), and the strongest predictor of score in regression analysis. We further show that preference aligned generation shifts faces toward younger, more feminine faces, and can override explicit prompts for unattractive faces, thereby limiting user control. Finally, we explore mitigation strategies, both for data collection and post training on human preference models. These findings highlight the need for preference models that disentangle image quality from human cognitive bias, enabling more reliable evaluation.

## Metadata
- **Published**: 2026-10-20T13:35:34Z
- **Authors**: Harvey Mannering, Zhiwu Huang, Adam Prügel-Bennett
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28195v1)
---
title: RA$^2$: Retain-Anchored Attraction Preserves Forget-Adjacent Utility in LLM Unlearning
published: 2026-10-14T01:31:40Z
authors: Zinan Ling, Yang Xiao, Ruimeng Ye, Sijia Liu, Bo Hui
url: http://arxiv.org/abs/2610.19385v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RA$^2$: Retain-Anchored Attraction Preserves Forget-Adjacent Utility in LLM Unlearning

## Abstract
Large Language Model (LLM) unlearning is often evaluated primarily by target suppression and clean retain utility. These metrics can miss a local failure mode: a model may perform well on standard retain prompts, yet degrade on benign reasoning when prompts lie near the forgotten domain. This phenomenon is termed forget-adjacent utility loss. A fundamental question is: where should forget representations go after they leave the removed behavior? Successful unlearning depends not only on whether forget-conditioned representations depart from the harmful computation, but also on the direction in which they are redirected afterward. We propose RA$^2$ (Retain-Anchored Attraction), a latent-space unlearning method that redirects forget-token states toward nearby retain-supported representations while preserving higher-layer behavior on retain data. On WMDP and MUSE, RA$^2$ yields higher forget-adjacent utility than strong unlearning baselines at similar broad-utility levels. These results show that the migration direction of forget representations materially affects benign behavior near the forget boundary. Our code is available at https://github.com/ZacLing/retain_anchored_attraction.

## Metadata
- **Published**: 2026-10-14T01:31:40Z
- **Authors**: Zinan Ling, Yang Xiao, Ruimeng Ye, Sijia Liu, Bo Hui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19385v1)
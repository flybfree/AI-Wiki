---
title: ECHO: Replacing the Compliance Proxy with Response Harmfulness in Optimization-Based Jailbreak Attack
published: 2026-10-16T07:07:08Z
authors: Yuanwei Wu, Lingdong Huang, Yunlong Mao, Kanye Ye Wang, Jingyu Hua, Sheng Zhong
url: http://arxiv.org/abs/2610.23030v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ECHO: Replacing the Compliance Proxy with Response Harmfulness in Optimization-Based Jailbreak Attack

## Abstract
Despite extensive safety alignment, large language models remain vulnerable to jailbreak attacks. Existing optimization-based attacks share a single objective: maximize a token-level proxy of victim compliance---such as the likelihood of an affirmative prefix---computed on the prompt rather than the decoded reply. This proxy cannot distinguish a cautious hedge from a fully actionable harmful answer, leaving the search blind to what the model actually says. We propose ECHO (Evaluation-Conditioned Harmfulness Optimization), which replaces the compliance proxy with response-level, continuous harmfulness scores from HarmSig, a 1.7B regressor grounded in actual harmful capability. ECHO couples HarmSig with five word-level perturbation operators and Keyword-Anchored Beam Search with global top-m memory, under a strict black-box threat model. Across five open-weight victims on AdvBench, ECHO achieves up to 0.898 StrongREJECT mean score and 89.23% HarmBench success. Our code is publicly available at https://github.com/STANWYW/echo.

## Metadata
- **Published**: 2026-10-16T07:07:08Z
- **Authors**: Yuanwei Wu, Lingdong Huang, Yunlong Mao, Kanye Ye Wang, Jingyu Hua, Sheng Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23030v1)
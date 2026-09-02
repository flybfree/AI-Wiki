---
title: Beyond Token Positions: Safety Alignment Across Denoising Steps in Diffusion Language Models
published: 2026-08-31T23:50:31Z
authors: Guoli Wang, Haonan Shi, Tu Ouyang, An Wang
url: http://arxiv.org/abs/2609.00495v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Token Positions: Safety Alignment Across Denoising Steps in Diffusion Language Models

## Abstract
Diffusion large language models (dLLMs) generate text through iterative denoising rather than left-to-right decoding. This generation paradigm introduces two axes that can influence safety alignment: when tokens are generated during denoising and where they appear in the response. In this paper, we measure dLLM safety behavior under harmful prompts by tracing intermediate token distributions and commitment decisions throughout denoising. Our analysis shows that refusal signals are concentrated in early denoising steps and leading response positions, and the tokens committed early can strongly shape the final safety outcome. Our measurements further show that the denoising step and persistence of refusal-token commitment are important for understanding dLLM safety. Based on these findings, we propose Refusal-Aware Early Commitment (RAEC), a simple training-free decoding method that commits persistent refusal signals from early steps. Experiments on LLaDA and Dream show that RAEC reduces attack success rates while largely preserving utility. The code is available at https://github.com/Glresearch1/RAEC.

## Metadata
- **Published**: 2026-08-31T23:50:31Z
- **Authors**: Guoli Wang, Haonan Shi, Tu Ouyang, An Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00495v1)
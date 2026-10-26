---
title: REACT: Representational Early Analysis and Control of Chain-of-Thought Trajectories
published: 2026-10-23T03:28:34Z
authors: Hanwen Zhang, Enyi Jiang, Ruike Zhu, Qinan Yu, Sanmi Koyejo
url: http://arxiv.org/abs/2610.32113v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REACT: Representational Early Analysis and Control of Chain-of-Thought Trajectories

## Abstract
Chain-of-thought (CoT) generation offers an opportunity to intervene before a reasoning model completes its answer. But does the point at which risk is easiest to detect also offer the most effective control? We study this question with REACT, a conditional activation intervention that learns a safety direction from paired safe and unsafe trajectories and applies it once to an early CoT hidden state. The model weights remain frozen, and all subsequent tokens are generated without further edits. To study timing, we train directions separately at each of the first five CoT positions and evaluate ungated edits with full post-edit regeneration. Across three distilled reasoning models and three generation seeds, the strongest gains concentrate in a two- to three-token early window; on DeepSeek-R1-Distill-Llama-8B, the effect falls to approximately zero at the fourth and fifth tokens, even though later states can be more predictive of risk. This separates risk readability from effective control: intervention timing must be evaluated through its effect on subsequent generation. On the same 8B model, REACT raises the rate of fully safe CoT-answer outputs on StrongREJECT-273 from 29.06% to 82.05%, while keeping benign refusal and usefulness near baseline. An anonymized implementation is available at https://anonymous.4open.science/r/REACT_official2-333B.

## Metadata
- **Published**: 2026-10-23T03:28:34Z
- **Authors**: Hanwen Zhang, Enyi Jiang, Ruike Zhu, Qinan Yu, Sanmi Koyejo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32113v1)
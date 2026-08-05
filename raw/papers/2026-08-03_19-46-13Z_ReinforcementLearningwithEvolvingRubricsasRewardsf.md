---
title: Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning
published: 2026-08-03T19:46:13Z
authors: Fangxu Yu, Tao Feng, Dehai Min, Zinan Lin, Weijia Xu, Michael Xu, Philip S. Yu, Ge Liu, Tianyi Zhou
url: http://arxiv.org/abs/2608.02831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning

## Abstract
Audio reasoning is essential for machine understanding of the acoustic world. Reinforcement learning with verifiable rewards can elicit such reasoning, yet existing reward designs are complementary in their limitations: outcome-based rewards supervise only the final answer and let the model reach it without attending to the audio, whereas process-based rewards score the reasoning itself but rely on coarse, hand-crafted, and fixed criteria that neither adapt to each question nor stay grounded in the acoustic evidence. Moreover, questions differ in what they demand, with some hinging on perception and others on multi-step reasoning, and any static criterion weakens as the policy improves. Supervising the reasoning process with fine-grained, audio-grounded, and adaptive rewards is therefore crucial, yet challenging since such rewards are impractical to design by hand for every sample. To this end, we introduce AudioRubrics, a reinforcement learning framework that supervises audio reasoning with self-evolving, audio-grounded rubric rewards. AudioRubrics synthesizes per-sample rubrics from the raw waveform and, conditioned on the model's own rollouts, regenerates and reweights criteria per group, supplying a continuous learning signal that keeps targeting the current policy's weaknesses as static criteria saturate. Comprehensive evaluations across three audio reasoning benchmarks reveal that AudioRubrics substantially outperforms a wide range of open-source and training-based baselines. Furthermore, our analysis shows that the gains scale with the capability of the rubric generator and judge, and AudioRubrics converges to a stable reasoning length that avoids both degenerate collapse and unbounded growth. The improvement in audio perception further demonstrates the effectiveness of anchoring supervision in the acoustic evidence. Our project page is available at https://audiorubrics.github.io.

## Metadata
- **Published**: 2026-08-03T19:46:13Z
- **Authors**: Fangxu Yu, Tao Feng, Dehai Min, Zinan Lin, Weijia Xu, Michael Xu, Philip S. Yu, Ge Liu, Tianyi Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02831v1)
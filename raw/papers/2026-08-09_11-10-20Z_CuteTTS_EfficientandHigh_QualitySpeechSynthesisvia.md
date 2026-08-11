---
title: CuteTTS: Efficient and High-Quality Speech Synthesis via Autoregressive Modeling of Continuous Latents
published: 2026-08-09T11:10:20Z
authors: Yuqian Zhang, Yao Shi, Kexin Huang, Botian Jiang, Zhe Xu, Yiwei Zhao, Min Liang, Shuang Chen, Xipeng Qiu
url: http://arxiv.org/abs/2608.08638v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CuteTTS: Efficient and High-Quality Speech Synthesis via Autoregressive Modeling of Continuous Latents

## Abstract
Zero-shot text-to-speech (TTS) now supports interactive assistants, personalized media, and accessibility tools. All TTS systems require faithful linguistic rendering, consistent speaker identity, and low-latency response. Yet compact streaming systems must preserve sufficient acoustic detail in a predictable low-rate latent sequence, while iterative diffusion sampling and classifier-free guidance multiply inference cost at every autoregressive step. To strike a balance between high-fidelity synthesis and low-latency inference, we present CuteTTS, a compact continuous-autoregressive TTS system. It combines semantically aligned causal VAE latents with patch-level autoregression, explicit speaker conditioning, and a bidirectional flow-matching head. We further introduce guidance-step distillation, which absorbs classifier-free guidance and multiple solver steps into a single interval-conditioned student. Evaluations on LibriSpeech and Seed-TTS-Eval demonstrate competitive intelligibility and speaker similarity in zero-shot voice cloning, while distillation lowers first-audio latency by 23.3% and real-time factor by 40.8% relative to the base model with comparable objective and subjective quality. These results provide a practical path toward continuous-autoregressive TTS that reconciles high-fidelity generation with the latency demands of real-time interaction.

## Metadata
- **Published**: 2026-08-09T11:10:20Z
- **Authors**: Yuqian Zhang, Yao Shi, Kexin Huang, Botian Jiang, Zhe Xu, Yiwei Zhao, Min Liang, Shuang Chen, Xipeng Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08638v1)
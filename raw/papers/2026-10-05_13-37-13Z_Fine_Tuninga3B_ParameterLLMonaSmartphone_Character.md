---
title: Fine-Tuning a 3B-Parameter LLM on a Smartphone: Characterizing Sustained Training
published: 2026-10-05T13:37:13Z
authors: Andrew Geyko, Marius Mosbach, André Brinkmann
url: http://arxiv.org/abs/2610.06325v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fine-Tuning a 3B-Parameter LLM on a Smartphone: Characterizing Sustained Training

## Abstract
Multi-billion-parameter LLMs now run on phones for inference, and training them on the device would personalize them without user data leaving the phone. Prior work has measured individual training steps of such models on phones, but not complete training runs, and not whether adapters trained on the device improve personalization. We present the first systematic characterization of a multi-billion-parameter LLM fine-tuned on a mobile device, covering memory, per-step time, thermal behavior, and energy. An iPhone 17 Pro can fine-tune a 3B-parameter LLM to a typical user within one battery charge, and the resulting adapters improve personalization as much as adapters trained on a server. Sustained training throttles the phone to about half its initial throughput, and none of the pausing or burst schedules we tested recovers it. Nearly all of each training step is spent in the frozen base model, most of it in the backward pass, which nine of the ten other runtimes we audited do not accelerate. Apple's MLX had a kernel for it that was never dispatched and was incorrect, and our repair, now merged upstream, trains an adapter 1.47x faster on a third less energy. On-device fine-tuning is feasible on current phones, and making it efficient requires runtimes and operating systems to treat training as a first-class workload.

## Metadata
- **Published**: 2026-10-05T13:37:13Z
- **Authors**: Andrew Geyko, Marius Mosbach, André Brinkmann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06325v1)
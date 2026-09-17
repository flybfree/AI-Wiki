---
title: MiST: Mid-Training LLMs for Cybersecurity
published: 2026-09-16T11:33:12Z
authors: Oded Ovadia, Elad Ben Zaken, Elad Guttman, Orly Moreno Kadosh
url: http://arxiv.org/abs/2609.18496v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MiST: Mid-Training LLMs for Cybersecurity

## Abstract
Cybersecurity combines high-stakes analysis with complex technical language, making it an impactful and challenging domain for LLMs. We present MiST (Mid-trained Security Transformer), a suite of 8B and 32B models that achieve strong performance on public cybersecurity benchmarks. We use mid-training as an intermediate adaptation stage between general pre-training and cybersecurity training. Rather than performing continual pre-training over large volumes of raw domain text, we curate a compact, expert-vetted seed corpus, and transform it into high-quality domain-specific synthetic training data. The final MiST checkpoints improve mean cybersecurity accuracy by +13.1 and +8.6 absolute percentage points over the corresponding Qwen baselines for 8B and 32B, respectively, corresponding to relative gains of +27.0% and +15.8%. Ablation results further show that these cybersecurity gains arise in the mid-training and supervised fine-tuning stages through a combination of the synthetic data generation flows. Furthermore, we show that MiST provides a stronger initialization for downstream task-specific fine-tuning adaptation and reinforcement learning.

## Metadata
- **Published**: 2026-09-16T11:33:12Z
- **Authors**: Oded Ovadia, Elad Ben Zaken, Elad Guttman, Orly Moreno Kadosh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18496v1)
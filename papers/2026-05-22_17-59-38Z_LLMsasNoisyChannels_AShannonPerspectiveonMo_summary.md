---
title: "Summary: 2026-05-22_17-59-38Z_LLMsasNoisyChannels_AShannonPerspectiveonModelCapa.md"
date: 2026-05-22
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-22_17-59-38Z_LLMsasNoisyChannels_AShannonPerspectiveonModelCapa.md


**Source**: [Original Paper](http://arxiv.org/abs/2605.23901v1)
Saved: 2026-05-25 00:01
Source: 2026-05-22_17-59-38Z_LLMsasNoisyChannels_AShannonPerspectiveonModelCapa.md
Model: None

---


## Summary  
The paper argues that existing scaling laws for Large Language Models (LLMs) are overly simplistic because they predict only monotonic improvements with more compute or data, ignoring phenomena such as catastrophic overtraining and quantization‑induced degradation. By treating LLM training as an information‑transmission problem over a noisy channel, the authors introduce the Shannon Scaling Law—a unified theoretical framework that links model parameters to bandwidth and tokens to signal power. This perspective predicts a fundamental capacity limit: when the signal‑to‑noise ratio (SNR) is insufficient, performance flattens or drops, producing an “U‑shaped” curve rather than a smooth rise. The authors validate this theory with extensive experiments on Pythia and OLMo2 models under various perturbations.

## Key Contributions  
- [Finding 1] Existing monotonic scaling laws cannot explain non‑monotonic performance dips such as catastrophic overtraining or quantization loss, highlighting a gap in current theoretical understanding.  
- [Finding 2] The Shannon Scaling Law provides a principled model that maps LLM parameters to channel bandwidth and tokens to signal power, explicitly capturing the interaction between learning signal and intrinsic noise.  
- [Finding 3] Experimental validation shows the Shannon framework outperforms classical and recent perturbation‑aware laws, achieving high $R^2$ scores and accurately predicting unseen model capacities.

## Methodology  
The authors adopt a channel‑theoretic analogy: each LLM parameter set is analogous to channel bandwidth, while training tokens represent signal power. They compute an SNR metric for given configurations of model size and data volume, then fit the Shannon capacity curve to observed loss trajectories. Experiments involve perturbing Pythia (≤6.9 B) and OLMo2 models with ≤180 B tokens using Gaussian noise, quantization, and supervised fine‑tuning on math, QA, and code tasks. The fitted model is extrapolated to a 307 B token regime, while baseline monotonic laws collapse.

## Results  
The Shannon Scaling Law yields $R^2 = 0.847$ when predicting the unseen 12 B Pythia model up to 307 B tokens, far exceeding the $R^2$ of conventional scaling curves (≈0.6). It captures loss basins missed by prior approaches and demonstrates a clear transition from monotonic improvement to U‑shaped degradation as SNR falls below threshold. Classical baselines show near‑zero fit, confirming their inadequacy.

## Significance  
This work bridges information theory with LLM scaling, offering a testable model for capacity limits that explains why larger models do not always improve performance. It enables more realistic resource planning and highlights the importance of maintaining adequate SNR during training.

## Related Concepts  
- Shannon‑Hartley theorem (capacity = B log₂(1+SNR))  
- Signal‑to‑noise ratio (SNR) in communication systems  
- Information capacity as a bound on learnable parameters  
- Catastrophic overtraining and quantization degradation  
- Classical power‑law scaling laws for LLMs

[[LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws]]
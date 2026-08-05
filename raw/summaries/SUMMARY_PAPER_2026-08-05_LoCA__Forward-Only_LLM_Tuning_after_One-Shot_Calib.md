---
title: LoCA: Forward-Only LLM Tuning after One-Shot Calibration with Local Credit Assignment
url: http://arxiv.org/abs/2608.03020v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_02-06-43Z_LoCA_Forward_OnlyLLMTuningafterOne_ShotCalibration.md
generated_at: 2026-08-05 01:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LoCA, a two‑stage method that replaces repeated end‑to‑end backpropagation with a single calibration pass using local credit assignment. On Qwen2.5 models ranging from 0.5B to 14B, LoCA achieves lower cross‑entropy than the corresponding LoRA runs while reducing GPU peak memory by 26–29% and CPU steady‑state memory by 36–52%. The method amortizes global credit assignment into one calibration step.

## Key Takeaways
- Local Credit Assignment fits a low‑rank map from the final prediction error to a correction of each transformer block’s hidden state with only one backward pass, eliminating the need for repeated activation storage.
- This map is then reused to construct blockwise regression targets that are solved via closed‑form ridge equations, allowing forward‑only tuning without additional backpropagation.
- The approach cuts GPU peak memory usage by 26–29% and CPU steady‑state memory by 36–52% compared with LoRA, while also reducing per‑pass time by roughly half.

## Context
Parameter‑efficient fine‑tuning techniques such as LoRA still rely on end‑to‑end backpropagation through frozen backbones, which is computationally expensive and limits the size of models that can be adapted. This work demonstrates that a one‑time calibration can replace those repeated backward passes, offering a scalable alternative for large language model adaptation.

## Implications
For practitioners, LoCA enables faster iteration cycles and lower hardware demands, making fine‑tuning feasible on modest GPUs or even CPUs. It also suggests a broader shift toward forward‑only tuning strategies that could reduce compute costs in large language model deployment and research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03020v1)

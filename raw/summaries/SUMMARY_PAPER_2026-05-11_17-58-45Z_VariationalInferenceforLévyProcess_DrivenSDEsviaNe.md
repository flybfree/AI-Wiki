---

title: "Summary: Variational Inference for Lévy Process-Driven SDEs via Neural Tilting"
url: http://arxiv.org/abs/2605.10934v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-11_17-58-45Z_VariationalInferenceforLévyProcess_DrivenSDEsviaNe.md
generated_at: "2026-06-11 10:38"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper proposes a neural exponential tilting framework for variational inference on stochastic differential equations driven by Lévy processes. The method learns to reweight the heavy‑tailed Lévy measure with neural networks, preserving jump structure while enabling tractable optimization and closed‑form normalization. Empirical results show that the approach outperforms Gaussian‑based variational methods in capturing discontinuities and provides reliable posterior estimates on both synthetic and real data.

## Key Takeaways
- The neural tilting technique uses a quadratic neural network to reparameterize the Lévy measure, allowing the variational family to exactly represent jump dynamics without assuming Gaussianity.  
- By exploiting symmetry‑aware Monte Carlo optimizers, the method achieves closed‑form normalization of the tilted distribution, making inference computationally efficient even for heavy‑tailed processes.  
- The framework yields posterior predictions that accurately reflect discontinuities and tail behavior, demonstrating superior performance over standard variational baselines on both synthetic Lévy SDEs and real financial climate datasets.

## Context
Heavy‑tailed phenomena such as extreme weather events or market crashes cannot be captured by Gaussian approximations, yet current AI inference tools often rely on them. This work bridges that gap by integrating advanced neural architectures with rigorous probability theory, offering a principled alternative for Bayesian modeling in domains where discontinuities matter. The approach aligns with the trend toward differentiable probabilistic models that support scalable optimization.

## Implications
For practitioners in finance and climate science, this method provides a reliable way to infer posterior distributions of jump‑driven processes without sacrificing accuracy or scalability. It enables automated risk assessment and scenario analysis where traditional Monte Carlo methods are impractical due to heavy tails, thereby enhancing decision‑making under uncertainty.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.10934v1)

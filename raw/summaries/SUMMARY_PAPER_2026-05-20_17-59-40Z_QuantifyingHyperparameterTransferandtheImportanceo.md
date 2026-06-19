---

title: Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate
url: http://arxiv.org/abs/2605.21486v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-20_17-59-40Z_QuantifyingHyperparameterTransferandtheImportanceo.md
generated_at: "2026-06-11 10:44"
model: nvidia/nemotron-3-nano-4b

---


## Summary  
The paper introduces a framework to quantify hyperparameter transfer between small and large language model scales, evaluating it through scaling law fit quality, extrapolation error robustness, and asymptotic loss penalty. It demonstrates that the Maximal Update ($μ$P) parameterization yields superior learning rate transfer compared with standard parameterization (SP), primarily because it maximizes the embedding layer learning rate.

## Key Takeaways  
- The embedding layer learning rate in SP acts as a bottleneck causing training instabilities, whereas $μ$P’s higher embedding rate smooths training and improves hyperparameter transfer.  
- Weight decay enhances scaling law fits but can degrade robustness of extrapolation when token‑per‑parameter is fixed.  
- $μ$P’s advantage stems from its near scale‑invariant parameterization, making it more effective than SP for large models.

## Context  
Hyperparameter optimization remains a bottleneck in training increasingly massive language models where resources are limited and scaling laws provide guidance. This work bridges theory and practice by offering empirical metrics to assess how hyperparameters transfer across model sizes. The findings highlight the role of specific layer learning rates within this broader optimization challenge.

## Implications  
Practitioners can adopt $μ$P to stabilize training of large LLMs without extensive hyperparameter searches, reducing compute costs. The insights also suggest that weight decay strategies should be tuned per‑layer configuration to balance scaling law performance and extrapolation robustness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.21486v1)

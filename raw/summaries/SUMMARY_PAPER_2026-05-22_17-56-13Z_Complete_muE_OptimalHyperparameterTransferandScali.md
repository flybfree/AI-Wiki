---

title: "Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models"
url: http://arxiv.org/abs/2605.23893v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-22_17-56-13Z_Complete_muE_OptimalHyperparameterTransferandScali.md
generated_at: "2026-06-11 10:46"
model: nvidia/nemotron-3-nano-4b

---


## Summary
Complete-muE introduces a two-bridge system that transfers hyperparameters between dense and Mixture-of-Experts transformer blocks, handling changes in architecture, expert count, and token granularity. The framework demonstrates that tuning hyperparameters on a single dense reference model yields near‑optimal results across diverse MoE configurations, enabling faster convergence without extensive search.

## Key Takeaways
- Bridge~I uses μP with normalized router scale to map dense FFN to Dense MoE, allowing active‑width adjustments while preserving routing stability.  
- Bridge~II employs activated‑expert scaling and a bounded residual shift σ₀ to transition between Dense MoE and sparse MoE without first‑order SDE corrections.  
- The Complete muE rule provides stable hyperparameter optima across capacity, granularity, shared/group‑balanced hybrids, width/depth, batch size, and duration changes.

## Context
The need for hyperparameter transfer in MoE models arises because scaling model capacity often involves redesigning both the expert pool and token distribution. Existing methods are limited by fixed architectures or per‑step token counts, making them unsuitable for real‑world deployment where multiple configurations coexist.

## Implications
Complete-muE simplifies large‑scale training pipelines by allowing a single hyperparameter baseline to be reused across model variants, reducing computational cost and accelerating research iteration. Practitioners can adopt this approach to deploy MoE models faster while maintaining competitive performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.23893v1)

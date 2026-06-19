---

title: 'Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models'
published: "2026-05-22T17:56:13Z"
authors: Hongwu Peng, Ohiremen Dibua, Yuanjun Xiong, Yifan Gong, Jianming Zhang, Yan Kang
url: http://arxiv.org/abs/2605.23893v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models



**Source**: [Original Paper](http://arxiv.org/abs/2605.23893v1)
## Abstract
We propose Complete-muE, a framework which targets hyperparameter transfer across dense FFN and any Mixture-of-Experts (MoE) setups in transformer blocks. Existing tools such as $μ$P (requires fixed architectue) or SDE (requires fixed per-step token count) cannot directly solve the hyperparameter transfer problem in MoE setups because Dense to MoE transfer or MoE total experts scaling changes both architecture and tokens per expert. Complete-muE solves this challenge with a two-bridge system: Bridge~I maps between dense FFN and Dense MoE by active-width $μ$P with a normalized router scale. Bridge~II maps between Dense MoE and sparse MoE by activated-expert scaling, where the first-order SDE LR/WD correction cancels while a bounded residual $σ_0$ shift remains. The resulting transfer rule, which we term as Complete muE, covers changes in activated experts, total capacity, granularity, and shared/group-balanced hybrids for MoE models as well as network width/depth, batch size, and duration changes for general Transformer models. Extensive language model and diffusion model pretraining experiments confirm that complete-muE yields relatively stable hyperparameter optima across model architectures and parameter counts -- with only minor drift consistent with the non-strict SDE behavior of Bridge~II. In practice this drift is small enough that hyperparameters tuned on a single dense reference transfer near-optimally to all MoE configurations -- \emph{tune dense once, transfer to all} is the practical recipe at the core of Complete-muE. This enables MoE models to achieve accelerated convergence speedup over dense models when scaling model capacity without costly hyperparameter search.

## Metadata
- **Published**: 2026-05-22T17:56:13Z
- **Authors**: Hongwu Peng, Ohiremen Dibua, Yuanjun Xiong, Yifan Gong, Jianming Zhang, Yan Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23893v1)
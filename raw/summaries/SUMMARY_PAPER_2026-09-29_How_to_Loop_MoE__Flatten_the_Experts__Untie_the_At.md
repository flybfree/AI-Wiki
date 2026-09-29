---
title: How to Loop MoE: Flatten the Experts, Untie the Attention
url: http://arxiv.org/abs/2609.35751v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_17-58-03Z_HowtoLoopMoE_FlattentheExperts_UntietheAttention.md
generated_at: 2026-09-29 02:08
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Foil, a novel architecture for looping Mixture-of-Experts (MoE) models that enhances parameter efficiency and performance by reusing model blocks multiple times. Foil achieves superior results through two key mechanisms: flattening the expert structure to expand the routing pool while maintaining fixed compute and parameters, and untying attention weights across passes to allow distinct representations per loop iteration. Experimental validation demonstrates that Foil consistently lowers pretraining loss compared to baselines, with performance improving monotonically as flattening increases, ultimately delivering better downstream accuracy without additional computational cost.

## Key Takeaways
- Foil restructures MoE models by halving the number of expert layers while simultaneously doubling the experts per layer and the number of passes; this "flattening" strategy keeps total expert parameters and compute constant but significantly increases the size of the routing pool available for each token, leading to more diverse expert selection.
- Untying attention parameters across loop iterations proves critical for performance gains; by assigning unique attention weights to each pass while keeping experts and routers shared, Foil achieves more balanced and confident routing decisions, which correlates with healthier expert utilization and reduced pretraining loss at scale.
- Ablation studies reveal that the benefits of looping and widening expert layers are synergistic, establishing design guidance for sparse looped MoEs: practitioners should prioritize models with higher experts per layer and more passes, as routing confidence serves as a more reliable health metric than load balance, and increasing pass counts amplifies the returns on model width.

## Context
As Transformer models scale, researchers seek methods to extract maximum capability from fixed parameter budgets without linearly increasing compute costs. Looped Transformers address this by reusing layer blocks, while sparse MoE architectures improve efficiency by activating only a subset of parameters per token; however, effectively combining these paradigms has remained an open challenge due to routing inefficiencies and suboptimal expert utilization in naive looped implementations. This work bridges that gap by proposing Foil, which systematically addresses how to loop sparse experts to maximize their potential, contributing to the broader effort of optimizing model scaling laws through architectural innovation rather than brute-force parameter growth.

## Implications
The findings provide actionable design principles for developing more efficient large language models, suggesting that practitioners can improve performance by adjusting expert width and pass counts rather than solely increasing depth or total parameters. By highlighting routing confidence as a superior diagnostic metric over load balance, the research offers new tools for debugging and stabilizing MoE training dynamics in production environments. Furthermore, the demonstrated monotonic improvements with flattening encourage industry adoption of looped architectures to achieve higher accuracy within strict latency and compute constraints, potentially reducing inference costs while maintaining or improving model quality

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35751v1)

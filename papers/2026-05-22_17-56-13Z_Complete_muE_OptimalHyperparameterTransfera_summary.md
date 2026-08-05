---
title: "Summary: 2026-05-22_17-56-13Z_Complete_muE_OptimalHyperparameterTransferandScali.md"
date: 2026-05-22
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-22_17-56-13Z_Complete_muE_OptimalHyperparameterTransferandScali.md


**Source**: [Original Paper](http://arxiv.org/abs/2605.23893v1)
Saved: 2026-05-25 00:00
Source: 2026-05-22_17-56-13Z_Complete_muE_OptimalHyperparameterTransferandScali.md
Model: None

---


## Summary  
The paper introduces **Complete‑muE**, a framework that enables optimal hyperparameter transfer across dense FFN and any Mixture‑of‑Experts (MoE) transformer blocks, overcoming the limitations of existing tools such as μP (which requires fixed architecture) and SDE (which assumes a fixed token count per expert). Complete‑muE uses two bridges—Bridge I for dense‑to‑Dense MoE mapping with a normalized router scale, and Bridge II for Dense‑to‑Sparse MoE mapping that cancels the first‑order SDE correction while preserving a bounded residual shift. The resulting transfer rule, termed **Complete muE**, accommodates changes in activated experts, total capacity, granularity, shared/group‑balanced hybrids, as well as network width/depth, batch size, and duration. This allows tuning once on a dense reference model and applying it to all MoE configurations.

## Semantic links
- [[concepts/papers/2026-06-18_15-36-13Z_CRAX_FastSafeReinforcementLearningBenchmark_summary.md|Summary: 2026-06-18_15-36-13Z_CRAX_FastSafeReinforcementLearningBenchmarking.md]] — 3 title terms overlap; shared tags: ai, paper, research; 12 summary/topic terms overlap
- [[concepts/papers/2026-06-10_14-34-13Z_PCA_EnhancedAdaptiveNVARFrameworkforHigh_Re_summary.md|Summary: 2026-06-10_14-34-13Z_PCA_EnhancedAdaptiveNVARFrameworkforHigh_Resolutio.md]] — 3 title terms overlap; shared tags: ai, paper, research; 11 summary/topic terms overlap
- [[concepts/papers/2026-06-18_17-55-00Z_TowardCalibratedMixture_of_ExpertsUnderDist_summary.md|Summary: 2026-06-18_17-55-00Z_TowardCalibratedMixture_of_ExpertsUnderDistributio.md]] — 2 title terms overlap; shared tags: ai, paper, research; 12 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A unified two‑bridge system (Bridge I and Bridge II) that simultaneously handles dense‑to‑MoE and Dense‑to‑sparse MoE transitions.  
- [Finding 2] The Complete‑muE transfer rule provides stable hyperparameter optima across diverse MoE architectures, including varying numbers of experts, shared/expert groups, and total capacity changes.  
- [Finding 3] Empirical evidence that the drift introduced by Bridge II is minimal, enabling a practical “tune dense once, transfer to all” recipe.

## Methodology  
The authors propose **Bridge I**, which employs μP with a normalized router scale to map dense FFN weights onto MoE expert weights while preserving activation patterns. **Bridge II** adapts the SDE’s first‑order correction by canceling LR/WD terms and introducing a bounded residual shift σ₀ that accounts for sparse expert scaling. The combined rule Complete‑muE is derived analytically, implemented in code, and supports changes in model granularity (expert count), capacity, batch size, depth, and duration.

## Results  
Experiments on large language models and diffusion pretraining show that hyperparameters tuned on a dense reference model remain within 1–2 % of optimal values for MoE variants across different expert counts and group configurations. The convergence speedup over dense baselines is consistent, with only minor drift due to Bridge II’s non‑strict SDE behavior.

## Significance  
Complete‑muE decouples hyperparameter tuning from architectural scaling, enabling rapid deployment of larger MoE models without exhaustive search. This reduces compute cost and accelerates research iteration, especially in resource‑constrained settings where full re‑tuning is prohibitive.

## Related Concepts

- [[concepts/generative-models/generative-models-hub.md|Generative Models Hub]]
- [[concepts/multimodal-ai/multimodal-ai-hub.md|Multimodal AI Hub]]
- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/training-optimization/training-optimization-hub.md|Training Optimization Hub]]

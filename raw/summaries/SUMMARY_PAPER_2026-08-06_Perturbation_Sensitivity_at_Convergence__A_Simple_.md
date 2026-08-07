---
title: Perturbation Sensitivity at Convergence: A Simple Signal for Identifying Spuriously Correlated Samples
url: http://arxiv.org/abs/2608.05419v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_21-29-11Z_PerturbationSensitivityatConvergence_ASimpleSignal.md
generated_at: 2026-08-06 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes a method to detect spuriously correlated samples in models trained by empirical risk minimization using the convergence of training loss as an indicator; it shows that after convergence the model cannot distinguish between two population groups and that fixed perturbations affect predictions differently for each type.  

## Key Takeaways  
- A usable signal emerges at convergence where the model's loss no longer distinguishes between two population groups, allowing identification of samples affected by spurious correlation without group labels or early stopping.  
- Fixed input perturbations flip predictions of fragile samples far more often than those consistent with spurious correlation, enabling detection through simple forward passes.  
- Rebalancing training using these detected samples improves worst‑group accuracy from 57.3% to 80.8%, compared to 85.8% when ground‑truth labels are used.  

## Context  
This work addresses a longstanding issue in machine learning where models exploit spurious correlations, leading to poor performance on unseen subpopulations; identifying such samples without costly annotations is crucial for building robust and generalizable systems.  

## Implications  
Practitioners can apply this signal to enhance model reliability across diverse data distributions, reducing reliance on expensive group‑labeled validation sets and enabling more equitable AI outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05419v1)

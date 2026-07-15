---
title: "Summary: 2026-05-06_17-53-20Z_SharpCapacityThresholdsinLinearAssociativeMemory_F.md"
date: 2026-05-06
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-06_17-53-20Z_SharpCapacityThresholdsinLinearAssociativeMemory_F.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-05-07 23:08
Source: 2026-05-06_17-53-20Z_SharpCapacityThresholdsinLinearAssociativeMemory_F.md
Model: None

---


## Summary  
The paper investigates how many key‑value associations a $d\times d$ linear memory can store, showing that the capacity depends on both storage degrees of freedom and retrieval criterion. It derives sharp scaling laws for winner‑take‑all (top‑1) decoding and listwise decoding under a Tail‑Average Margin criterion. For Gaussian isotropic models, top‑1 requires $n\asymp d^2/\log n$ while listwise admits quadratic capacity $d^2\asymp \alpha n$. The authors also develop an exact asymptotic theory for the TAM risk minimizer.

## Key Contributions  
- [Finding 1] Top‑1 retrieval in linear associative memory has a logarithmic capacity bound $d^2 \asymp n\log n$, driven by extreme‑value statistics.  
- [Finding 2] Listwise retrieval with Tail‑Average Margin admits quadratic capacity $d^2 \asymp \alpha n$, supported by an exact asymptotic risk‑minimizing solution.  
- [Finding 3] The same quadratic scaling is necessary for any linear memory under the TAM criterion, and a small‑tail extrapolation suggests a sharp top‑1 threshold of order $2n\log n$.

## Methodology  
The authors adopt an isotropic Gaussian model where each stored pair corresponds to a vector in $\mathbb{R}^d$. They analyze two retrieval regimes: winner‑take‑all (top‑1) which requires the correct signal to dominate all distractors, and listwise decoding governed by the convex Tail‑Average Margin (TAM), defined as the probability that the true target lies within the top‑$\alpha$ candidates. Capacity is derived via extreme‑value theory for top‑1 and a two‑parameter scalar variational principle for TAM risk.

## Results  
Theoretical analysis yields $d^2 \asymp n\log n$ for winner‑take‑all, establishing a sharp phase transition in the correlation matrix construction. For listwise retrieval, an exact asymptotic theorem shows that at load $\alpha = n/d^2$, the TAM empirical‑risk minimizer separates satisfiable and unsatisfiable phases with a ridgeless critical load given by $\alpha_c = 1/2$. The theory also predicts limiting distributions for true scores, competitor scores, margins, and percentile profiles. Small‑tail extrapolation further suggests that the optimal top‑1 threshold scales as $d^2 \approx 2 n\log n$.

## Significance  
These results clarify why logarithmic scaling appears in winner‑take‑all associative memory models, linking it to extreme‑value phenomena rather than mere dimensionality. The quadratic capacity for listwise decoding under TAM demonstrates a fundamentally different regime where redundancy is tolerated and retrieval can be robust. Together they provide a unified framework for interpreting linear memory performance across diverse retrieval strategies.

## Related Concepts  
- Winner‑take‑all decoding  
- Listwise retrieval  
- Tail‑Average Margin (TAM) criterion  
- Extreme‑value statistics  
- Correlation matrix memory construction

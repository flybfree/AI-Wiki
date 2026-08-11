---
title: From Approachability Residuals to Anytime-Valid Evidence: The Online Convex Geometry of Testing by Betting
url: http://arxiv.org/abs/2608.09450v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_11-23-30Z_FromApproachabilityResidualstoAnytime_ValidEvidenc.md
generated_at: 2026-08-10 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper establishes a precise algebraic link between betting‑based sequential tests and Blackwell approachability by using support‑function residuals of an online convex learner. It derives a pathwise identity for the target distance, shows how bounded residuals translate into finite‑time test outcomes, and demonstrates that this framework recovers deterministic Blackwell games in the noise‑free case.

## Key Takeaways
- The exact pathwise identity dist(\bar r_T,S) = (1/T)\sum_{t=1}^T q_t + Reg_T/T shows how learner residuals directly measure approachability.  
- Bounded residuals |q_t| ≤ B allow a finite‑time transfer: if OCO and log‑wealth regrets are at most a_T and ℓ_T, then a gap exceeding a_T/T + 2B√((log(1/α)+ℓ_T)/T) forces rejection by time T.  
- The resulting wealth process under adaptive nulls yields exponential separation when mean separation persists at rate δ²/(4B²), linking sublinear OCO regret to stochastic approachability.

## Context
This work bridges online convex optimization and hypothesis testing, offering a unified probabilistic framework that quantifies how learning uncertainty translates into statistical evidence. By treating test outcomes as betting profits, the paper provides a concrete operational method for evaluating model performance under controlled experimental settings.

## Implications
For practitioners in AI research and industry, this protocol enables automated hypothesis testing without relying on fixed null models, supporting adaptive data collection and risk‑aware decision making. The exact algebraic connection also offers a benchmark for evaluating new learning algorithms through their impact on test statistics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09450v1)

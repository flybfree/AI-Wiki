---
title: Amortizing the Calibration Triple: A Projection-Consistent Neural Operator for Local-Stochastic Volatility
url: http://arxiv.org/abs/2608.01217v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_13-03-48Z_AmortizingtheCalibrationTriple_AProjection_Consist.md
generated_at: 2026-08-03 23:38
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a projection‑consistent neural operator that amortizes the costly fixed‑point calibration of local‑stochastic volatility. By reformulating the calibration problem in log‑implied‑variance coordinates and using Gyöngy’s quotient Fokker–Planck equation, the authors train a DeepONet or FNO to jointly produce an implied‑volatility surface, Dupire local volatility, LSV leverage, and the conditional moment required by the projection identity. Empirical results show that calibration latency drops from 98.5 ms to 0.6 ms while reducing root‑mean‑square errors in local‑volatility and leverage by up to 36 % and 16 %, respectively.

## Key Takeaways
- The calibration triple (implied surface, Dupire volatility, LSV leverage) is learned via a division‑free residual system that enforces static‑arbitrage constraints.  
- Empirical tests demonstrate that forward‑start and cliquet errors are reduced to 0.1 % and 0.2 % compared with particle methods, indicating strong consistency under the existence of LSV and stability of the inverse residual.  
- The heavy calibration solve is moved offline; online inference reduces to a single operator evaluation, achieving sub‑millisecond latency.

## Context
The paper addresses a persistent bottleneck in quantitative finance where stochastic volatility models require iterative fixed‑point solves that are too slow for real‑time trading. Recent advances in neural operators provide scalable alternatives, yet few have been tailored to the specific calibration constraints of LSV. This work bridges AI research and market practice by delivering a projection‑consistent framework that respects both statistical consistency and arbitrage rules.

## Implications
For traders and risk managers, this method enables near‑instantaneous pricing adjustments without sacrificing model fidelity, supporting high‑frequency strategies that rely on stochastic volatility surfaces. Practitioners can integrate the operator into existing pipelines with minimal latency impact, while researchers gain a benchmark for projection‑consistent neural operators in financial modeling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01217v1)

---
title: Climate-Dyna Deep Hedging for XVAs: Model-Based Reinforcement Learning, Residual Climate HVA, and Hedge-Instrument Discovery
published: 2026-08-02T12:48:24Z
authors: Xiaozhen Wang, Francois Buet-Golfouse
url: http://arxiv.org/abs/2608.01208v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Climate-Dyna Deep Hedging for XVAs: Model-Based Reinforcement Learning, Residual Climate HVA, and Hedge-Instrument Discovery

## Abstract
For a trading desk, residual climate hedging valuation adjustment (HVA) is the climate cost left after its inherited hedge and any admissible overlay have been taken into account; it therefore cannot be inferred from a stand-alone stress loss. We obtain this residual by comparing paired climate-on and baseline worlds and reoptimizing the overlay for each hedge universe, which also turns hedge-instrument discovery into a valuation problem: an instrument is useful to the extent that it lowers the optimized residual cost. The linear-Gaussian case has an exact finite-horizon Riccati solution; Climate-Dyna starts from that hedge and learns the remaining nonlinear correction from paired world-model rollouts, with an independent gate deciding whether to deploy the update. In a public-data-calibrated semi-synthetic EU ETS study, crediting the inherited hedge lowers the mean climate charge from 1.517 to 0.906, and the learned overlay lowers it to 0.831 against a 0.821 exact floor; residual Dyna cuts regret by 93% relative to replay with one quarter as many trajectories, while adaptation from only 25 target transitions retains 60.7% of the exact-assisted gain.

## Metadata
- **Published**: 2026-08-02T12:48:24Z
- **Authors**: Xiaozhen Wang, Francois Buet-Golfouse
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01208v1)
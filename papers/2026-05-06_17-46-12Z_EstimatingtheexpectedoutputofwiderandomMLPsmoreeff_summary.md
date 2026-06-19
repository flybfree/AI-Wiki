---
title: "2026 05 06 17 46 12Z Estimatingtheexpectedoutputofwiderandommlpsmoreeff Summary"
date: 2026-05-06
tags: ['paper', 'research', 'ai']
---
# Estimating the expected output of wide random MLPs more efficiently than sampling


**Source**: [Original Paper](http://arxiv.org/abs/2605.05179v1)
Saved: 2026-05-07 22:08
Source: 2026-05-06_17-46-12Z_EstimatingtheexpectedoutputofwiderandomMLPsmoreeff.md

---

## Summary
This paper proposes an alternative to Monte Carlo sampling for estimating the expected output of wide random MLPs at initialization. Instead of forwarding samples through the network, the method builds approximate representations of layerwise activation distributions using cumulants and Hermite expansions. The authors show that, for sufficiently wide networks, this approach can reach a target mean-squared error with substantially fewer FLOPs than direct sampling.

## Key Takeaways
- Expectation estimation need not rely on brute-force sampling.
- Distributional approximations can be cheaper and more accurate in wide regimes.
- The method is especially effective for rare-event probability estimation.

## Context
The work addresses expected-loss estimation at network initialization for Gaussian inputs. It also explores how the estimator can be used during model training.

## Implications
If scalable in practice, this technique could improve efficiency in uncertainty estimation and tail-risk analysis. The paper also suggests a possible route toward training models with lower catastrophic-tail probability.

## Original Reference
- Title: Estimating the expected output of wide random MLPs more efficiently than sampling
- Authors: Wilson Wu, Victor Lecomte, Michael Winer, George Robinson, Jacob Hilton, Paul Christiano
- Published: 2026-05-06T17:46:12Z
- URL: http://arxiv.org/abs/2605.05179v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-05-06_17-46-12Z_EstimatingtheexpectedoutputofwiderandomMLPsmoreeff.md
---
title: REFLEX: Reflexive Equilibrium Fixed-point Learning for Endogenous eXchanges
published: 2026-08-17T06:19:06Z
authors: Vignesh Nagarajan, Shriraghav Ashok
url: http://arxiv.org/abs/2608.16155v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REFLEX: Reflexive Equilibrium Fixed-point Learning for Endogenous eXchanges

## Abstract
In over-the-counter corporate bond markets, dealers compete for client trades by quoting bid and ask prices. Tighter quotes attract more business, but also informed customers more likely to trade ahead of adverse price moves, leaving the dealer holding the risk. As dealers increasingly use machine learning to set quotes, they retrain these models on the trades their own quotes attract, creating a feedback loop in which each model reshapes the market that generates its next training data. The question is therefore not only whether a quoting model performs well, but whether the market it creates stays stable as the model learns from it. Existing performative prediction theory gives a sharp stability condition, yet expresses it through abstract properties of the learning objective a trading desk cannot measure before deployment. We introduce REFLEX, a framework that replaces those unobservable quantities with three measurable features of dealer behavior: how strongly trading volume responds to tighter quotes, how sharply the dealer's objective bends around its optimum, and how quickly informed flow increases as spreads narrow. REFLEX combines these into a single retraining modulus, a pre-deployment stability margin estimated from a desk's own quote and execution history that predicts whether repeated retraining will converge or amplify itself. In simulation, predicted and measured stability agree within 8%, and competing dealers increase instability by 1.74x with two and 3.16x with three, as predicted. Where ordinary retraining becomes unstable at modulus 1.21, a structurally anchored correction converges as blind retraining collapses. Calibrated over 36 years of public market data, stability headroom falls roughly 4.4x for investment grade and 4.3x for high yield from calm to crisis regimes. Ultimately, REFLEX turns an abstract convergence theorem into a market-level safety margin.

## Metadata
- **Published**: 2026-08-17T06:19:06Z
- **Authors**: Vignesh Nagarajan, Shriraghav Ashok
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16155v1)
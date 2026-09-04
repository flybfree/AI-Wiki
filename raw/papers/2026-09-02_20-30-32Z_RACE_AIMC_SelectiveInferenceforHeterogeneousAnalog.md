---
title: RACE-AIMC: Selective Inference for Heterogeneous Analog In-Memory Accelerators at the Edge
published: 2026-09-02T20:30:32Z
authors: Osama Yousuf, Martin Lueker-Boden
url: http://arxiv.org/abs/2609.03149v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RACE-AIMC: Selective Inference for Heterogeneous Analog In-Memory Accelerators at the Edge

## Abstract
Analog in-memory computing (AIMC) speeds up neural-network inference by doing the arithmetic directly inside a memory array, instead of shuttling weights back and forth between memory and a processor. This saves energy, but the physical devices that store the weights are imperfect: programming errors, electrical noise, limited-resolution converters, and outright broken cells all distort the computation, and every physical chip is distorted in its own way. A designer with several such chips available faces an uncomfortable choice: run all of them and combine the answers (safe, but wasteful of energy), or trust a single chip blindly (cheap, but with no guarantee on how often it is wrong). This paper introduces RACE-AIMC (Risk-Aware Certified Ensemble for AIMC), a framework that resolves this choice with statistics rather than guesswork. Offline, RACE-AIMC studies a pool of physical accelerators, picks the single best one for a given energy budget, and computes a mathematically exact upper bound on how often that accelerator will be wrong when it chooses to answer. Online, only that one accelerator is switched on; a lightweight check decides whether to accept its answer or defer to a fallback. In our simulations using a noisy weight mapping and multiple independent test runs, every certified bound stayed under a 10% error target (mean bound 7.83% +- 0.89%, with 70.88% +- 0.98% of inputs answered directly). The resulting system matches the accuracy of a clean digital baseline while cutting modeled energy use by 69.02% relative to always running every accelerator in the pool.

## Metadata
- **Published**: 2026-09-02T20:30:32Z
- **Authors**: Osama Yousuf, Martin Lueker-Boden
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03149v1)
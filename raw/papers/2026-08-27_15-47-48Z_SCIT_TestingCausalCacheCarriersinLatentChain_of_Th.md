---
title: SCIT: Testing Causal Cache Carriers in Latent Chain-of-Thought Models
published: 2026-08-27T15:47:48Z
authors: Yi Ding, Lijun Huang, Menglin Yang
url: http://arxiv.org/abs/2608.27265v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCIT: Testing Causal Cache Carriers in Latent Chain-of-Thought Models

## Abstract
Latent chain-of-thought models move intermediate reasoning from emitted text into continuous states, improving compactness but hiding the causal object. We introduce SCIT, the Suffix Cache Interchange Test, a causal protocol that constructs exact source-recipient counterfactuals, patches declared cache segments, and identifies which transformer object carries the counterfactual computation. SCIT combines sufficiency tests with K/V component splits, hidden-state controls, semantic source controls, decoded validation, and matched corruption. On CODI-GPT2 and a Sim-CoT-style GPT-2 reproduction, counterfactual arithmetic transfers primarily through value-cache suffix trajectories rather than hidden states, keys, reusable answer slots, or single-token triggers. Complete sufficiency-and-necessity evidence for the late-value-suffix mechanism holds for the main CODI-GPT2 checkpoint; the Sim-CoT-style checkpoint shows the same sufficiency and decoded-control pattern but insufficient matched-corruption evidence for a necessity call. Beyond these local arithmetic cells, SCIT reveals carrier-regime shifts: arithmetic-like GPT-2/1B cells preserve latent-tail value/KV transfer, whereas competent 8B and repaired non-arithmetic cells route through prompt-prefix or full-cache K/V; boundary cells receive no mechanism call. SCIT therefore contributes a cache-level diagnostic, a checkpoint-specific GPT-2 arithmetic mechanism, and a competence-gated carrier map rather than a universal latent-tail claim.

## Metadata
- **Published**: 2026-08-27T15:47:48Z
- **Authors**: Yi Ding, Lijun Huang, Menglin Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27265v1)
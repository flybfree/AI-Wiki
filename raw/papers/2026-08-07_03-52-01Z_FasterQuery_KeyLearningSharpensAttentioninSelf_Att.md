---
title: Faster Query-Key Learning Sharpens Attention in Self-Attention Models
published: 2026-08-07T03:52:01Z
authors: Rahul Vashisht, Harish G. Ramaswamy
url: http://arxiv.org/abs/2608.06776v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Faster Query-Key Learning Sharpens Attention in Self-Attention Models

## Abstract
A standard self-attention layer consists of two interacting circuits: the query-key circuit that governs attention allocation, and the output-value circuit that maps attended representations to predictions. Collapsed and factorized parameterizations of the query-key and output-value circuits lead to qualitatively different attention patterns. In particular, some parameterizations give sharper attention to task-relevant tokens, at a similar training loss. We analyze how the parameterizations of these circuits shape the parameter trajectories in single-layer self-attention models trained for next-token prediction. Through gradient-flow analysis, we show that factorization induces implicit rescaling of the two circuits' learning rates. We derive closed-form dynamics showing that output-value and query-key parameters move along a line, with relative speeds determined by their learning rates. Faster query-key learning relative to output-value learning thus produces sharper attention, as the model compensates for slower output-value learning by increasing attention mass on relevant tokens. Experiments show that differences in the relative learning rates of the two circuits govern attention concentration. This improves attention interpretability proxies while maintaining comparable predictive performance.

## Metadata
- **Published**: 2026-08-07T03:52:01Z
- **Authors**: Rahul Vashisht, Harish G. Ramaswamy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06776v1)
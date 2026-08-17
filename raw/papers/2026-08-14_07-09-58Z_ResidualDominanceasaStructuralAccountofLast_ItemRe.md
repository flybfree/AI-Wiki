---
title: Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders
published: 2026-08-14T07:09:58Z
authors: Keito Kozaki, Keigo Sakurai, Ren Togo, Takahiro Ogawa, Miki Haseyama
url: http://arxiv.org/abs/2608.14021v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders

## Abstract
Transformer-based sequential recommenders with causal self-attention often rely heavily on the most recent interaction at inference time, but how this behavior is structurally expressed in the representation used for prediction remains unclear. We combine prediction-time diagnostics with norm-based analysis of the full attention block. First, we show that SASRec-style models exhibit highly localized last-item reliance. We then find that, although self-attention aggregates contextual information, residual addition sharply shifts the full-block representation toward same-position contributions, which we term residual dominance. To probe this interpretation, we use inference-time residual scaling as a controlled diagnostic intervention. Changing the residual strength induces a monotonic trade-off between structural mixing and last-item reliance, while reducing residual strength recovers a subset of final-position misses for which representations at non-final positions already rank the ground-truth item correctly. Our results provide a structural account linking extreme last-item reliance to residual dominance at inference time. The code is publicly available.

## Metadata
- **Published**: 2026-08-14T07:09:58Z
- **Authors**: Keito Kozaki, Keigo Sakurai, Ren Togo, Takahiro Ogawa, Miki Haseyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14021v1)
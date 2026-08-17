---
title: Non-Parametric Spatiotemporal Trajectory Prediction via State-Conditioned Transition Sampling
published: 2026-08-14T14:42:21Z
authors: Michael Fore, Akshay Jain, Justin Downes, Rohan Pradhan, Duncan Botti
url: http://arxiv.org/abs/2608.14349v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Non-Parametric Spatiotemporal Trajectory Prediction via State-Conditioned Transition Sampling

## Abstract
We present a training-free method for multi-modal trajectory prediction that achieves comparable accuracy to a 57M-parameter transformer while requiring no GPU and zero learned parameters. The method builds a transition table of historical state-to-next-position pairs and retrieves neighbors using a product kernel over spatial proximity, bearing, speed, and temporal context. Two inference modes operate over this shared representation: diversity-penalized sampling produces trajectories covering distinct plausible routes, while beam search finds the highest-likelihood path. On the TrAISformer benchmark (Danish Maritime AIS), our method achieves competitive accuracy at full data availability and dramatically outperforms the transformer in data-scarce regimes---remaining stable down to 10% of training data where TrAISformer degrades catastrophically. This enables deployment in new geographic regions from an order of magnitude less historical data, and with no GPU training.

## Metadata
- **Published**: 2026-08-14T14:42:21Z
- **Authors**: Michael Fore, Akshay Jain, Justin Downes, Rohan Pradhan, Duncan Botti
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14349v1)
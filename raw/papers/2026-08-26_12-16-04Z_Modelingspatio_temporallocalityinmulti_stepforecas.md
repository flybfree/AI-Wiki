---
title: Modeling spatio-temporal locality in multi-step forecasting of geo-referenced time series
published: 2026-08-26T12:16:04Z
authors: Annunziata D'Aversa, Gianvito Pio, Michelangelo Ceci
url: http://arxiv.org/abs/2608.25698v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Modeling spatio-temporal locality in multi-step forecasting of geo-referenced time series

## Abstract
Forecasting future measurements from geographically distributed sensors is essential across many domains. However, the spatial distribution of these sensors raises multiple challenges, primarily due to spatial autocorrelation phenomena, that introduce inter-dependencies among nearby locations, that cannot therefore be treated independently. While some existing approaches can capture such phenomena, they generally model the spatial dimension globally across all locations. On the other hand, the method we propose in this paper, called SPALT, focuses on capturing spatial relationships among time series with similar trends, even if they occur at different times, thus modeling the spatio-temporal locality. SPALT leverages linear model trees, which allow us to consider the spatial autocorrelation locally: during the tree-building process, the adopted heuristics group time series exhibiting similar trends into the same node, on which additional features considering the spatial dimension are selectively injected. Additionally, we propose a new pruning strategy, based on Reduced Error Pruning, that also considers the spatio-temporal locality during the tree simplification. Designed for a multi-step setting, SPALT provides forecasts for multiple future time steps across multiple sensors simultaneously. The characteristics exhibited by SPALT can provide significant benefits in different domains, where measurements come from distributed sensors. In this paper, we focus on data produced by sensors located in multiple renewable power plants measuring their energy production at regular, short intervals. Experiments on 3 real-world datasets demonstrate the effectiveness of SPALT in forecasting the production of energy at different time horizons, and its superior performance in comparison with tree-based models and state-of-the-art neural networks that incorporate both temporal and spatial dimensions.

## Metadata
- **Published**: 2026-08-26T12:16:04Z
- **Authors**: Annunziata D'Aversa, Gianvito Pio, Michelangelo Ceci
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25698v1)
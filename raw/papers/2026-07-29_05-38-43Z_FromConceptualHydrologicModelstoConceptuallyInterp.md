---
title: From Conceptual Hydrologic Models to Conceptually Interpretable Neural Networks: A Snow-Water Mass-Conserving-Perceptron Framework for Discovering Catchment-Scale Precipitation-Storage-Runoff Representations
published: 2026-07-29T05:38:43Z
authors: Yuan-Heng Wang, Hoshin V. Gupta
url: http://arxiv.org/abs/2607.26492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Conceptual Hydrologic Models to Conceptually Interpretable Neural Networks: A Snow-Water Mass-Conserving-Perceptron Framework for Discovering Catchment-Scale Precipitation-Storage-Runoff Representations

## Abstract
The Mass-Conserving Perceptron (MCP) establishes a modeling paradigm in which conceptual hydrologic models can be reformulated as physically constrained, conceptually interpretable neural networks. Here, we develop a snow-water MCP network framework and evaluate it across 513 CAMELS-US basins. We first recast a coupled two-state SOIL-MCP and SNOWMCP conceptual model as a mass-conserving neural network and show that the hydrologic-model and neural-network formulations achieve comparable predictive performance. We then examine cross-node state-information sharing within two-state HYDROMCP architectures and evaluate broader single-layer networks constructed from three types of interpretable MCP units with one to five states. Across CONUS, the median KGEss increases from 0.82 for one-state networks to 0.89 for two-state networks and 0.90 for five-state networks, suggesting diminishing aggregate gains beyond two states. Basin-specific MCP and LSTM selection yields the same median KGEss of 0.90, while the selected MCP networks use fewer parameters on average. Complementary AIC- and KGE-based selection identifies compact, basin-specific directed-graph representations that balance predictive accuracy and model complexity. These analyses provide an empirical basis for identifying the numbers, types, and interactions of states needed for hydrologic representation. Future studies should test joint training against multiple hydrologic responses, such as streamflow, snow water equivalent, and groundwater storage.

## Metadata
- **Published**: 2026-07-29T05:38:43Z
- **Authors**: Yuan-Heng Wang, Hoshin V. Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26492v1)
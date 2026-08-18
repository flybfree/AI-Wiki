---
title: Toward AI-Friendly Cartography: Understanding How Color Design Influences Foundation Model Spatial Reasoning on Sequential Choropleth Maps
published: 2026-08-16T13:24:31Z
authors: Yonghe Sun, Zhenjia Liu, Hua Liao, Wenjia Xu, Nai Yang, Weihua Dong, Zhiwei Wei
url: http://arxiv.org/abs/2608.15736v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward AI-Friendly Cartography: Understanding How Color Design Influences Foundation Model Spatial Reasoning on Sequential Choropleth Maps

## Abstract
Foundation models (FMs) increasingly support multimodal and geospatial reasoning, yet it remains unclear whether cartographic principles designed for human perception are equally effective for machines. Focusing on sequential choropleth maps, we examine how hue palette, color ordering, and lightness contrast influence FM spatial reasoning. We construct a controlled benchmark of 5,760 maps and 28,800 questions spanning Attribute Identify, Spatial Recognition, Compare, Rank, and Pattern Delineate, and evaluate 21 open-source and proprietary multimodal FMs. Results show that hue choice has limited and inconsistent effects, whereas disrupting sequential color ordering substantially reduces performance, especially for comparison and ranking. Reduced lightness contrast also consistently impairs reasoning, while increasing contrast beyond sufficient separability provides only marginal gains. LoRA fine-tuning improves overall accuracy but preserves these relative sensitivities. Additional factorial experiments further indicate that errors arise from color-and-legend decoding, spatial reasoning, and the integration of thematic attributes with spatial structure. These findings show that conventional sequential ordering and sufficient contrast remain important for machine map understanding and provide empirical guidance for AI-friendly cartographic design.

## Metadata
- **Published**: 2026-08-16T13:24:31Z
- **Authors**: Yonghe Sun, Zhenjia Liu, Hua Liao, Wenjia Xu, Nai Yang, Weihua Dong, Zhiwei Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15736v1)
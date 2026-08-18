---
title: ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning
published: 2026-08-15T15:46:46Z
authors: Ziyue Yang, Chaolin Xu, Yijing Wang, Tiankai Gu, Hui Yang, Yanhong Lin, Kaiyuan Liu, Fei Xiao
url: http://arxiv.org/abs/2608.15291v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning

## Abstract
Demand forecasting increasingly requires combining two complementary sources of information: historical sales reveal recurring numerical dynamics, while future promotions, holidays, price changes, and platform interventions provide forward-looking knowledge. Existing text-enhanced forecasting methods often encode such context into generic representations and fuse it uniformly with time-series features, without explicitly distinguishing which semantic effects are forecast-relevant or how they should modify future dynamics.   We introduce ReasonCast, a structured semantic intervention framework that translates event knowledge into forecast-specific operations. An agent examines the event context, the no-text forecast, and its uncertainty to determine whether textual reasoning is needed. Rather than injecting free-form text, ReasonCast represents event knowledge through structured fields describing event relevance, demand direction, temporal shape, amplitude, and peak intensity. These fields interact selectively with temporal components of a time-series foundation model. An additive path corrects local trends and temporal shapes, while a multiplicative path captures event-driven level shifts.   ReasonCast introduces a forecast-grounded post-training curriculum. Schema SFT establishes semantic fields; semantic-field RL calibrates direction, shape, amplitude, and peak judgments; and forecast-utility RL evaluates semantic interventions through a frozen forecaster, aligning reasoning outputs with marginal forecast improvement. ReasonCast lowers WMAPE by 3.29, 1.25, and 0.47 percentage points on holiday-sensitive categories, mega-sale-sensitive categories, and M5 event windows, respectively. On stable-sales periods, indiscriminate semantic intervention increases WMAPE by 1.68 percentage points, whereas suppressing unnecessary intervention preserves the numerical backbone.

## Metadata
- **Published**: 2026-08-15T15:46:46Z
- **Authors**: Ziyue Yang, Chaolin Xu, Yijing Wang, Tiankai Gu, Hui Yang, Yanhong Lin, Kaiyuan Liu, Fei Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15291v1)
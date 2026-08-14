---
title: Demand Transfer Estimation at Scale via Restricted Logit Modeling
published: 2026-08-13T00:37:13Z
authors: Lakshya Garg, Deep Narayan Mishra, Swapnil Yadav, Haoan Wang, Sujal Alugubelli, Karthik Kumaran, Anupriya Sharma
url: http://arxiv.org/abs/2608.12680v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Demand Transfer Estimation at Scale via Restricted Logit Modeling

## Abstract
Item demand forecasting is an integral component of store assortment optimization. Existing literature focuses on learning a suitable customer choice model and using this model to determine the value of an objective function (i.e. expected demand) with respect to an assortment proposal. However, for large item universe with many categories, this approach can prove inefficient, needing a separate demand forecast for every possible item assortment. An alternate approach exists whereby we combine the efficiency of forecasting item demand independently, while at the same time applying adjustments to the independent forecasts that account for the relations between item demand and the availability of other similar items on the shelf.   Central to this approach is the estimation of Demand Transfer (DT) coefficients. These DT coefficients represent the percent of a particular target item's (item that the customer walked in the store to buy) demand that is redirected to each other item in the universe should the target item be removed from the shelf. We introduce an approach that allows us to compute these DT coefficients on large item universes (assortments having 1 million+ items). Experiments on data as well as historical transaction data for multiple locations within categories demonstrate that when certain reasonable assumptions about substitution behavior are satisfied, our procedure is able to accurately estimate underlying DT coefficients and lead to improvements in demand forecasting.

## Metadata
- **Published**: 2026-08-13T00:37:13Z
- **Authors**: Lakshya Garg, Deep Narayan Mishra, Swapnil Yadav, Haoan Wang, Sujal Alugubelli, Karthik Kumaran, Anupriya Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12680v1)
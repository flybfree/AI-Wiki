---
title: Convolution Smoothed Quantile Regression for XGBoost
published: 2026-08-15T15:44:19Z
authors: Mandy Yao, Meredith Franklin
url: http://arxiv.org/abs/2608.15290v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Convolution Smoothed Quantile Regression for XGBoost

## Abstract
The increasing availability of large and complex datasets across many scientific disciplines has led to widespread adoption of machine learning (ML) for prediction. However, most ML algorithms focus on point estimation and provide limited information about predictive uncertainty or the conditional distribution of the response, restricting their ability to characterize rare or extreme outcomes. We develop QXGB, a quantile-based gradient boosting framework, and introduce a convolution smoothed loss within it that estimates conditional quantiles for constructing dense cumulative distribution functions (CDFs), exceedance probabilities, and tail behaviour relevant to extreme outcomes. This approach preserves the computational efficiency of extreme gradient boosting while restoring the Hessian information XGBoost relies on for tree splitting, in turn providing interpretable measures of extreme value and exceedance probability predictions. We derive the gradients and Hessians needed to integrate convolution smoothed quantile loss with different kernel specifications into XGBoost, and with simulated data, benchmark this approach against alternative smoothed quantile regression losses, the native quantile objective in the XGBoost Python package, and independent versus multi-output tree estimation. The practical relevance is illustrated in an application predicting fine particulate matter (PM$_{2.5}$) in northern California, including periods where levels were elevated due to wildfire smoke. Our results show that convolution smoothed QXGB, particularly when paired with multi-output trees, delivers accurate predictions with near-zero quantile crossing, well-calibrated CDF and exceedance probability estimates, and useful tail characterization for extreme values. Interval estimation is also evaluated as a measure of data spread.

## Metadata
- **Published**: 2026-08-15T15:44:19Z
- **Authors**: Mandy Yao, Meredith Franklin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15290v1)
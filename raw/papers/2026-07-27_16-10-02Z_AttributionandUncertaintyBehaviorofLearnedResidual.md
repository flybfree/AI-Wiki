---
title: Attribution and Uncertainty Behavior of Learned Residual Gyro Correction for Gyro-Stellar Estimation
published: 2026-07-27T16:10:02Z
authors: Mariela De Lucas Álvarez, Melvin Laux, Arthur de Freitas Precht, Maurice Martin, Edoardo Caroselli, Frank Kirchner, Alexander Fabisch
url: http://arxiv.org/abs/2607.24608v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Attribution and Uncertainty Behavior of Learned Residual Gyro Correction for Gyro-Stellar Estimation

## Abstract
This work investigates uncertainty decomposition and explainability in a deep learning-based framework for gyroscope bias correction. A 1-D Convolutional Neural Network is trained to predict residual angular rate corrections from multi-sensor inputs, including gyroscope and star tracker measurements. The bias corrections are sent to a flight-representative Gyro-Stellar Estimator. The network produces both mean corrections and input-dependent (heteroscedastic) aleatoric uncertainty, while epistemic uncertainty is estimated via an ensemble of independently trained models.   The proposed approach is trained under nominal conditions and evaluated in both nominal and structured perturbations that include additive and temporally correlated noise. Gradient-based attribution methods are applied to both the correction and uncertainty outputs, enabling a decomposition of the evidence that drives state updates and uncertainty estimates. By aggregating attribution patterns across rotational axes and regimes, we reveal axis-specific behaviors and characterize how structured perturbations influence the collaboration between aleatoric and epistemic uncertainty.   Uncertainty analysis shows that aleatoric uncertainty increases with perturbation intensity, but the distributions overlap and the calibration is not consistent across regimes. On the other hand, epistemic uncertainty gives a clear signal that gets clearer as the distributional shift happens, showing that the models disagree more. These results show that aleatoric and epistemic uncertainty work well together and that epistemic uncertainty is better at distinguishing between nominal and perturbed operating conditions. The results provide insight into the behavior of hybrid learning-based state estimation components and motivate the use of uncertainty for downstream monitoring and fault detection.

## Metadata
- **Published**: 2026-07-27T16:10:02Z
- **Authors**: Mariela De Lucas Álvarez, Melvin Laux, Arthur de Freitas Precht, Maurice Martin, Edoardo Caroselli, Frank Kirchner, Alexander Fabisch
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24608v1)
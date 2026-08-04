---
title: An Uncertainty-Driven Hybrid Deep Learning Approach for Broad-Coverage RF Modulation Recognition
published: 2026-08-01T17:57:36Z
authors: Nurettin Safak, Durdu Can Yerdeyatar, Muhammet Sefa Demirel, Alperen Marasli, Taha Eren Atmaca, Ozgun Ersoy
url: http://arxiv.org/abs/2608.00796v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Uncertainty-Driven Hybrid Deep Learning Approach for Broad-Coverage RF Modulation Recognition

## Abstract
Automatic RF modulation recognition is of critical importance in spectrum monitoring, electronic warfare, and cognitive radio applications, where low signal-to-noise ratio (SNR) conditions and the growing diversity of modulation schemes limit the performance of existing methods. This paper proposes an uncertainty-driven hybrid deep learning architecture for recognizing RF signals over a broad modulation space. The proposed approach carries out a multi-stage classification process by combining spectral information obtained through low-cost FFT-based preprocessing with time-frequency features extracted from short-time Fourier transform (STFT) spectrograms. The architecture comprises a 2D convolutional neural network (2D CNN)-based path for fast, low-latency primary classification, MC Dropout-supported Bayesian uncertainty estimation for assessing classification reliability, and a BiLSTM-based secondary decision mechanism activated under high-uncertainty conditions. The proposed system is evaluated in a controlled simulation environment spanning different SNR levels and modulation classes. Experimental results show that the primary 2D CNN path achieves $83.3\pm0.7\%$ accuracy with an inference time of only 0.138 ms per sample, providing superior performance compared with traditional rule-based and classical machine-learning approaches. Furthermore, the obtained findings reveal the limitations of compact spectral feature representations and classifiers lacking temporal modeling, particularly in disambiguating FSK-based modulations. The uncertainty estimation module offers promising results for detecting low-confidence decisions, and the proposed approach demonstrates the potential of a low-latency and scalable solution for real-time RF modulation recognition.

## Metadata
- **Published**: 2026-08-01T17:57:36Z
- **Authors**: Nurettin Safak, Durdu Can Yerdeyatar, Muhammet Sefa Demirel, Alperen Marasli, Taha Eren Atmaca, Ozgun Ersoy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00796v1)
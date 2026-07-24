---
title: A Quantum-Classical Hybrid Framework for Multivariate Time-Series Forecasting Complexity-Fidelity Trade-offs and Limitations
published: 2026-07-17T10:30:12Z
authors: Sanjay Chakraborty, Fredrik Heintz
url: http://arxiv.org/abs/2607.16358v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Quantum-Classical Hybrid Framework for Multivariate Time-Series Forecasting Complexity-Fidelity Trade-offs and Limitations

## Abstract
This paper presents a unified quantum-classical hybrid framework for multi-horizon time-series forecasting, introducing two model variants Quantum Reservoir Forecaster (QRC-F) and Variational Quantum Forecaster (VQF-F). The proposed framework investigates the complexity-fidelity trade-off of quantum forecasting under near-term NISQ hardware constraints. Continuous time-series signals are transformed into binary representations through uniform quantization and encoded into quantum states using angle encoding with parameterized RY rotation gates. Cross-channel entanglement layers capture dependencies among multiple variables. QRC-F utilizes a fixed random unitary quantum reservoir for stable, gradient-free temporal feature extraction, whereas VQF-F employs a trainable variational quantum circuit optimized through the parameter-shift rule to learn temporal and inter-variable patterns from Pauli expectation values. Both models replace computationally expensive quadratic self-attention with efficient linear transformations, reducing parameter complexity. A shared MIMO-based multi-horizon prediction head simultaneously generates forecasts across multiple horizons, avoiding error accumulation in recursive forecasting. Experimental evaluations on benchmark datasets, including ETTh1, ETTh2, ETTm1, ETTm2, Weather, electricity, and exchange-rate, demonstrate that VQF-F achieves superior training stability and parameter efficiency, while QRC-F provides enhanced robustness and circuit fidelity under quantum noise. The results establish a practical quantum-native forecasting framework with strong potential for deployment on near-term NISQ devices.

## Metadata
- **Published**: 2026-07-17T10:30:12Z
- **Authors**: Sanjay Chakraborty, Fredrik Heintz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16358v1)
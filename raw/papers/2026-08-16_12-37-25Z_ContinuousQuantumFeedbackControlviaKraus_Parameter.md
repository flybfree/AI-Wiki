---
title: Continuous Quantum Feedback Control via Kraus-Parameterized Belief Reinforcement Learning
published: 2026-08-16T12:37:25Z
authors: Priyanshi Singh, Krishna Bhatia
url: http://arxiv.org/abs/2608.15715v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Continuous Quantum Feedback Control via Kraus-Parameterized Belief Reinforcement Learning

## Abstract
Quantum feedback control requires acting on noisy continuous measurement records without direct access to the underlying quantum state. We propose Kraus-Parameterized Belief Reinforcement Learning, a pipeline in which a recurrent encoder, constrained to the Stiefel manifold, produces density-matrix estimates that are guaranteed positive-semidefinite and trace-normalized by construction, embedding quantum state geometry directly into the learning loop. A Proximal Policy Optimization (PPO) actor then maps these physically valid belief states to continuous control actions. On a simulated continuously monitored qubit, the resulting policy achieves stable feedback control, maintaining a measurement-conditioned belief fidelity of approximately 0.77-0.80 and exhibiting substantially lower return variance than a parameter-matched LSTM-history baseline across both nominal and out-of-distribution conditions. Although gains in raw target fidelity are modest, the geometric constraint guarantees a physically valid, interpretable belief representation and yields markedly more stable control under measurement inefficiency and abrupt dynamics switches. These results indicate that physics-informed neural memory is a practical inductive bias for reliable quantum feedback control.

## Metadata
- **Published**: 2026-08-16T12:37:25Z
- **Authors**: Priyanshi Singh, Krishna Bhatia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15715v1)
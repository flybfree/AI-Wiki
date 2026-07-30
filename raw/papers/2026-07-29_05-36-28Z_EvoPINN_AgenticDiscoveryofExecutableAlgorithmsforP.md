---
title: EvoPINN: Agentic Discovery of Executable Algorithms for Physics-Informed Neural Networks
published: 2026-07-29T05:36:28Z
authors: Peng Yin, Kai Li, Yifan Zhang, Jian Cheng
url: http://arxiv.org/abs/2607.26490v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoPINN: Agentic Discovery of Executable Algorithms for Physics-Informed Neural Networks

## Abstract
Physics-informed neural networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs), yet their performance heavily relies on the manual, trial-and-error engineering of neural representations, loss formulations, and optimization dynamics. While Large Language Models (LLMs) offer a promising avenue for automated design, unconstrained code generation often yields mathematically invalid or numerically unstable solutions under strict scientific computing constraints. To bridge this gap, we propose \textbf{EvoPINN}, an agentic framework that reformulates PINN development from labor-intensive manual design into a rigorous, execution-grounded algorithm discovery problem. EvoPINN navigates a modular search space by decoupling neural representations from training programs, utilizing an LLM agent to iteratively propose memory-conditioned programmatic modifications. To ensure scientific validity, all candidates undergo strict structural verification and budget-matched PDE evaluation. Extensive experiments across diverse PDE regimes (oscillatory, elliptic, dissipative, and nonlinear transport) demonstrate that EvoPINN discovers PDE-specialized learning algorithms that significantly reduce relative $L_{2}$ error compared to baselines. Crucially, EvoPINN autonomously invented SLRC-PINN, a novel architecture whose performance gains persist under rigorous parameter-matched comparisons, establishing the viability of execution-grounded agents for discovering genuinely new scientific computing mechanisms.

## Metadata
- **Published**: 2026-07-29T05:36:28Z
- **Authors**: Peng Yin, Kai Li, Yifan Zhang, Jian Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26490v1)
---
title: Scaling of Capability and Efficiency at Inference Time in Large Reasoning Models
published: 2026-09-22T23:56:45Z
authors: Moritz Laber, Zohair Shafi, Germans Savcisens, Brennan Klein, Matteo Chinazzi, Samuel V. Scarpino, Albert-László Barabási, Tina Eliassi-Rad
url: http://arxiv.org/abs/2609.27166v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling of Capability and Efficiency at Inference Time in Large Reasoning Models

## Abstract
Capability and efficiency are two key dimensions of reasoning in large language models (LLMs). Capability refers to the ability to solve a given problem correctly, whereas efficiency refers to the ability to do so with limited resources. When LLMs use Chain-of-Thought (CoT) reasoning to solve problems of controlled hardness, both the number of problems solved correctly and the number of tokens required to reach a correct answer depend on problem hardness and model size. However, how these factors jointly shape capability and efficiency remains poorly understood. Here, we use hierarchical Bayesian models to evaluate the capability and efficiency of LLMs from the DeepSeek-R1-Distill model family across four classes of arithmetic and algorithmic reasoning problems. At a fixed model size, the probability of correctly solving an instance decays approximately exponentially with instance size, our proxy for problem hardness. The decay scale grows sublinearly with model size, indicating that larger models are more capable, but that capability gains diminish with scale. Output length grows as a power law with instance size, which serves as a proxy for difficulty. However, the parameters of this power law do not vary systematically with model size, suggesting that larger models do not become more efficient. Together, these findings reveal potential limitations of naive scaling as a strategy for developing more capable AI systems: capability improves with diminishing returns, while efficiency shows little to no improvement.

## Metadata
- **Published**: 2026-09-22T23:56:45Z
- **Authors**: Moritz Laber, Zohair Shafi, Germans Savcisens, Brennan Klein, Matteo Chinazzi, Samuel V. Scarpino, Albert-László Barabási, Tina Eliassi-Rad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27166v1)
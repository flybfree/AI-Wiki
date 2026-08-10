---
title: The Sparsity Whisperer
published: 2026-08-06T22:37:26Z
authors: Linghao Kong, Inimai Subramanian, Micah Adler, Dan Alistarh, Dan Gutfreund, Nir Shavit
url: http://arxiv.org/abs/2608.06630v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Sparsity Whisperer

## Abstract
Pruning reduces the inference cost of large language models, but existing criteria primarily preserve large activations or reconstruct layer outputs. We argue that this overlooks a key computation performed by particularly sparsity-sensitive neurons in the MLP up and gate projections: separating similar inputs into dissimilar outputs. This suggests that effective pruning should preserve not only activations, but also the differences between outputs more broadly. We introduce a family of difference-informed pruning methods built upon this principle. Wisp is a first-order, update-free method that scores weights using input-difference norms, and Wisp+ refines this score neuronwise using the input pairs each neuron separates most strongly. Finally, Whisper is a second-order method that uses a lightly regularized difference Hessian as its reconstruction objective. Across Llama 2 and 3.1 models from 7B to 405B parameters, our second-order variant consistently improves over strong reconstruction-based baselines, while our update-free variants improve over activation-aware baselines, especially in constrained settings. The improvements over Wanda and SparseGPT extend to structured sparsity, downstream evaluations, and other model families. Augmenting stronger techniques such as RIA and ALPS with our difference-informed criteria yields further improvements, shifting the overall accuracy-runtime frontier outward at negligible additional cost. These results suggest that preserving output differences is a broadly useful and composable signal for post-training LLM sparsification.

## Metadata
- **Published**: 2026-08-06T22:37:26Z
- **Authors**: Linghao Kong, Inimai Subramanian, Micah Adler, Dan Alistarh, Dan Gutfreund, Nir Shavit
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06630v1)
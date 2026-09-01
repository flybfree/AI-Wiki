---
title: When Errors Become Memories: Causal Pathway Tracing in Multi-Turn Memory-Augmented LLMs
published: 2026-08-31T03:26:32Z
authors: Shuyao Xiao, Shengling Wang, Xuan Chen, Ke Chao, Ming Cui, Feifei Qian, Fanlin Meng, Chaoyang Mei, Chaoyong Jiang, Qi Ouyang, Junxi Yi
url: http://arxiv.org/abs/2608.30198v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Errors Become Memories: Causal Pathway Tracing in Multi-Turn Memory-Augmented LLMs

## Abstract
Long-term memory enables large language models (LLMs) to preserve and reuse information across interactions, but it can also turn localized errors into persistent risks. Existing work mainly evaluates whether memory systems store and retrieve information correctly, leaving limited understanding of how errors propagate across responses, memory states, and future interactions. We propose a structural causal model (SCM)-based framework for cross-turn error propagation in memory-augmented LLMs. We model user questions, model responses, and memory states as a dynamic causal process, and identify two entry pathways: internal memory updating and external question feedback. By intervening on these pathways, we construct four counterfactual trajectories and quantify their downstream effects and interaction. Error influence is evaluated at four levels: memory retention, natural responses, targeted diagnostic probing, and probability-level error preference. Experiments show that error influence generally decays with interaction distance, while the memory-update pathway contributes more persistent effects than question feedback; latent errors may remain even after disappearing from natural responses. Propagation patterns also vary across memory categories and memory mechanisms. Pathway-guided restoration further validates this decomposition: Question Repair reduces residual error by 27.5%, Memory Repair by 70.2%, and Joint Repair by 98.3%, nearly eliminating residual propagation.

## Metadata
- **Published**: 2026-08-31T03:26:32Z
- **Authors**: Shuyao Xiao, Shengling Wang, Xuan Chen, Ke Chao, Ming Cui, Feifei Qian, Fanlin Meng, Chaoyang Mei, Chaoyong Jiang, Qi Ouyang, Junxi Yi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30198v1)
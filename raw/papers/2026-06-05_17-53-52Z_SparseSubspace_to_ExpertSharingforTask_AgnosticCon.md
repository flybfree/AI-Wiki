---

title: Sparse Subspace-to-Expert Sharing for Task-Agnostic Continual Learning
published: "2026-06-05T17:53:52Z"
authors: Fatema Siddika, Md Anwar Hossen, Tanwi Mallick, Ali Jannesari
url: http://arxiv.org/abs/2606.07500v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Sparse Subspace-to-Expert Sharing for Task-Agnostic Continual Learning



**Source**: [Original Paper](http://arxiv.org/abs/2606.07500v1)
## Abstract
Continual learning in Large Language Models (LLMs) is hindered by the plasticity-stability dilemma, where acquiring new capabilities often leads to catastrophic forgetting of previous knowledge. Existing methods typically treat parameters uniformly, failing to distinguish between specific task knowledge and shared capabilities. We introduce Mixture of Sparse Experts for Task Agnostic Continual Learning (SETA), a framework that resolves the plasticity-stability conflict through adaptive sparse subspace decomposition into task-specific expert modules. Unlike standard updates, where tasks compete for the same parameters, SETA separates knowledge into unique experts, designed to isolate task-specific patterns, and shared experts, responsible for capturing common features. This structure is maintained through adaptive elastic anchoring and a routing-aware regularization that jointly protect shared knowledge at both the weight and routing levels and enable a unified gating network to automatically retrieve the correct expert combination during inference. Extensive experiments across diverse domain-specific benchmarks demonstrate that SETA achieves competitive or superior overall performance relative to state-of-the-art continual learning baselines, with particularly strong retention of early-task knowledge and improved backward transfer on LLaMA-2 7B and Qwen3-4B.

## Metadata
- **Published**: 2026-06-05T17:53:52Z
- **Authors**: Fatema Siddika, Md Anwar Hossen, Tanwi Mallick, Ali Jannesari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.07500v1)
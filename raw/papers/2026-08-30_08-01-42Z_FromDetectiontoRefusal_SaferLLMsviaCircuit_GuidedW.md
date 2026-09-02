---
title: From Detection to Refusal: Safer LLMs via Circuit-Guided Weight Scaling
published: 2026-08-30T08:01:42Z
authors: Kuan-Lin Chu, Chung-En Sun, Tsui-Wei Weng
url: http://arxiv.org/abs/2609.00051v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Detection to Refusal: Safer LLMs via Circuit-Guided Weight Scaling

## Abstract
Despite extensive alignment efforts, Large Language Models (LLMs) remain vulnerable to generating unsafe content under adversarial prompting, yet the internal mechanisms by which safety behaviors are implemented remain poorly understood. We study LLM safety from a mechanistic interpretability perspective and characterize a multi-stage *safety circuit* that organizes refusal behavior, consisting of (i) $\textbf{Harmful Detection Heads}$ that respond to harmful inputs, (ii) $\textbf{Safety Neurons}$ that mediate and stabilize safety signals in the residual stream, and (iii) $\textbf{Refusal Heads}$ that translate these signals into safe response generation. Using targeted attention-head and neuron-level interventions, we provide causal evidence consistent with this circuit organization, showing that suppressing upstream Harmful Detection Heads disrupts downstream refusal behavior and that safety neurons mediate this interaction. We validate that this decomposition recurs across multiple LLM architectures and adversarial attack settings, and use simple, architecture-preserving weight scaling as a mechanistic probe to test its functional relevance. Across six LLMs, circuit-guided scaling improves safety rates under attacks by 26.5%, while incurring only a 1.7% accuracy drop across four standard benchmarks. Overall, our results support a circuit-level interpretation of LLM safety and suggest that mechanistic abstractions can reveal stable and transferable patterns underlying aligned behavior.

## Metadata
- **Published**: 2026-08-30T08:01:42Z
- **Authors**: Kuan-Lin Chu, Chung-En Sun, Tsui-Wei Weng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00051v1)
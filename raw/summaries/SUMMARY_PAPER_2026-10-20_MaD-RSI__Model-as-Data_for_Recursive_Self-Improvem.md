---
title: MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses
url: http://arxiv.org/abs/2610.28201v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_13-41-00Z_MaD_RSI_Model_as_DataforRecursiveSelf_Improvemento.md
generated_at: 2026-10-20 22:11
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MaD-RSI introduces a paradigm shift in recursive self-improvement (RSI) for LLM agent harnesses by treating multiple heterogeneous models as training data rather than as post-hoc evaluation targets. The framework directly optimizes a single shared harness by incorporating diverse failure trajectories from multiple LLMs into the training loop, yielding improved cross-model generalization and reduced computational costs compared to prior single-model RSI methods.

## Key Takeaways
- Existing RSI methods create a strong coupling between the optimized harness and its target LLM, meaning a harness tuned for one model generalizes poorly to others and requires substantial retraining when new models are introduced. MaD-RSI breaks this coupling by centering the harness as the optimization target and using model differences as constructive training signals rather than mere evaluation criteria.
- The framework incorporates diverse failure trajectories from multiple heterogeneous LLMs directly into the training process, leveraging model-specific behavioral differences as evidence to guide the self-improvement of a shared harness. This transforms model diversity from a generalization challenge into a training asset.
- The authors introduce a new evaluation framework with two complementary metrics specifically designed to assess harness optimization effectiveness across models, addressing the gap in how prior work measures cross-model transferability. Experiments across multiple datasets and LLMs confirm that MaD-RSI outperforms existing approaches in generalization while simultaneously reducing training costs.

## Context
Recursive self-improvement of agent harnesses sits at the intersection of automated prompt engineering, tool-use optimization, and meta-learning for LLM agents. As the number of available LLMs grows and organizations deploy heterogeneous model stacks, the ability to build harnesses that generalize across models without per-model retraining becomes a critical scalability concern. MaD-RSI addresses this by reframing the optimization problem around the harness itself, drawing on ideas from multi-task learning and data augmentation to make model diversity a productive signal.

## Implications
For practitioners deploying agent systems across multiple LLM providers, MaD-RSI offers a path to building reusable harnesses that adapt to new models with minimal additional training, significantly lowering the operational cost of maintaining agent pipelines. For the broader research community, the "model-as-data" framing challenges the prevailing assumption that model differences are obstacles to be measured after training, suggesting instead that heterogeneous model behavior is a rich source of training signal that can drive more robust and generalizable agent architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28201v1)

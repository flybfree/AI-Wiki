---
title: T-Router: Learning Thalamic Routing for Reasoning with Parameter-Efficient Reinforcement Learning
url: http://arxiv.org/abs/2609.39109v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_06-48-06Z_T_Router_LearningThalamicRoutingforReasoningwithPa.md
generated_at: 2026-09-30 20:52
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces T-Router, a parameter-efficient reinforcement learning method that improves reasoning by adapting how a pretrained model reuses completed computations rather than modifying its weights. By utilizing a compressed, addressable bank and a depth-recurrent controller to manage context-dependent routing of block changes, T-Router achieves state-of-the-art performance on mathematical benchmarks while adding only 0.466% parameters to an 8.95B backbone model.

## Key Takeaways
- T-Router implements a thalamic-inspired routing mechanism where a depth-recurrent controller conditions the selection and relative-scale writeback of block changes stored in a compressed, addressable bank, enabling layers to dynamically learn which earlier computational contributions to utilize without altering backbone parameters or layer order.
- The method allocates just 41.73M parameters on an 8.95B model and achieves a MathAvg score of 83.64 ± 1.16 after GSM8K reinforcement learning, significantly outperforming full-parameter GRPO (73.79) and LoRA (77.28), while also raising mean AIME accuracy from 48.33 to 60.56 across multiple task families with matched retries.
- Capacity-controlled comparisons highlight the benefits of addressable block changes and recurrent context, and separate search training extends the interface to tool-mediated reasoning, establishing controlled computation reuse as a robust and scalable route for parameter-efficient reinforcement learning in reasoning tasks.

## Context
As large language models scale, parameter-efficient fine-tuning has become critical to reduce computational overhead while maintaining performance, yet reinforcement learning for reasoning remains expensive and often relies on full-model updates or less flexible adaptation techniques. T-Router addresses this gap by proposing a structured approach to computation reuse inspired by biological routing, offering a biologically plausible alternative that complements existing PEFT methods and aligns with the field's push toward more efficient, scalable model improvement strategies.

## Implications
The demonstrated efficacy of T-Router suggests that controlled computation reuse can serve as a highly effective paradigm for scaling reasoning capabilities without the prohibitive costs associated with full-parameter reinforcement learning, potentially democratizing access to advanced model training for smaller organizations. Practitioners and industry stakeholders can adopt this approach to deploy reasoning-enhanced models with minimal parameter overhead, enabling faster iteration cycles, reduced storage requirements, and more efficient resource utilization in production environments where compute budgets are constrained.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39109v1)

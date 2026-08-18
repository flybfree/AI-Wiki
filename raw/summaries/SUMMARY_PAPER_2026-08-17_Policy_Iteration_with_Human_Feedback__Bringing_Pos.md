---
title: Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context Learning
url: http://arxiv.org/abs/2608.16831v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_17-16-43Z_PolicyIterationwithHumanFeedback_BringingPost_Trai.md
generated_at: 2026-08-17 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Policy Iteration with Human Feedback (PIHF), a framework that uses a pretrained language model as an execution substrate while iteratively refining a natural‑language policy and tool set through expert review. By localizing failures in reasoning and tool use, PIHF generates candidate revisions that are validated by Recall@1 and Recall@5 metrics. The approach yields significant improvements in rare‑disease diagnosis benchmarks, raising Recall@1 by 32.7 points for GPT‑5.4 and 31.1 points for Qwen3.6‑35B.

## Key Takeaways
- PIHF combines a fixed pretrained language model with a human expert loop that reviews reasoning traces to produce versioned policy revisions, creating a recurrent evaluate‑and‑improve cycle.
- The framework’s validation relies on Recall@1 and Recall@5, which measure how often the best candidate matches the correct answer after execution, providing objective feedback for each revision attempt.
- Experiments show that PIHF can boost diagnostic recall by over 30 percentage points across both proprietary and open‑weight large language models, demonstrating strong performance gains even with ultra‑rare disease data.

## Context
Generative pretraining has enabled reusable task representations, while in‑context learning shows static models can adapt to new tasks from instructions. PIHF extends this idea by moving the policy revision process into a human‑in‑the‑loop system that continuously evaluates and updates the model’s behavior without retraining.

## Implications
The results suggest that expert‑guided policy iteration can be integrated into existing large language systems, offering a scalable way to improve rare‑disease diagnostic tools. Practitioners may adopt PIHF to fine‑tune high‑stakes applications where human oversight is critical and model updates are costly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16831v1)

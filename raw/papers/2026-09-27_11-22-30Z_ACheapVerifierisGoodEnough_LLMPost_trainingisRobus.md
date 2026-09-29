---
title: A Cheap Verifier is Good Enough: LLM Post-training is Robust to Erroneous Rewards
published: 2026-09-27T11:22:30Z
authors: Andreas Plesner, Curtis Northcutt, Francisco Guzmán, Anish Athalye
url: http://arxiv.org/abs/2609.33467v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Cheap Verifier is Good Enough: LLM Post-training is Robust to Erroneous Rewards

## Abstract
When post-training large language models on tasks with semi-verifiable rewards, there are many factors (training steps, base model size, training order, data quality, verifier accuracy, etc.) that practitioners must contend with to maximize model performance. Yet, it remains unclear how well verifier agreement predicts post-training performance on such tasks. In this paper, we explore this question with over 11k H100 GPU-hours, across HealthBench and PRBench tasks in medical, legal, and finance domains. Across the tested domains, Qwen3 trainees (1.7B-8B on HealthBench; 8B on PRBench), evaluation splits, and frontier LLM reference judges (which we call golden verifiers), higher verifier agreement does not consistently identify the best training verifier. Expensive verifiers need not outperform inexpensive ones, and open-weight Gemma verifiers produce strong training outcomes. We compare two low-cost choices retrospectively -- a cost-reducing choice and a balanced choice -- with estimated grading cost reductions of 98.8%-99.7% relative to the golden grading protocols and average post-training score gaps of 1-3 points from the best evaluated training verifier. These averages include larger losses in individual settings; they do not establish that verifier choices are interchangeable.

## Metadata
- **Published**: 2026-09-27T11:22:30Z
- **Authors**: Andreas Plesner, Curtis Northcutt, Francisco Guzmán, Anish Athalye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33467v1)
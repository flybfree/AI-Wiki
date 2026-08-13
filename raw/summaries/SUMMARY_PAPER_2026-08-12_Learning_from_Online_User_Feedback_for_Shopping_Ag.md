---
title: Learning from Online User Feedback for Shopping Agents
url: http://arxiv.org/abs/2608.11604v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_03-24-44Z_LearningfromOnlineUserFeedbackforShoppingAgents.md
generated_at: 2026-08-12 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LOFA, a framework that learns from real online user feedback in shopping agents without human annotation. It combines reinforcement learning using purchase outcomes with feedback‑aware on‑policy distillation to turn conversational directives into token‑level supervision. Experiments show LOFA improves recommendation quality, response helpfulness, and user satisfaction over baselines.

## Key Takeaways
- LOFA leverages real online interaction logs as supervision by converting users' natural conversational feedback into dense token‑level labels without manual annotation.
- The framework merges reinforcement learning based on verifiable purchase outcomes with an on‑policy distillation step that extracts directives from dialogue.
- Experimental results demonstrate consistent gains in recommendation quality, response helpfulness, and user satisfaction alignment compared to strong baselines.

## Context
Current e‑commerce systems rely heavily on offline signals such as clicks or synthetic preferences, which cannot capture the nuanced language feedback users provide. Incorporating these rich but noisy conversational logs could unlock more personalized agents.

## Implications
For practitioners, LOFA offers a practical way to continuously improve shopping agents using existing interaction data. This reduces reliance on costly annotation pipelines and aligns agent behavior with actual user preferences in real time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11604v1)

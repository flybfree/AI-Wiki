---
title: A Unified Framework to Elicit Structured Feedback for Interpretable Multi-Trait Essay Scoring
published: 2026-08-28T14:57:07Z
authors: Shihang Yang, Sanwoo Lee, Ningning Zhao, Yunfang Wu
url: http://arxiv.org/abs/2608.28407v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Unified Framework to Elicit Structured Feedback for Interpretable Multi-Trait Essay Scoring

## Abstract
Multi-trait Automated Essay Scoring (AES) requires rubric-grounded reasoning across interdependent traits, rather than isolated score prediction. Existing feedback-enhanced methods often decouple feedback from scoring or assess traits independently, weakening score--feedback consistency and rubric alignment. We propose HiFTS, a unified autoregressive framework that generates hierarchical CoT feedback before predicting trait-level and holistic scores. HiFTS distills rubric-grounded hierarchical CoT feedback from a teacher LLM and trains student models to jointly generate feedback and scores. HiFTS further applies Group Relative Policy Optimization with a composite reward balancing score agreement, calibration, feedback quality, and structural validity. At inference, a lightweight global prior provides holistic guidance to reduce drift during long-form reasoning. We also introduce CFMS-34, a Chinese multi-trait AES dataset with 951 essays annotated with holistic scores and 34 rubric-based traits. Experiments on CFMS-34 and ASAP++ show that HiFTS achieves strong holistic and trait-level scoring while producing coherent, rubric-aligned feedback.

## Metadata
- **Published**: 2026-08-28T14:57:07Z
- **Authors**: Shihang Yang, Sanwoo Lee, Ningning Zhao, Yunfang Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28407v1)
---
title: Glance, Scrutinize, and Think: Advancing Video Anomaly Detection from Training-Free to Agentic Reasoning
published: 2026-08-07T17:07:49Z
authors: Shibo Gao, Peipei Yang, Xu-Yao Zhang, Linlin Huang
url: http://arxiv.org/abs/2608.11260v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Glance, Scrutinize, and Think: Advancing Video Anomaly Detection from Training-Free to Agentic Reasoning

## Abstract
Video Anomaly Detection (VAD) aims to identify anomalous events and localize their temporal intervals. Existing approaches exhibit a "when-what" dissociation: traditional DNN-based methods localize when anomalies occur but lack semantic understanding, whereas LLM-based methods explain what happens but neglect precise temporal grounding. We attribute this to the absence of a unified reasoning paradigm. Inspired by how humans inspect surveillance videos - glancing globally to form temporal hypotheses, scrutinizing suspicious segments, and thinking iteratively to correct errors - we study this global-to-local paradigm from two perspectives. We first propose Glance then Scrutinize (GtS), a training-free framework using static and dynamic textual guidance for coarse-to-fine anomaly grounding and understanding, balancing accuracy and speed. To break the ceiling imposed by frozen external modules, we further propose a tool-augmented agentic VAD method, where a multimodal large language model learns to invoke a video cropping tool, inspect densely resampled frames, and self-correct mislocalized hypotheses, via cold-start supervised fine-tuning followed by reinforcement learning with a joint answer-grounding reward. For training and evaluation, we extend our prior VAGU benchmark into VAGU-T (Video Anomaly Grounding, Understanding, and Thinking), comprising 7,567 real-world videos over 21 anomaly categories with human-validated grounding, explanations, QA pairs, and chain-of-thought tool-calling traces. We further introduce JeAUG, a metric jointly evaluating semantic interpretability and temporal precision. Experiments show that GtS substantially surpasses training-free baselines, while the agentic model delivers both higher accuracy and faster inference.

## Metadata
- **Published**: 2026-08-07T17:07:49Z
- **Authors**: Shibo Gao, Peipei Yang, Xu-Yao Zhang, Linlin Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11260v1)
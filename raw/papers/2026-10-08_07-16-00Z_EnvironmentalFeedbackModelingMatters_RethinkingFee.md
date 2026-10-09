---
title: Environmental Feedback Modeling Matters: Rethinking Feedback Treatment in Agentic Hindsight Self-Distillation
published: 2026-10-08T07:16:00Z
authors: Hangxi Guo, Fengyuan Liu, Yue Wang, Yuhua Qi, Haoyi Xiong, Fei Sun, Mengnan Du
url: http://arxiv.org/abs/2610.11384v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Environmental Feedback Modeling Matters: Rethinking Feedback Treatment in Agentic Hindsight Self-Distillation

## Abstract
Reinforcement learning is commonly used to train language agents in interactive environments, but cannot be directly applied when rewards are unavailable. Recent methods use environmental feedback as privileged context for hindsight self-distillation, but our analysis suggests that simply conditioning the teacher on feedback is insufficient, motivating us to rethink how environmental feedback is used in agentic self-distillation. Given that environmental feedback contains rich supervision for modeling how the environment responds to agent actions, we introduce \textit{agentic SElf-distilLation with environmental Feedback modeling} (SELF), a framework that jointly optimizes environmental feedback modeling and hindsight self-distillation. SELF learns to predict environmental responses while distilling guidance from a feedback-conditioned self-teacher into the policy. Our analysis reveals a mutually reinforcing mechanism: environmental feedback modeling strengthens hindsight supervision and policy learning, while self-distillation enhances the model's ability to model environmental feedback. With Qwen3-8B, SELF outperforms SDPO and GRPO by 6.4 and 4.1 percentage points in $τ$-bench success rate, and by 10.71 and 3.57 percentage points in AppWorld task goal completion, respectively. These results show that SELF uses environmental feedback more effectively within agentic self-distillation, improving agent capabilities.

## Metadata
- **Published**: 2026-10-08T07:16:00Z
- **Authors**: Hangxi Guo, Fengyuan Liu, Yue Wang, Yuhua Qi, Haoyi Xiong, Fei Sun, Mengnan Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11384v1)
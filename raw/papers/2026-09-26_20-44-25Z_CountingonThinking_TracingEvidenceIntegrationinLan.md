---
title: Counting on Thinking: Tracing Evidence Integration in Language Models
published: 2026-09-26T20:44:25Z
authors: Jingming Xue, Robert C. Wilson, Huadong Xiong
url: http://arxiv.org/abs/2609.32932v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Counting on Thinking: Tracing Evidence Integration in Language Models

## Abstract
Finite computational resources force a tradeoff between automatic System 1 processes and costly System 2 thinking. Large language models (LLMs) can spend extra computation on hard problems, yet direct answers struggle even with counting, an elementary operation humans and animals perform automatically. We ask why this requires thinking in LLMs. Evidence integration has long been used in psychology and neuroscience to probe decision-making. Our evidence-integration task presents one letter per conversational turn and asks which of two target letters appeared more often. A running count difference solves the task optimally by weighting every letter equally; tokens at each turn could represent and update this difference. Direct responses instead weighted evidence unevenly, with strong recency effects, and assigned less probability to the correct answer as difficulty increased. Thinking improved performance and made integration weights nearly uniform, yet final-query attention remained concentrated on the sequence ends in both modes. Reasoning trajectories showed models revisiting input, recounting letters, and checking intermediate counts that informed the answer, suggesting that thinking constructs the accumulated count that direct responses lack rather than reading out one already formed. Reasoning-token costs grew with the number of letters far more than with coherence. Outcome feedback did not bring this computation into direct responses: under in-context reinforcement learning (ICRL), performance deteriorated over repeated games and recency effects strengthened, yet models grew more confident. Humans and animals amortize such computations into automatic processes, whereas current LLMs still pay for them with thinking on every trial. Which operations learning can make directly available remains central to how future models allocate computation.

## Metadata
- **Published**: 2026-09-26T20:44:25Z
- **Authors**: Jingming Xue, Robert C. Wilson, Huadong Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32932v1)
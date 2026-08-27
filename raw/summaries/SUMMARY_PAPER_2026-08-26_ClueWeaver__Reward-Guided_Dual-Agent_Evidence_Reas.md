---
title: ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives
url: http://arxiv.org/abs/2608.25531v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_08-39-09Z_ClueWeaver_Reward_GuidedDual_AgentEvidenceReasonin.md
generated_at: 2026-08-26 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
ClueWeaver is a dual-agent framework that enables compact local language models to answer questions on long literary narratives by selecting evidence and generating interpretable rationales. The approach separates evidence retrieval from inference, allowing inspectable reasoning while improving performance over end‑to‑end prompting.

## Key Takeaways
- Finder selects passages via retrieval‑guided segmentation to retain answer‑critical clues.
- Interpreter generates rationales with paragraph‑ID citations and self‑calibration for high‑risk questions.
- Reward‑guided reinforcement learning optimizes both agents: Finder rewards evidence retention, Interpreter rewards correctness.

## Context
This work addresses the challenge of deploying large language models locally on long texts where full context is impractical. It offers a modular approach that improves interpretability and efficiency for humanities research tasks.

## Implications
Practitioners can rely on compact models for nuanced literary analysis while maintaining traceable reasoning, supporting trustworthy AI in scholarly settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25531v1)

---
title: Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory for the Humanoid Robot Head Kim
url: http://arxiv.org/abs/2607.24190v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_09-11-55Z_NotForgotten_ImplementationandEvaluationofaPersona.md
generated_at: 2026-07-27 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a lightweight episodic memory module for the humanoid robot Kim that stores and retrieves past interactions using vector similarity and LLM prompts. Evaluation in an online study with 43 participants showed that episodic recall boosted perceived sociability, trustworthiness, and warmth while leaving disturbance unchanged.

## Key Takeaways
- The hybrid scoring function combines cosine similarity with a memory strength metric to retrieve relevant past dialogues, enabling personalized context injection during LLM generation. - Within‑subjects results indicate episodic memory significantly raises scores on trustworthiness (d = 0.62) and warmth (d = 0.56), confirming its social benefit. - Perceived disturbance remains unchanged (d = 0.00), suggesting the approach avoids privacy discomfort or uncanny valley effects.

## Context
Current AI chatbots lack persistent memory, limiting their ability to sustain human‑like relationships. Embedding episodic recall into embodied robots addresses a gap in social robotics by providing continuity across sessions.

## Implications
Integrating personalized memory can improve user trust and engagement for service bots, making them more effective in customer support or companionship roles. Practitioners should consider lightweight retrieval methods to balance performance with privacy constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24190v1)

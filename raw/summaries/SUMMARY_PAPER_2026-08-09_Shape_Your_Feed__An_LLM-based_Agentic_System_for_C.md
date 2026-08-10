---
title: Shape Your Feed: An LLM-based Agentic System for Conversational Recommendation
url: http://arxiv.org/abs/2608.06632v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_22-54-16Z_ShapeYourFeed_AnLLM_basedAgenticSystemforConversat.md
generated_at: 2026-08-09 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Shape Your Feed, an LLM‑based agentic system that lets users shape their recommendation feed in real time using natural language or voice commands. It combines perception, serving and self‑evolution flows to align user intent with content ranking, achieving high alignment accuracy and measurable gains on relevance and sentiment.

## Key Takeaways
- The framework captures fine‑grained user intent from text prompts, voice commands, and UI interactions through a Perception Flow that creates a persistent Semantic Profile. 
- Real‑time agentic re‑ranking and pruning of candidate items is performed in the Serving Flow, using the evolving profile to steer the feed dynamically. 
- The Self‑Evolution Flow aligns system behavior with human judgments via Direct Preference Optimization and an LLM‑as‑a‑Judge ensemble, improving alignment scoring to 98.85% accuracy.

## Context
Industrial recommendation systems have long relied on passive ranking that infers preferences from implicit signals, creating a gap between what users want and what they receive. This work bridges that gap by introducing an interactive, user‑steerable paradigm grounded in large language models.

## Implications
SYF demonstrates a scalable path toward truly interactive recommendations for production environments, offering practitioners a concrete method to integrate LLM agents into existing recommendation pipelines. The approach could transform user experience across e‑commerce, media, and content platforms by making feeds responsive to explicit preferences.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06632v1)

---
title: Bootstrapping Conversational Recommendation Agents At Spotify: Synthetic Data Generation and Self-Improvement Loops
published: 2026-09-16T14:48:02Z
authors: Enrico Palumbo, Alexandre Tamborrino, Victor Ode, Ben Lacker, Adrià Casas Escoda, Jeremy Hopple, Marcus Better, James Leoni, Hugo Galvão, Hugues Bouchard, Mounia Lalmas, José Luis Redondo García, Abenezer Abebe, Ann Clifton, Anton Blomberg, Henrik Lindström, Dani Doro, Christine Doig Cardet
url: http://arxiv.org/abs/2609.30297v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bootstrapping Conversational Recommendation Agents At Spotify: Synthetic Data Generation and Self-Improvement Loops

## Abstract
Conversational recommendation agents are a new paradigm for content discovery, enabling users to express complex intents through natural language (e.g., "recommend Italian indie artists I haven't heard before"). A central challenge in building such agents is optimizing agent planning -- deciding how to select, sequence, and invoke tools -- particularly in cold-start settings where real user interactions are not yet available. We introduce a pipeline for multi-turn synthetic data generation and a self-improvement loop to address this challenge. The synthetic data pipeline transforms single-turn prompts into realistic multi-turn conversations, enabling systematic evaluation before launch. The self-improvement loop combines variance-based contrastive optimization with iterative refinement through a coding agent, automatically identifying and fixing planning and tool-use errors. Our approach improves quality by +8% on top of a highly optimized manual prompt. The system has been productionized and significantly accelerated iteration cycles for the launch of a conversational recommendation agent at Spotify. Online A/B tests demonstrate its effectiveness, with +14% user listening, +5% increase in weekly active users, and a 5% reduction in skip rate compared to a prior experience supporting only session refinement. This work provides a practical framework for accelerating the development of conversational recommendation agents in industry.

## Metadata
- **Published**: 2026-09-16T14:48:02Z
- **Authors**: Enrico Palumbo, Alexandre Tamborrino, Victor Ode, Ben Lacker, Adrià Casas Escoda, Jeremy Hopple, Marcus Better, James Leoni, Hugo Galvão, Hugues Bouchard, Mounia Lalmas, José Luis Redondo García, Abenezer Abebe, Ann Clifton, Anton Blomberg, Henrik Lindström, Dani Doro, Christine Doig Cardet
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30297v1)
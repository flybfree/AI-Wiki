---
title: What Keeps Agent Skills from Being Reusable? Evidence from 138K SKILL.md Files
url: http://arxiv.org/abs/2608.08453v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_03-49-30Z_WhatKeepsAgentSkillsfromBeingReusable_Evidencefrom.md
generated_at: 2026-08-10 22:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why many publicly shared agent skills fail to be reusable, using a defect taxonomy on 138,133 SKILL.md files from 20,556 repositories. It finds that over nine out of ten skills contain at least one detectable issue, and that routing metadata problems are the most common failure mode.

## Key Takeaways
- The majority of skills exhibit defects such as weak or missing routing metadata, bloated bodies, or disorganized resources, which hinder reliable retrieval from LLM agents.  
- Defect rates remain high even under lenient definitions (88.8‑94.6 %) and are consistent across different evaluation thresholds, indicating a pervasive quality issue.  
- Skills that include specification awareness have fewer defects than those marked as AI-generated, which suffer more from safety and portability concerns.

## Context
Agent skills are meant to encapsulate reusable procedures for LLM agents, allowing them to persist beyond single interactions. The rapid proliferation of public skill repositories has raised expectations for interoperability, yet the current analysis reveals a systematic breakdown in how these components are structured and validated.

## Implications
For developers and platform maintainers, the findings suggest that without standardized quality checks, agent skills risk becoming brittle and unusable. Implementing lightweight linting pipelines and repair mechanisms could improve reliability and encourage broader adoption of reusable AI workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08453v1)

---
title: $τ$-Emotion-Bench: Exposing the Interaction Fragility of LLM Agents through Real-World User Emotions
url: http://arxiv.org/abs/2610.19560v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_04-19-15Z_τ__Emotion_Bench_ExposingtheInteractionFragilityof.md
generated_at: 2026-10-14 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces τ-Emotion-Bench, a ten-domain benchmark designed to evaluate tool-calling LLM agents under controlled, emotion-conditioned user interactions, exposing how emotional variation in user behavior undermines agent reliability in long-horizon tasks. The authors also present Tracer, a scalable agentic data-generation pipeline that constructs grounded tasks and collects interaction trajectories through an agent-user-environment harness, enabling both benchmark construction and agent training. Experiments demonstrate that frontier agents remain unreliable under emotional user variation, while Tracer-generated supervision consistently improves Qwen3 models across scales and generalizes to unseen domains.

## Key Takeaways
- Existing benchmarks for tool-calling agents assume cooperative and behaviorally stable users, leaving the effect of emotional variation on agent reliability largely unexplored. τ-Emotion-Bench addresses this gap by introducing controlled emotion-conditioned user interactions across ten domains while preserving the underlying task objective, revealing substantial gaps between average task success and consistent task completion for frontier agents.
- Tracer is a scalable agentic data-generation pipeline that constructs grounded, policy-valid tasks and collects trajectories through an interactive agent-user-environment harness. By allowing dissatisfied users to terminate inefficient interactions, the harness provides an interaction-aware signal that filters trajectories with excessive user dependence and favors effective tool use, enabling scalable supervision for training agents.
- Behavioral analyses show that higher task success correlates with a better balance between tool execution and necessary user follow-up, and Tracer-generated supervision consistently improves Qwen3 models across scales, generalizes to unseen domains, and transfers to existing benchmarks such as τ-Bench and τ-Trait, demonstrating the practical value of interaction-aware training signals.

## Context
This work sits at the intersection of agentic AI evaluation and human-computer interaction research. As LLM agents increasingly handle multi-step tool-calling workflows in customer service, healthcare, and technical support, real users are not uniformly cooperative—they express frustration, impatience, or confusion. Prior benchmarks like τ-Bench and τ-Trait have advanced agent evaluation but still model users as static or purely cooperative, creating a blind spot for deployment scenarios where emotional dynamics shape interaction quality. τ-Emotion-Bench fills this gap by formalizing emotional variation as a controlled experimental variable, making agent fragility measurable and actionable.

## Implications
For practitioners deploying LLM agents in customer-facing or collaborative settings, this research signals that current frontier models are not robust to emotionally varied users, and that training data must incorporate interaction-aware signals—such as user-initiated termination of unproductive exchanges—to build agents that balance autonomous tool execution with appropriate user engagement. For the broader AI research community, Tracer offers a reproducible, scalable pipeline for generating emotion-conditioned training data that generalizes across domains, suggesting a path toward more reliable agentic systems without requiring prohibitively expensive human annotation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19560v1)

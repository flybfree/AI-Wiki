---
title: Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery
url: http://arxiv.org/abs/2610.31461v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_15-55-18Z_AdaptiveSkillGranularityforCodingAgents_RuntimeRou.md
generated_at: 2026-10-22 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Adaptive Skill Granularity, a framework for coding agents that dynamically selects between primitive tool calls, macro skills, or hybrid execution paths based on task structure, execution state, and macro-skill failure signals. The authors demonstrate that fixed-granularity execution is efficient when applicable but brittle under task mismatch, while runtime routing combined with explicit macro-to-micro recovery significantly improves robustness and enables controlled recovery from macro failures that fixed-granularity approaches cannot resolve.

## Key Takeaways
- The framework treats skill granularity as an action-abstraction policy conditioned on three factors: task structure, execution state, and macro-skill failures. This reframes skill selection from a static retrieval problem into a dynamic runtime control problem, combining a feature-based granularity controller with a finite-state recovery executor to make execution-path decisions during agent operation rather than before execution begins.
- Fixed macro execution, while efficient when the macro skill matches the task, is brittle under mismatch conditions. The paper evaluates this using a deterministic coding-agent protocol with verifier-defined success metrics, total cost tracking, and process-level metrics including macro adoption rates, failure recovery rates, route match accuracy, and transition correctness, showing that runtime routing and explicit macro-to-micro recovery improve robustness and recover controlled macro failures that fixed-granularity execution leaves unresolved.
- The findings advocate that skill libraries for coding agents should be treated not merely as retrievable resources but as controllable, verifiable, and recoverable execution abstractions. This shifts the design philosophy of agent skill systems from passive retrieval-and-composition toward active runtime management with explicit fallback and recovery mechanisms.

## Context
This work addresses a critical gap in the growing field of LLM-based coding agents, where prior research has focused predominantly on how agents retrieve, compose, or synthesize skills before execution begins. The paper identifies that execution itself introduces an additional runtime control problem that existing skill frameworks do not adequately address, particularly the challenge of deciding at runtime whether to invoke primitive tool calls, composite macro skills, or hybrid strategies that begin with a macro and fall back to micro-level recovery. This positions the work at the intersection of agent planning, tool-use orchestration, and robust execution design.

## Implications
For practitioners building coding agents and autonomous software engineering systems, this framework suggests that production-grade agent architectures need runtime granularity controllers and explicit recovery state machines rather than static skill-selection pipelines. For the broader AI research community, the paper challenges the prevailing assumption that skill libraries are primarily retrieval problems, reframing them as controllable execution abstractions that require verification, fallback logic, and failure-aware routing. This has direct implications for industrial coding-agent products where reliability under task mismatch is a practical deployment concern rather than a theoretical edge case.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31461v1)

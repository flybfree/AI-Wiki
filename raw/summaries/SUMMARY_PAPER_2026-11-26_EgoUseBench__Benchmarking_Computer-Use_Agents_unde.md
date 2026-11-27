---
title: EgoUseBench: Benchmarking Computer-Use Agents under Evolving First-Person Contexts
url: http://arxiv.org/abs/2611.34466v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-25_14-36-38Z_EgoUseBench_BenchmarkingComputer_UseAgentsunderEvo.md
generated_at: 2026-11-26 21:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
EgoUseBench is a benchmark designed to evaluate computer-use agents under evolving first-person contexts, reflecting how AI wearables such as smart glasses can ground digital tasks in a user's physical surroundings. It constructs 693 tasks from over 74 hours of real-world first-person recordings across three settings: Computer-Use (explicit instructions), Offline Ego Use (prerecorded first-person context), and Online Ego Use (continuous observations as intent evolves). Evaluating advanced models, the authors find that average success rates in Online Ego Use are 26.3% lower than in Computer-Use, showing that keeping execution aligned with changing first-person context and user intent remains difficult.

## Key Takeaways
- The paper introduces the "Ego Use" paradigm, in which first-person observations from wearables let agents identify objects and activities relevant to user requests and ground digital tasks in the surrounding context, rather than relying solely on explicit instructions.
- EgoUseBench tracks first-person observations, user requirements, and website state separately, and groups tasks by how information changes during execution into three types: Graft (revised user requirements), Refresh (new first-person observations), and Clarify (agent-initiated information seeking).
- First-person evidence is limited by the wearer's viewpoint and can be incomplete or ambiguous, so agents must revise their understanding of physical context and intent and reassess whether prior digital actions remain valid; this is reflected in the 26.3% average success-rate drop in Online Ego Use relative to Computer-Use.

## Context
Computer-use agents are increasingly expected to act in digital environments, but most evaluation assumes stable, explicitly specified instructions. Wearable devices shift the interaction toward ongoing physical activity, where the agent must infer relevant objects and intent from first-person video rather than from a fixed prompt. This makes context tracking, revision, and reassessment central challenges that existing benchmarks do not adequately capture.

## Implications
The results suggest that current advanced models are not yet reliable when first-person context and user intent evolve during execution, which matters for wearable-assisted productivity, accessibility, and embodied assistants. Practitioners building Ego Use systems should prioritize robust context revision, state tracking, and agent-initiated information seeking rather than only improving single-shot task completion. EgoUseBench provides a reusable measurement framework for comparing agents across Computer-Use, Offline Ego Use, and Online Ego Use settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.34466v1)

---
title: ReFract: Benchmarking Perspective Awareness in Language Model Agents with Text World Models
url: http://arxiv.org/abs/2610.03356v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_14-21-26Z_ReFract_BenchmarkingPerspectiveAwarenessinLanguage.md
generated_at: 2026-10-04 21:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ReFract introduces a benchmark of 150 expert-validated tasks designed to evaluate whether LLM agents can adjust their actions and information provision based on the specific role of the user they are assisting, a capability the authors term "Perspective Awareness." The benchmark is grounded in anonymized domain support conversations from industrial maintenance and equipment fault troubleshooting settings, where agents must infer what a given role intends and act only through tools and knowledge boundaries legitimate for that role. State-of-the-art LLMs achieve at most 69% task success, with over half of their action trajectories containing perspective-violating actions, revealing this as a largely unsolved evaluation axis.

## Key Takeaways
- Perspective Awareness is defined as the agent's ability to infer what a specific user role intends and to act exclusively through tools and information channels that role may legitimately use, meaning the same query must elicit different agent responses depending on whether the user is, for example, a technician, a supervisor, or a safety officer. This goes beyond simple instruction-following and requires genuine role modeling.
- The benchmark entries are constructed using Text World Models that simulate the agent's operating environments and assemble perspective-aware action trajectories, grounded in anonymized queries from real domain support conversations. This grounding in expert-validated, real-world scenarios distinguishes ReFract from synthetic or abstract benchmarks and ensures ecological validity for high-stakes industrial settings.
- The consequences of failure are materially different from software coding tasks: agent responses are enacted on physical equipment, meaning perspective-violating actions can cause irreversible equipment damage, production loss, or personnel harm. This elevates the stakes of perspective awareness from a quality-of-service concern to a safety-critical requirement, and the finding that SOTA models exceed 50% perspective-violating trajectories underscores how far current systems fall short.

## Context
As LLM agents move from chat interfaces into embodied or tool-augmented deployments in industrial, medical, and operational settings, the assumption that a single "best" response suffices for all users breaks down. Existing agent benchmarks such as SWE-bench, ToolBench, or WebArena evaluate task completion but treat the user as a homogeneous entity, ignoring the organizational and role-based structure of real workplaces. ReFract fills this gap by formalizing perspective awareness as a measurable, distinct axis of agent evaluation, complementing the growing literature on role-play, persona modeling, and situated dialogue in NLP.

## Implications
For industry practitioners deploying LLM agents in maintenance, manufacturing, or field-service operations, ReFract signals that current models cannot yet be trusted to tailor their actions to the knowledge and authority boundaries of different workers, creating real safety and liability risks when agents recommend or execute actions beyond a user's legitimate scope. For the AI research community, the benchmark motivates a shift from optimizing "how to act" toward calibrating "for whom to act," potentially driving new training objectives, role-conditioned tool-use policies, and evaluation frameworks that treat perspective awareness as a first-class capability rather than an afterthought.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03356v1)

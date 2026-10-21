---
title: Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization
url: http://arxiv.org/abs/2610.27889v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_09-11-39Z_ElicitationorExpansion_DemystifyingGainsfromAgentH.md
generated_at: 2026-10-20 21:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether performance gains from agent harness optimization represent "elicitation" (improved reliability on tasks already within a model's capability) or "expansion" (genuinely broadening the range of solvable tasks). Using pass@k analysis borrowed from reinforcement learning literature, the authors systematically compare optimized harnesses against their pre-optimization counterparts across static prediction and dynamic tasks, finding that apparent pass@1 advantages can reverse at larger attempt budgets and that aggregate gains often conceal shortfalls on harder tasks.

## Key Takeaways
- The distinction between elicitation and expansion is critical for recursive self-improvement and evolutionary search pipelines: expansion provides a broader range of successful experiences that can push capability boundaries, whereas elicitation merely improves reliability on already-achievable tasks. Naïve success rate metrics fail to capture this distinction, making them inadequate for guiding harness optimization research.
- The authors apply pass@k methodology from RL training comparisons to harness optimization, assessing changes in reachable task coverage, comparing harness optimization against model scaling and increased inference-time compute, and examining how gains vary with task difficulty. This fine-grained diagnostic framework reveals that harness optimization gains are not uniformly distributed across task difficulty levels.
- A key empirical finding is that pass@1 advantages of an optimized harness over stronger interventions (such as model scaling or additional compute) can reverse at larger attempt budgets, meaning that harness optimization may not provide a fundamentally broader capability envelope but rather a more efficient path to tasks the model could already solve. Aggregate performance gains can mask significant shortfalls on hard tasks, underscoring the need for granular, difficulty-stratified evaluation rather than headline success rates.

## Context
This work sits at the intersection of agentic AI systems, harness engineering, and capability evaluation. As the field moves toward recursive self-improvement loops where agents iteratively refine their own scaffolding, understanding whether harness gains genuinely expand the frontier or merely exploit existing potential becomes a foundational question. The paper draws on established pass@k evaluation frameworks from RL post-training literature and transplants them into the harness optimization domain, providing a methodological bridge that the community currently lacks.

## Implications
For practitioners building agent systems, this research warns against over-relying on aggregate benchmark improvements when tuning harnesses, as such metrics can obscure whether a system is truly gaining new capabilities or simply becoming more consistent on known tasks. For researchers pursuing self-improving agent architectures, the elicitation-versus-expansion distinction determines whether harness optimization can serve as a genuine capability-advancing mechanism or merely a reliability booster, directly shaping how resources should be allocated between harness engineering, model scaling, and inference-time compute strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27889v1)

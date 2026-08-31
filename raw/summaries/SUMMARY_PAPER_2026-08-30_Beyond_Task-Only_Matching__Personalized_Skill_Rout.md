---
title: Beyond Task-Only Matching: Personalized Skill Routing with Counterfactual Evaluation
url: http://arxiv.org/abs/2608.28241v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_11-55-56Z_BeyondTask_OnlyMatching_PersonalizedSkillRoutingwi.md
generated_at: 2026-08-30 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces personalized skill routing for large language model agents, moving beyond task‑only semantic matching to jointly consider user profiles. The authors present a profile‑counterfactual benchmark and a progressive retrieve‑and‑rerank framework called SkillFeed that improves retrieval accuracy by 75.1 % top‑1 on their test set, with an additional 35.1‑point gain when user profiles change the reference skill.

## Key Takeaways
- Task‑only routers can select skills that are semantically plausible yet unsuitable for a user’s specific constraints, conflating task relevance with skill suitability.
- The profile‑counterfactual benchmark isolates how variations in user profiles alter which skill is appropriate for a given task.
- SkillFeed leverages body‑level evidence to rerank candidates that conflict with the user profile, delivering substantial accuracy improvements.

## Context
Large language model agents increasingly rely on reusable skill repositories to fulfill user requests. Existing routing methods treat relevance solely through task semantics, ignoring individual user profiles and leading to mismatched recommendations. This work advances retrieval by conditioning it on both task and user attributes, reflecting a broader trend toward personalized AI systems that adapt to diverse contexts.

## Implications
Accurate skill routing enhances the reliability of LLM agents in real‑world applications such as tutoring platforms and customer support bots, reducing user frustration from unsuitable recommendations. For industry practitioners, integrating profile‑conditioned routing can improve engagement metrics and operational efficiency by ensuring skills align with both task demands and individual constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28241v1)

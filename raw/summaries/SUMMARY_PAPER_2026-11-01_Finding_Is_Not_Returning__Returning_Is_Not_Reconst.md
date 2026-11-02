---
title: Finding Is Not Returning, Returning Is Not Reconstructing: A Multi-Dimensional Evaluation of Agent Social Re-entry
url: http://arxiv.org/abs/2610.39781v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-29_10-31-18Z_FindingIsNotReturning_ReturningIsNotReconstructing.md
generated_at: 2026-11-01 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a novel multi-dimensional evaluation framework for assessing whether LLM agents can autonomously re-engage with previously inactive conversations in persistent social environments. The authors decompose "agent social re-entry" into three distinct capabilities—Finding (identifying a past conversation), Returning (deciding to re-engage), and Reconstructing (maintaining conversational continuity)—and demonstrate through evaluations across six LLM configurations that improving one dimension does not guarantee improvement in the others, revealing a critical gap in current agent architectures.

## Key Takeaways
- The paper establishes that remembering a past interaction is fundamentally different from being able to identify when to revisit it, decide to return to it, or reconstruct the context needed for coherent continuation. These three capabilities—Finding, Returning, and Reconstructing—are treated as complementary but independent dimensions, challenging the common assumption that memory retrieval alone suffices for social re-engagement.
- Evaluations across six LLM configurations reveal that resurfacing mechanisms substantially improve target conversation identification (Finding), and persistent memory is associated with higher rates of autonomous target-directed replying (Returning). However, neither improvement translates into consistent gains in contextual reconstruction (Reconstructing), exposing a persistent weakness in maintaining conversational continuity across time gaps.
- The authors develop a shared-snapshot evaluation framework that measures these three dimensions independently, providing a methodological contribution that allows researchers to diagnose which specific capability is failing rather than conflating memory retrieval performance with overall conversational quality.

## Context
As LLM agents are increasingly deployed in persistent social environments such as long-running group chats, collaborative workspaces, and multi-session interactions, the ability to re-engage with dormant conversations becomes a practical necessity rather than a theoretical curiosity. Existing research has heavily focused on long-term memory architectures and conversational context retrieval, but these approaches implicitly assume that retrieving a past conversation is equivalent to being able to use it socially. This paper addresses a critical blind spot by formalizing the gap between retrieval and genuine social re-engagement, contributing to the growing field of agent evaluation and benchmarking.

## Implications
For practitioners building agent systems intended for sustained social interaction, this work signals that current memory and retrieval improvements are insufficient for producing coherent, contextually aware re-engagement with past conversations. Industry developers deploying agents in collaborative or community settings should not assume that stronger retrieval pipelines will automatically yield socially competent agents. The shared-snapshot evaluation framework offers a diagnostic tool that can guide targeted architectural improvements in each dimension of social re-entry, helping the field move beyond single-metric evaluations toward more holistic assessments of agent social competence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.39781v1)

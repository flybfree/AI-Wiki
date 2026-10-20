---
title: When Should AI Chime In? Benchmarking Timely Contribution of Proactive Agents in Multi-Party Chat
url: http://arxiv.org/abs/2610.25896v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_06-54-04Z_WhenShouldAIChimeIn_BenchmarkingTimelyContribution.md
generated_at: 2026-10-19 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PITCH (Proactive Intervention Timing in CHat), the first benchmark designed to evaluate when AI agents should proactively contribute information in multi-party conversations, isolating the timing question from content relevance. The authors collected 1,091 human judgments across 35 unscripted conversations involving 89 participants, then evaluated 15 models across 28 configurations. The central finding is that while models can place contributions accurately when given full conversation history, they systematically intervene too early when making decisions live as conversations unfold, with best-turn accuracy collapsing from 57.8% to 19.0% and nearly half of placements occurring before every participant's acceptable window.

## Key Takeaways
- The PITCH benchmark represents a novel methodological contribution: participants in synchronous multi-party chats (2-4 people) author candidate AI contribution messages, place them into chat history, and deliberate as a group about optimal placement. This yields 384 candidate contributions and 1,091 judgments, each specifying an ideal turn, an acceptable window, or a determination that the contribution should not appear at all, providing a human-grounded evaluation framework previously absent from the field.
- Models exhibit a severe timing failure in live settings: when asked to decide in real time as conversations unfold rather than retrospectively, best-turn accuracy drops from 57.8% to 19.0%, and 46.4% of model placements occur before every participant's acceptable window. Lay humans deciding live outperform models (23.7% vs. 19.0% accuracy) and produce fewer premature placements (39.7% vs. 46.4%), suggesting that human social intuition about conversational timing remains superior to current model reasoning.
- Analysis of model reasoning traces reveals a fundamental blind spot: 93% of intervention justifications cite relevance as the sole criterion for chiming in, while almost none consider the value of waiting. This indicates that current models lack any explicit reasoning about conversational pacing, turn-taking dynamics, or the social cost of interruption, treating timing as an afterthought rather than a core decision variable.

## Context
As AI agents increasingly participate in group settings such as meetings, classrooms, and collaborative workspaces, the question of when to speak has become as critical as what to say. Existing research on proactive agents has focused primarily on content generation and relevance detection, leaving timing as an underexplored dimension. PITCH fills this gap by providing the first large-scale, human-grounded benchmark specifically targeting intervention timing in unscripted multi-party conversations, enabling rigorous evaluation of whether agents can integrate socially rather than merely informationally.

## Implications
For practitioners building group-collaboration AI tools, these findings signal that current models are not yet ready to participate in live human conversations without causing disruption, as their tendency to intervene prematurely undermines trust and usability. The benchmark provides a concrete evaluation target for developers to train and test timing-aware reasoning, and the finding that models almost never reason about waiting suggests that explicit timing modules, social-awareness training, or deliberation frameworks that model conversational pacing are necessary next steps. For the broader field, PITCH establishes evaluation standards that could shift proactive-agent research from optimizing what to say toward optimizing when and whether to say it.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25896v1)

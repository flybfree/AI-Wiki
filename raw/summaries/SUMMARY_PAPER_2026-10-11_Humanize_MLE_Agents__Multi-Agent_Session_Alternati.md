---
title: Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits
url: http://arxiv.org/abs/2610.13494v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_12-26-34Z_HumanizeMLEAgents_Multi_AgentSessionAlternationBey.md
generated_at: 2026-10-11 20:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies two fundamental failure modes in single-agent LLM-based approaches to long-horizon machine learning engineering tasks: "long-horizon deceleration," where reasoning quality degrades as sessions lengthen, and "harness staleness," where custom scaffolding loses its advantage as underlying models improve. To overcome these limits, the authors propose Humanize MLE Agents (HMA), a multi-agent framework that alternates two agents on a shared workspace with bounded session lengths and context resets between sessions, achieving a state-of-the-art 78.2% any-medal rate on 75 Kaggle tasks in MLE-bench while using only a quarter of the time budget of the strongest open-source baseline.

## Key Takeaways
- The authors formalize multi-agent session alternation as a context-reset semi-Markov decision process (CR-SMDP), deriving sufficient conditions under which alternating agents can exceed single-agent performance limits, an explicit experiment-budget bound, and conditions under which session caps preserve the alternation advantage. This theoretical grounding distinguishes the work from purely empirical multi-agent systems.
- HMA operates without task-specific harnesses, skills, or prior knowledge supplements, relying solely on the alternation mechanism itself. Across six configurations spanning five heterogeneous agent pairs, HMA improves any-medal rate over constituent baselines by 6.4 points on average, demonstrating that the benefit is a property of the workflow structure rather than a specific model pairing.
- The approach generalizes beyond MLE: a supplementary case on kernel optimization reaches 878 cycles, within 1.6% of the community leaderboard leader, showing the session-alternation paradigm transfers to other long-horizon optimization tasks.

## Context
As LLM agents are increasingly deployed for complex, multi-step engineering tasks such as Kaggle competitions and kernel optimization, practitioners rely heavily on context engineering through custom harnesses that manage tools, accumulated experience, and skills. This paper challenges the prevailing assumption that ever-longer single-agent sessions with richer scaffolding are the path to better performance. By demonstrating that both reasoning quality and harness utility degrade predictably over extended sessions, the work shifts attention from improving single-agent capacity toward designing multi-agent workflows that exploit structural resets and collaborative alternation, a direction that aligns with broader trends in multi-agent systems research but is grounded here in formal decision-theoretic analysis.

## Implications
For practitioners building MLE automation pipelines, HMA suggests that investing in workflow-level agent orchestration—specifically bounded sessions, context resets, and alternating agent roles—can yield substantial performance gains at a fraction of the compute cost compared to scaling single-agent sessions or building elaborate custom harnesses. For the broader AI research community, the CR-SMDP framework and the identification of harness staleness provide a principled lens for evaluating when multi-agent coordination is theoretically justified versus when it is merely a workaround for model limitations, guiding future system design toward architectures that remain robust as underlying models improve.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13494v1)

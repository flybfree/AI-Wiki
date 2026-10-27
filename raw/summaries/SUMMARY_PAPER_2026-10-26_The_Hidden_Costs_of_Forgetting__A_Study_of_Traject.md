---
title: The Hidden Costs of Forgetting: A Study of Trajectory Deletion in Software Engineering Agents
url: http://arxiv.org/abs/2610.35496v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-26_14-25-17Z_TheHiddenCostsofForgetting_AStudyofTrajectoryDelet.md
generated_at: 2026-10-26 23:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents an empirical study examining the hidden costs and behavioral consequences of trajectory deletion in software engineering agents that interact with LLMs. Through 42 trajectory-reduction configurations across 9,400 runs on SWE-bench Verified, the authors demonstrate that while aggressive deletion of reasoning text can preserve task effectiveness, agents compensate by re-fetching deleted content, and the actual cost savings depend critically on the pricing model used—under caching-aware pricing, trajectory reduction yields zero cost savings because it breaks cached prefixes billed at lower rates.

## Key Takeaways
- Deleting up to 100% of reasoning text from old turns can preserve overall agent effectiveness, but only when deletion is applied with a delay; immediate deletion significantly degrades performance. This finding challenges the assumption that aggressive token reduction is universally safe and highlights that timing of deletion is as important as the amount deleted.
- Agents compensate for deleted trajectory content by re-fetching it, which increases both the number of interaction turns and the total input/output tokens consumed. This behavioral compensation means that end-to-end effectiveness metrics can mask underlying inefficiencies, making trajectory-level analysis essential for understanding true agent behavior.
- Under a flat pricing model, 26 of 42 evaluations showed reduced costs, but under a caching-aware pricing model, zero evaluations yielded lower costs because reducing the trajectory destroys the cached prefix that LLM providers bill at a discounted rate. This reveals that token-count-based cost estimation is fundamentally misleading and that realistic pricing models must be incorporated into any trajectory reduction strategy.

## Context
Software engineering agents such as those evaluated on SWE-bench Verified operate by resending their entire interaction trajectory to an LLM at every turn, creating a growing context window that drives up inference costs. Prior work suggested that random deletion of 75% of tokens in old turns could preserve effectiveness, but the mechanisms behind this resilience and its true cost implications remained unexplored. This paper fills that gap by systematically varying deletion scope, granularity, amount, and timing across two state-of-the-art agents, providing the first comprehensive empirical account of how agents behave when their memory is pruned.

## Implications
For practitioners deploying LLM-based coding agents in production, this work demonstrates that naive token-reduction strategies can backfire under realistic caching-aware pricing models, potentially increasing costs rather than reducing them. Industry teams must move beyond token-count metrics and adopt pricing-model-aware evaluation when designing memory management policies for agent systems. The findings also motivate future research into smarter memory management techniques that reduce costs without triggering costly re-fetching behavior, a critical open problem as agentic software engineering systems scale in complexity and usage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35496v1)

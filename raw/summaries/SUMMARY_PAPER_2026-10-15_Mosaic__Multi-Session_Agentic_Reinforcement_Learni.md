---
title: Mosaic: Multi-Session Agentic Reinforcement Learning
url: http://arxiv.org/abs/2610.22174v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_16-32-44Z_Mosaic_Multi_SessionAgenticReinforcementLearning.md
generated_at: 2026-10-15 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces Mosaic, a multi-session agentic reinforcement learning method that addresses the mismatch between single-session training assumptions and multi-session inference-time execution in agentic systems. Mosaic employs critic-free hierarchical optimization to estimate session-level contributions within trajectories, outperforming naive advantage broadcasting on BrowseComp benchmarks with Qwen3.5-4B while using fewer sessions on average.

## Key Takeaways
- Existing agentic RL methods assume single-session trajectories where all interactions occur within one continuously accumulated context, but practical agentic techniques like context compaction and subagent forking naturally produce trajectories spanning multiple sessions, creating a fundamental training-inference mismatch that Mosaic explicitly addresses by supporting an arbitrary number of sessions within a single trajectory.
- The widely adopted baseline approach of broadcasting trajectory-level advantages uniformly to all sessions fails to distinguish the contributions of individual sessions and provides no guidance for session allocation within trajectories, motivating Mosaic's hierarchical optimization that incorporates session-usage signals into advantage estimation at the trajectory level and shapes each session's advantage according to its estimated marginal contribution at the session level.
- Experiments demonstrate that Mosaic achieves superior performance over advantage broadcasting in both context compaction and subagent forking scenarios while simultaneously reducing the average number of sessions used, with further analyses confirming improvements in session utility and allocation efficiency, which the authors identify as a promising target for future multi-session agentic RL research.

## Context
Agentic reinforcement learning has become a central paradigm for training language models to perform complex multi-step reasoning and tool-use tasks, yet the field has largely operated under the simplifying assumption that agent trajectories unfold within a single continuous context window. As practical agentic systems increasingly rely on techniques such as context compaction to manage long interactions and subagent forking to parallelize reasoning, the gap between training assumptions and deployment realities has become a critical bottleneck that this paper directly confronts.

## Implications
For practitioners building agentic systems in production, Mosaic offers a principled method for training agents that naturally operate across multiple sessions, potentially reducing computational costs by encouraging more efficient session allocation rather than wasteful session proliferation. The identification of session utility and allocation as optimization targets opens a new research direction for the broader agentic RL community, suggesting that future advances should move beyond single-session paradigms to accommodate the heterogeneous, multi-session architectures that real-world agent deployments increasingly require.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22174v1)

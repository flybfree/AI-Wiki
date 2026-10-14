---
title: TurnCost: Turns, Not Observations: Cache-Aware Loop Engineering for Coding Agents
url: http://arxiv.org/abs/2610.15093v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_18-03-24Z_TurnCost_Turns_NotObservations_Cache_AwareLoopEngi.md
generated_at: 2026-10-13 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper challenges the prevailing assumption that compressing tool observations or routing turns to cheaper models is the primary lever for reducing coding-agent costs. By analyzing 600 publicly released coding-agent trajectories across two agent scaffolds and two language models, the authors demonstrate that turn count—not observation size—is the dominant driver of trajectory cost, explaining 84% of variance compared to just 4% for mean observation size. They introduce TurnCost, a tool for re-scoring trajectory corpora under alternative caching, pricing, compression, and routing policies, and derive a closed-form break-even condition for model delegation that empirically validates when delegation increases rather than reduces cost.

## Key Takeaways
- Median tool observations in coding-agent trajectories contain only 118–286 tokens, while the large build logs commonly cited to motivate compression strategies occur near the ninety-ninth percentile. This means the practical opportunity for observation-compression optimizations is far smaller than the literature suggests, and the most expensive trajectories paradoxically have the smallest observations but the most turns.
- Under near-ideal prefix caching, 98.6% of input tokens are served from cache, meaning flat input pricing overestimates actual loop cost by roughly 7x on average. This fundamentally undermines cost models that treat every turn's input tokens as freshly priced, and it shifts the economic analysis toward turn count as the true cost driver.
- The authors derive and empirically validate a closed-form break-even condition for model delegation, finding that delegation to cheaper models increases cost in half of the evaluated settings, landing near the predicted boundary. Turn count explains 84% of the variance in log trajectory cost versus 4% for mean observation size, identifying unnecessary turns as the larger and largely unexamined optimization opportunity, though the authors explicitly note they do not establish that turns can be removed while holding task success fixed.

## Context
The field of AI coding agents has invested heavily in observation compression, context management, and model routing as efficiency strategies, largely motivated by anecdotal examples of enormous build logs and tool outputs. This paper provides the first systematic empirical analysis of actual trajectory distributions across multiple agent scaffolds and models, revealing that the cost structure assumed by prior work is substantially distorted by prefix caching and that the true bottleneck is loop iteration count rather than per-turn payload size. It reframes "loop engineering" as a discipline where turn minimization, not observation compression, should be the primary optimization target.

## Implications
For practitioners building coding-agent pipelines, this work suggests that investment in aggressive observation compression or cheap-model delegation may yield diminishing or even negative returns, while efforts to reduce unnecessary agent turns—through better planning, early termination, or smarter tool-use policies—represent a far larger and underexplored cost-saving opportunity. For the broader AI research community, the release of TurnCost as a re-scoring tool enables rigorous, cache-aware evaluation of agent efficiency policies, potentially reshaping benchmarking standards and cost accounting for agentic systems. The finding that 98.6% of tokens hit prefix cache also has direct implications for API providers and infrastructure teams designing pricing and caching strategies for agentic workloads.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15093v1)

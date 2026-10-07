---
title: ReFold: Training-Free Reversible Inter-Turn Context Folding for Long-Horizon Agents
url: http://arxiv.org/abs/2610.07863v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_07-09-54Z_ReFold_Training_FreeReversibleInter_TurnContextFol.md
generated_at: 2026-10-06 21:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ReFold addresses the growing context and cost problem in long-horizon LLM agents by introducing a training-free rendering layer that compresses only the model’s rendered context while preserving the full interaction history. It removes inter-turn redundancy through reversible stubbing and folding, reducing token consumption, KV-cache memory, forced compactions, and serving delays without requiring auxiliary predictors or permanent content loss.

## Key Takeaways
- ReFold compresses the model’s rendered context rather than the underlying interaction history, allowing long-horizon agents to remain within context limits while retaining the ability to restore removed content when needed. This reversibility is important because predictive context management methods often permanently discard information, which can harm later reasoning or recovery.
- The method removes two specific forms of inter-turn redundancy: content that an earlier turn already displayed, which is replaced by a stub, and turns that the agent itself reports as finished, which are folded into a one-line note. These operators target redundant context that accumulates in append-only agent histories, especially in ReAct-style workflows where prior observations and completed steps are repeatedly re-sent.
- ReFold uses chunked rendering and rewrites the cached prefix only every few steps instead of at every step, helping preserve prefix-cache efficiency while reducing runtime overhead. Across five long-horizon benchmarks and two frontier LLMs, it reduces token consumption by up to 2.5x, halves KV-cache memory per session, avoids up to 92% of forced compactions under capped context budgets, reduces request queuing delays by up to 100%, accelerates inference by up to 1.7x, and cuts inference costs by up to 3.4x.

## Context
Long-horizon agents are increasingly used for multi-step reasoning, tool use, and interactive task completion, but their append-only interaction histories create a fundamental scaling bottleneck. As each step is re-sent to the model, context length, memory usage, latency, and inference cost grow with the number of steps, often forcing truncation, summarization, or compaction that can degrade performance. ReFold matters because it reframes context management as a reversible rendering problem rather than a lossy prediction problem, which is especially relevant for agentic systems that need both long-term memory and efficient serving.

## Implications
For practitioners, ReFold offers a practical way to improve long-horizon agent efficiency without retraining models or adding auxiliary prediction components. Its plug-and-play rendering-layer design makes it attractive for existing ReAct-style harnesses, production agent frameworks, and serving systems where context budgets, KV-cache pressure, and queue delays directly affect cost and responsiveness. More broadly, the work suggests that reversible context compression can be a safer and more scalable alternative to permanent context pruning, enabling longer agent sessions while preserving recoverability and task reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07863v1)

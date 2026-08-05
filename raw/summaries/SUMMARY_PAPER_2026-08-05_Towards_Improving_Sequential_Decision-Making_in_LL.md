---
title: Towards Improving Sequential Decision-Making in LLM Agents via Experience Memory
url: http://arxiv.org/abs/2608.03420v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_10-12-12Z_TowardsImprovingSequentialDecision_MakinginLLMAgen.md
generated_at: 2026-08-05 01:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why large language models underperform in sequential decision-making tasks despite excelling at single-shot reasoning, using fully observable two-player zero‑sum games as a benchmark. It demonstrates that LLMs often play suboptimally on simple games like tic‑tac‑toe and are outperformed by model‑based methods such as MCTS. The authors introduce an experience memory component that enables post-game reflection and rule extraction, improving performance without altering the model weights.

## Key Takeaways
- LLMs exhibit poor sequential decision-making in zero-sum games because their training does not capture credit assignment across turns.
- Adding an experience memory that stores past game states allows the agent to reflect on outcomes and extract actionable rules, leading to measurable gains on tic-tac-toe.
- The improvement occurs without fine‑tuning or modifying the underlying model weights, indicating a lightweight adaptation strategy.

## Context
Sequential decision-making remains a bottleneck for LLM agents because their autoregressive nature does not naturally handle long-term planning. Traditional reinforcement learning approaches require large datasets and may conflict with language modeling objectives. This work highlights a gap between single-shot reasoning capabilities and the need for sustained, optimal behavior over multiple steps.

## Implications
For practitioners developing autonomous AI assistants, integrating experience memory can enable more reliable task execution across multi-step workflows. The approach offers a modular upgrade that preserves model integrity while enhancing utility, suggesting a path toward scalable sequential agents without extensive retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03420v1)

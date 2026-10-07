---
title: Stateless Language Agents: Scaling Long-Horizon Automated Research
url: http://arxiv.org/abs/2610.07625v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_02-17-32Z_StatelessLanguageAgents_ScalingLong_HorizonAutomat.md
generated_at: 2026-10-06 21:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Stateless Language Agents (SLAs), a framework for long-horizon automated research in which durable research state is stored outside agent conversations and each agent invocation receives a fresh, role-specific context. The authors evaluate SLA against three recent frameworks on software engineering, kernel optimization, and algorithm design at budgets of up to one billion tokens, finding that SLA achieves the best final result on every task and reaches the strongest kernel baseline’s final performance with over 84% fewer tokens.

## Key Takeaways
- The paper identifies two central failure modes in long-running LLM research agents: agents replaying increasingly large conversation histories and duplicating work across parallel agents, which can cause continued token consumption without meaningful experimental progress. It argues that these failures arise from where research state is stored and who decides the next experiments.
- SLA separates stateful search from stateless agents: the harness maintains candidate solutions and measured outcomes, while agents do not carry their own conversations across invocations. This makes what each agent sees an explicit design choice, allowing the system to reconstruct concise, role-specific contexts instead of accumulating unbounded history.
- The SLA framework uses a stateless Advisor that reads harness-summarized evidence across search directions and assigns concrete experiments to parallel Workers. Ablations show that focused contexts and explicit assignments each contribute to progress, can compound over full runs, and the Advisor consumes less than 0.6% of tokens, suggesting that lightweight coordination can improve efficiency and reliability.

## Context
Automated research increasingly depends on language agents that plan, experiment, and iterate over long horizons, but many evaluations use short budgets or benchmarks that saturate early. This paper matters because it examines failure modes that appear only when systems run for many tokens and many invocations, where memory, coordination, and search direction become bottlenecks. It contributes a design principle for scalable agent systems: keep durable state outside conversations and make context construction a first-class architectural decision.

## Implications
For researchers and practitioners building autonomous coding, optimization, or scientific discovery systems, SLA suggests that simply increasing inference budgets is not enough; effective scaling requires explicit state management and assignment of next experiments. The approach may reduce token costs, improve parallel coordination, and make long-horizon agent systems more auditable and controllable. It also warns that short evaluation horizons can mislead developers about which components truly matter in production-scale research agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07625v1)

---
title: Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core
url: http://arxiv.org/abs/2610.30557v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_00-22-47Z_GovernedSelf_EvolutionforAutonomousInvesting_AMult.md
generated_at: 2026-10-22 22:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Steward, a multi-agent LLM system designed for autonomous investing that enforces a strict boundary on self-evolution through its type system and an invariant core of risk rules and order arithmetic. The system combines nine role-specialised agents, a seven-layer shared memory, and a governed self-improvement loop, and demonstrates in a five-month live deployment that it can contain a 24.6% sector drawdown to just a 0.3% loss while outperforming a single-model baseline in controlled replay experiments.

## Key Takeaways
- The system architecture separates decision-making across nine specialised agents: four analysts process news feeds, SEC filings, macroeconomic series, and market data to emit typed reports, a Portfolio Manager sets target positions, and a protected Risk Manager audits those positions. This role separation is enforced at the type-system level, meaning the boundary of what each agent can do is hard-coded rather than learned, preventing any agent from drifting into another's domain through self-evolution.
- Self-improvement is tightly governed through a three-stage review pipeline: code grades every trade and forecast nightly and writes results into shared memory; each quarter a reflector agent proposes prompt learnings; and a deterministic gate applies those learnings reversibly, with replay of recorded inputs verifying that the change actually improves outcomes. Crucially, an invariant core of order arithmetic, risk rules, and discipline-agent prompts is unreachable by any self-edit, ensuring that safety constraints cannot be overwritten by the system's own learning process.
- Empirical validation spans three independent experiments: a live five-month deployment (102 trading days, 1,632 LLM calls) that contained a 24.6% sector drawdown to 0.3%; a replay experiment where a single model given identical raw data traded more aggressively and lost 1.35 points against the market over five days while the joint design showed no significant loss and ignored injected instructions; and a 2015–2026 backtest showing the invariant core alone reduced maximum drawdown under all 50 random entry policies. The reflector successfully traced the dominant failure mode to its root cause and the gate applied a corrective learning that the agent adopted on trigger evenings but not on control evenings, demonstrating controlled, verifiable self-modification.

## Context
Autonomous LLM agents operating on live, untrusted web data face a fundamental tension: they must learn and adapt from outcomes to improve performance, yet they must not weaken their own safety guardrails in the process. In high-stakes domains like investing, where every trade is irreversible, this tension is especially acute. Steward addresses this by formalising the boundary of self-evolution in the system's type system and by making the improvement loop auditable through deterministic gates and replay verification. This positions the work at the intersection of multi-agent AI, governed self-improvement, and financial decision-making, offering a concrete architectural template for how LLM systems can evolve without eroding their invariants.

## Implications
For practitioners building autonomous trading or decision-support systems, Steward demonstrates that hard-coded invariants and role-specialised agent boundaries can materially reduce catastrophic risk, as evidenced by the backtest showing the core alone lowering maximum drawdown across all tested entry policies. For the broader AI safety and alignment community, the paper provides a working blueprint for governed self-evolution: a deterministic gate, reversible edits, and replay-based verification that together allow a system to learn from its own mistakes without the possibility of self-modification overriding its foundational constraints. This pattern is directly transferable to any domain where LLM agents must act irreversibly on noisy, adversarial inputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30557v1)

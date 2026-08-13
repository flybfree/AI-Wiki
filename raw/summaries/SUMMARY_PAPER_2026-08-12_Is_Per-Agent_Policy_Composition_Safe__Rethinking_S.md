---
title: Is Per-Agent Policy Composition Safe? Rethinking Successor-Feature Transfer in Cooperative Multi-Agent Reinforcement Learning
url: http://arxiv.org/abs/2608.11658v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_04-56-52Z_IsPer_AgentPolicyCompositionSafe_RethinkingSuccess.md
generated_at: 2026-08-12 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether composing policies from a shared library of learned successors is safe when multiple agents act together in reinforcement learning. It proves that letting each agent recombine its own policy independently can lead to joint behavior that is strictly worse than any individual policy, because the environment each agent experiences changes and invalidates its values. The authors identify synchronized composition as the only unconditionally safe fixed rule but note it cannot serve different goals to different agents, prompting a new hierarchical method called MA-USFA.

## Key Takeaways
- Independent recombining of agents' successor libraries can produce joint behavior that is strictly worse than any policy in the library because each agent's environment changes and its learned values become invalid.  
- The only unconditionally safe fixed rule is synchronized composition, which moves the whole team to one jointly trained policy but cannot assign distinct goals to individual agents.  
- MA-USFA introduces a two‑layer hierarchical approach: a lower layer of universal successor feature approximators predicts each agent's successors conditioned on teammates' objectives, and an upper composer selects library entries while providing cross‑agent corrections that per‑agent values cannot represent.

## Context
Multi‑agent reinforcement learning faces the challenge of coordinating diverse agents that must adapt to changing objectives without costly retraining. Existing composition techniques lack formal guarantees, leading to unpredictable or unsafe joint behavior in real‑world deployments such as fleet management and traffic control. This work addresses those gaps by providing a safety‑preserving framework.

## Implications
For practitioners, the paper offers a method that ensures safe policy composition while allowing heterogeneous goals across agents, reducing reliance on per‑task retraining. In industry, this translates to more reliable autonomous systems where multiple agents must operate under evolving objectives without compromising performance or safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11658v1)

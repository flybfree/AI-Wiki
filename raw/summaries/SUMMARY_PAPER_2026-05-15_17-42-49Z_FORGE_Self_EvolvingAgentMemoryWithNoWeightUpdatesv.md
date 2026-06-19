---

title: "Summary: FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast"
url: http://arxiv.org/abs/2605.16233v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-15_17-42-49Z_FORGE_Self_EvolvingAgentMemoryWithNoWeightUpdatesv.md
generated_at: "2026-06-11 10:41"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces FORGE, a population-based protocol that lets ReAct agents evolve natural-language memory through reflection without gradient updates. On the stochastic CAGE-2 task it boosts average returns by 1.7–7.7× over zero‑shot baselines and reduces major failures to about 1%.

## Key Takeaways
- Population broadcast is essential for performance gains, as shown by a no‑graduation ablation that proves broadcast alone drives improvement while graduation mainly saves compute.
- Few‑shot examples yield the highest returns for three of four LLM families, whereas rules provide better cost‑reliability with roughly 40% fewer tokens.
- Weak baseline models improve disproportionately, indicating FORGE may close capability gaps rather than amplify strong ones.

## Context
LLM agents face a challenge: improving memory and decision‑making without costly fine‑tuning. This work offers a scalable, gradient‑free method that can be applied across diverse model families, highlighting the potential of population learning in reinforcement settings.

## Implications
FORGE could enable more robust AI systems by leveraging collective knowledge sharing instead of individual updates, reducing training costs and mitigating failure rates. Practitioners may adopt this protocol to enhance agent reliability in resource‑constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.16233v1)

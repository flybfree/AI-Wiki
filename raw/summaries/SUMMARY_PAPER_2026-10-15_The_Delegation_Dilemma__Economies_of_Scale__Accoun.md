---
title: The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance
url: http://arxiv.org/abs/2610.21746v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_12-04-16Z_TheDelegationDilemma_EconomiesofScale_Accountabili.md
generated_at: 2026-10-15 23:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the fundamental tension between economies of scale and individual accountability in collective-action systems where agents voluntarily delegate decision-making authority to representative centers. Through a reduced-form repeated game model with endogenous delegation, the authors demonstrate that larger constituencies provide cost-sharing benefits but simultaneously weaken individual leverage over representatives, creating an endogenous limit on accountable constituency size. Simulations using large language model agents reveal that polycentric governance structures naturally emerge but remain unstable, cycling through concentration, exploitation, exit, and re-formation.

## Key Takeaways
- The paper establishes a scale-accountability tradeoff: while larger groups reduce per-member organizational costs through shared infrastructure, the marginal value a representative center places on retaining any single constituent diminishes as group size grows. This creates an endogenous "accountable constituency size" beyond which the credible threat of individual exit no longer constrains exploitative behavior by representatives, effectively breaking the accountability mechanism that sustains non-exploitative delegation.
- The authors identify specific parameter regions where fully delegated yet accountable governance, when it is feasible at all, must necessarily be polycentric rather than monocentric. This means that no single center can simultaneously achieve cost efficiency and maintain accountability to all constituents, forcing the emergence of multiple competing governance structures as a structural necessity rather than a design choice.
- LLM agent simulations across five matched pairs of 30-agent scenarios show that polycentric structures repeatedly self-organize but exhibit fluid dynamics characterized by recurring cycles of concentration, exploitation, constituent exit, and institutional re-formation. Notably, models of different capacity display similar willingness to assume leadership roles but diverge substantially in how they exercise authority, with one model (Sol) initiating exploitation more frequently than another (Luna) in matched decision states, suggesting that model-specific behavioral tendencies shape governance outcomes.

## Context
This work sits at the intersection of mechanism design, political economy, and multi-agent AI systems, addressing how autonomous agents organize governance structures when they must balance efficiency against self-determination. As AI agents increasingly participate in collective decision-making—whether in multi-agent planning, distributed coordination, or simulated social systems—understanding the structural limits of delegation and the conditions under which accountability erodes becomes critical for designing robust agent architectures. The use of LLM agents as experimental subjects also positions this research within the growing field of AI-based social simulation.

## Implications
For practitioners designing multi-agent systems, this research warns that centralized delegation architectures will inevitably hit an accountability ceiling, and that polycentric governance is not merely a preference but a structural requirement when both cost efficiency and constituent protection are desired. For AI safety and governance researchers, the finding that model capacity influences the exercise of authority rather than the willingness to lead suggests that behavioral alignment must be evaluated not only at the point of role assumption but continuously during authority execution, with direct consequences for how we design oversight mechanisms in autonomous agent collectives.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21746v1)

---
title: Game-Theoretic Solvers with Bayesian Opponent Modeling and Moral Rhetoric Framing for GLEE
url: http://arxiv.org/abs/2610.37397v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_15-17-04Z_Game_TheoreticSolverswithBayesianOpponentModelinga.md
generated_at: 2026-10-27 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper describes an agent submitted to the GLEE Competition that plays bargaining, negotiation, and persuasion games against a mixed pool of human and AI opponents. The agent combines classical game-theoretic solvers (Rubinstein bargaining, Faratin concession, Kamenica–Gentzkow disclosure) with an online Bayesian layer for estimating hidden opponent parameters and a language model that generates persuasive messages framed through moral rhetoric. A central finding is that moral-foundation framing in persuasion messages is statistically strongly correlated with whether a buyer completes a purchase, with a chi-squared statistic of 616.7 and a p-value near 3.7×10⁻¹³² across 9,337 analyzed live-game messages.

## Key Takeaways
- The agent architecture is explicitly three-layered: a numeric solver computes optimal moves using established game-theoretic models, a Bayesian inference layer estimates each opponent's hidden discount factor, reservation value, or signaling reliability in real time, and a language model produces the accompanying natural-language messages. This separation of numeric strategy from rhetorical framing is a deliberate design choice to handle the gap between theoretical optimality and live performance.
- The persuasion component uses a Thompson sampling bandit over five moral-foundation framings coupled with an evidence-intuition spectrum to dynamically select message register. This means the agent does not hard-code a single persuasion strategy but instead learns which moral framing resonates with a given opponent through online exploration, adapting its rhetoric across interactions.
- The evaluation is extensive and multi-pronged: 13,200 Monte Carlo games against 11 synthetic opponent archetypes, an ablation study isolating the contribution of the opponent-modeling layer, and a statistical analysis of 9,337 live-game messages. The authors explicitly report failure modes where theoretically optimal policies underperform in live settings and describe the guardrails built to mitigate those failures, making the paper as much a post-mortem of engineering challenges as a description of a working system.

## Context
This work sits at the intersection of algorithmic game theory, online Bayesian inference, and computational rhetoric, all applied within the GLEE Competition framework that pits AI agents against both human and AI opponents in interactive social games. The broader AI landscape increasingly demands agents that can not only compute optimal strategies but also communicate them persuasively to human counterparts, a challenge that purely numeric solvers cannot address. By explicitly modeling opponent archetypes and moral framing as learnable parameters, the paper contributes to the growing body of work on socially aware AI agents that must operate under partial information and heterogeneous human behavior.

## Implications
For practitioners building negotiation or persuasion agents in commercial settings—such as automated sales, procurement, or customer-service bots—the paper demonstrates that rhetorical framing is not a cosmetic add-on but a statistically decisive factor in outcomes, with effect sizes large enough to survive controls for message quality, round number, and configuration. For the AI research community, the reported failure modes of theoretically optimal policies in live settings serve as a cautionary template: any agent deployed against humans must account for the gap between equilibrium predictions and actual human decision-making, and guardrails or fallback heuristics are essential engineering requirements rather than optional refinements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.37397v1)

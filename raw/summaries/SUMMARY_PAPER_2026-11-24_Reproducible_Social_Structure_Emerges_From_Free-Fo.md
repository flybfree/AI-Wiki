---
title: Reproducible Social Structure Emerges From Free-Form Interaction Among LLM Agents
url: http://arxiv.org/abs/2611.31543v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_20-51-57Z_ReproducibleSocialStructureEmergesFromFree_FormInt.md
generated_at: 2026-11-24 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces a repeatable, goal-free, proactive multi-agent framework in which fifty persona-conditioned LLM agents with persistent memory decide whether, with whom, and how to communicate across three social platforms. By running the same world ten times from identical initial conditions for a total of 700 hours, the authors show that most network- and agent-level parameters are stable across repetitions, and that initially broad communication contracts into sparse sustained dyads in every world. The central contribution is a statistically grounded account of emergent within-configuration behavior rather than anecdotal single-run observations.

## Key Takeaways
- Repetition reveals robust structure: across ten identical-start worlds, measured network- and agent-level parameters are stable, and communication contracts from broad early exchange into sparse sustained dyads in all ten runs. Many identical dyads re-form across worlds far more often than expected by chance or by agent-specific sociability alone, indicating a reproducible social-structure process rather than run-specific noise.
- Static personality similarity is a weak predictor of sustained dyads. Instead, alignment and extremity in the emotions and traits expressed during first contact predict whether a pair later forms a sustained dyad, suggesting that early expressive dynamics—not fixed persona traits—drive durable pairing.
- Chain-of-thought expression and transplantation are informative. An agent's emotion and trait expression in its chain-of-thought predicts its future behavior, and swapping either persona prompts or accumulated memories between agents makes recipients behave more like donors; both transplant types move recipients about 60% of the way toward the donor personality, with state-transplanted agents behaving like their donor from the next turn onward.

## Context
Multi-agent LLM simulations are increasingly used as models of social systems, but much of the literature reports phenomena from a single run, leaving unclear which effects are robust features of the simulated system and which are random events. This paper addresses that reproducibility gap by treating the social world as a controlled experimental setting: identical initial conditions, repeated runs, non-perturbative measurement across temporal snapshots, and free-form proactive communication rather than scripted interaction. That design shifts the field from anecdotal case studies toward statistically grounded claims about emergent behavior in agent societies.

## Implications
For researchers, the framework provides a template for separating stable emergent phenomena from idiosyncratic run-to-run variation, and it identifies early-contact emotional/trait alignment as a more predictive signal than static personality similarity. For practitioners building social or organizational simulations, it suggests that persistent memory, first-contact expression, and chain-of-thought affect future behavior and can be transplanted between agents, with partial donor-like behavior emerging quickly. The results also imply that evaluations of LLM social systems should report repeated-world statistics, not just single trajectories, before drawing conclusions about robustness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.31543v1)

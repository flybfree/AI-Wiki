---
title: Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds
url: http://arxiv.org/abs/2610.25114v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-18_08-46-13Z_CompileOnce_RunCheap_Frozen_PortableSkillsforEmbod.md
generated_at: 2026-10-19 21:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary

This paper introduces Skill-RSI, a skill-level recursive self-improvement protocol in which a strong general-purpose model acts solely as an offline author that writes, runs, diagnoses, and repairs manipulation skills in simulation until they pass a hidden validation exam. Once frozen, these skills execute as standalone code or under a cheap caller model, eliminating the need for a frontier model in every episode. The authors demonstrate that Claude Code can compile 4 out of 7 RoboTwin 2.0 manipulation tasks into frozen skills at a cost of USD 4.29–8.22 per skill, and that inherited repair consistently outperforms from-scratch rewriting across controlled campaigns.

## Key Takeaways

- The compile protocol enforces strict isolation: the author model operates without access to hidden validation layouts, inherits only from prior versions, and produces tamper-evident ledgers. This design prevents overfitting to the author's own feedback loop and ensures the frozen skill generalizes to unseen layouts. On hidden layouts, repair that inherits the previous version beat from-scratch rewriting in 8 of 8 controlled campaigns (sign test p = 0.004), indicating that inheritance is the dominant mechanism for improvement rather than development feedback.

- Frozen skills demonstrate remarkable portability and cost efficiency. After compilation, the skills achieved 148/150 successes on new layouts with no model at all, and 147/150 with a DeepSeek-flash caller at a per-episode cost of USD 0.00028–0.00054. This represents a two-to-three-order-of-magnitude reduction in inference cost compared to calling a frontier model every episode, making repeated embodied manipulation economically viable.

- The hardest tasks expose a fundamental limitation: even when every campaign scored 78–95 out of 100, safety aborts (3–16 per run) prevented passing the strict gate of 95% success with zero aborts. A 100-episode exam bounds the abort rate only to 3.6%, meaning the safety constraint cannot be reliably verified within the prescribed evaluation budget. Three tasks failed to compile across 18 campaigns including attempts with GPT-6 and a pre-registered 150-layout run, highlighting that compile-once approaches face hard ceilings on complex manipulation.

## Context

Embodied AI has long lacked the data-rich pretraining pipelines that enabled large language models to acquire broad capabilities cheaply. Current approaches either require per-task demonstrations or a frontier model in every episode, both of which scale poorly. This paper positions itself as a third route between those two extremes, borrowing the software-engineering metaphor of "compile once, run cheap" and adapting recursive self-improvement techniques from the LLM literature to the domain of physical manipulation skills. The work sits at the intersection of program synthesis, embodied agent evaluation, and cost-aware deployment, addressing a practical bottleneck in scaling robot learning beyond curated demonstration sets.

## Implications

For practitioners deploying manipulation agents in warehouses, kitchens, or manufacturing lines, the frozen-skill paradigm offers a path to amortize expensive authoring costs across thousands of cheap inference episodes, potentially reducing per-task operational costs by orders of magnitude. The finding that inheritance-based repair dominates from-scratch rewriting suggests that future skill-compilation pipelines should prioritize versioned lineages and audited ledgers rather than iterative full rewrites. However, the safety-abort ceiling on the hardest tasks signals that compile-once approaches will not replace online adaptation for safety-critical manipulation, and that evaluation protocols must account for rare failure modes that bounded sampling cannot certify.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25114v1)

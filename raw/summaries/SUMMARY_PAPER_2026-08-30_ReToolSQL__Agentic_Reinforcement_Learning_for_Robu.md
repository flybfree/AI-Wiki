---
title: ReToolSQL: Agentic Reinforcement Learning for Robust Text-to-SQL
url: http://arxiv.org/abs/2608.27796v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_00-23-31Z_ReToolSQL_AgenticReinforcementLearningforRobustTex.md
generated_at: 2026-08-30 20:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ReToolSQL, a two‑stage reinforcement learning framework that improves text‑to‑SQL performance by first training on supervised traces and then fine‑tuning with agentic RL. RFT alone reaches 73.66% execution accuracy on BIRD‑SQL, while SFT→RFT yields 74.32% single‑pass and 74.77% with self‑consistency.

## Key Takeaways
- The supervised warm‑start on rejection‑sampled reasoning traces expands the set of solvable questions, raising pass@k coverage on the hardest cases.
- Agentic reinforcement fine‑tuning teaches the model when to verify, what evidence to retrieve, and how to repair faulty SQL using execution feedback.
- Initializing RFT from the SFT checkpoint produces the highest single‑pass accuracy (74.32%) and self‑consistency score (74.77%) on BIRD‑SQL.

## Context
Current text‑to‑SQL systems typically operate in a single turn, limiting their ability to correct mistakes after execution feedback is received. This work demonstrates how reinforcement learning can be applied to generate correct SQL queries within a large language model.

## Implications
For industry practitioners, the method shows that a single dense 31B model can achieve enterprise‑grade accuracy without human annotation, offering a scalable path forward for real‑world deployment where resources are limited and annotation costs are high.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27796v1)

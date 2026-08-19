---
title: An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models
url: http://arxiv.org/abs/2608.17956v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_16-09-51Z_AnOmittedModeIsaRareRule_TheSampling_VerificationD.md
generated_at: 2026-08-18 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how acceptance of a synthesized continuous world model by a planner certifies risk in the Code World Model paradigm and shows that omitted modes create dangerous sampling errors. It demonstrates that models can miss critical events with probability (1−r)^N and that LLM synthesis repairs such omissions often, while proving a localization budget for Lipschitz‑continuous rules.

## Key Takeaways
- The acceptance of a mode‑containing sample guarantees only that the sampled transition is reproduced, not broader safety across all possible transitions.  
- A model with Lipschitz constant at most L differing by η at a point disagrees on a region of volume κ((η−ε)/L)^(d+m), showing a measurable localization budget for rule violations.  
- Re‑scoring confirms that acceptance certifies sample consistency and no more, covering about two percent of the planner’s queries.

## Context
This work extends risk analysis in continuous control by linking model synthesis to classical planning assumptions, revealing that LLM outputs can inherit hidden discontinuities that planners cannot detect. It highlights a gap between formal verification budgets and real‑world model behavior, prompting new standards for model certification.

## Implications
For industry practitioners, the findings suggest that acceptance alone is insufficient for guaranteeing safe autonomous agents, requiring additional validation of Lipschitz continuity across modes. Researchers should develop class‑relative certificates to quantify identifiability and ensure that omission of rules does not compromise planner performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17956v1)

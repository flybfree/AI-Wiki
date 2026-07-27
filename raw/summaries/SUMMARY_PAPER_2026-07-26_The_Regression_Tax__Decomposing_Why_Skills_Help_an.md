---
title: The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents
url: http://arxiv.org/abs/2607.22520v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_17-50-03Z_TheRegressionTax_DecomposingWhySkillsHelpandHurtLL.md
generated_at: 2026-07-26 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a regression tax concept, measuring how adding procedural skills to LLM agents can both improve and degrade performance across many runs. It finds that regressions—failures caused by skill addition—are substantial and often outweigh gains, leading to net loss. The study identifies three mechanisms: osmosis, grounding displacement, and verification displacement.

## Key Takeaways
- Skill description osmosis causes agents to behave differently merely because the skill is present in context, even when not used.
- Grounding displacement occurs when a prescribed procedure overrides the agent’s natural input interpretation.
- Verification displacement happens when procedures suppress checks that would normally validate outputs.

## Context
LLM agents increasingly incorporate procedural skills for office automation tasks. Traditional evaluation focuses on overall success rates, which masks hidden costs like regressions. This work provides a finer-grained analysis of skill impact across diverse benchmarks and model harnesses.

## Implications
Practitioners must evaluate skills by separating gains from regressions rather than relying solely on aggregate improvement metrics. The findings suggest that grounding and verification mechanisms are more critical for reliability than the choice of procedural instructions themselves.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22520v1)

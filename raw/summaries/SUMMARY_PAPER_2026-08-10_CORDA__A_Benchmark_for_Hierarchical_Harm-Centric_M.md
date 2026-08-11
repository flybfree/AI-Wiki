---
title: CORDA: A Benchmark for Hierarchical Harm-Centric Moral Reasoning in Large Language Models
url: http://arxiv.org/abs/2608.08061v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_10-56-30Z_CORDA_ABenchmarkforHierarchicalHarm_CentricMoralRe.md
generated_at: 2026-08-10 22:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CORDA, a benchmark designed to test hierarchical, harm‑centric moral reasoning in large language models. The study evaluates 90 moral dilemmas across four ethical frameworks and finds that most instruction‑tuned LLMs default to deontological choices, often avoiding personal harm even when it reduces overall welfare.

## Key Takeaways
- Models consistently prioritise avoidance of direct personal harm over reducing total harm, revealing a strong deontological bias.  
- Performance on categorical rules such as “do not kill” is higher than on outcome‑based comparisons like minimising aggregate damage.  
- Although models follow explicit chain conditioning, several fail to respect human > animal > robot priority orders.

## Context
Current LLM moral evaluations focus mainly on whether answers are acceptable or avoid obvious violations, leaving the ability to weigh competing harms untested. CORDA fills this gap by forcing models to navigate conflicts where no option is morally cost‑free.

## Implications
The findings suggest that reliability in moral reasoning requires more than default restraint; it demands controllable prioritisation under conflict. Practitioners must design evaluation frameworks that probe hierarchical decision making, not just compliance with simple rules.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08061v1)

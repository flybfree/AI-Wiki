---
title: Logical Regression for Planning with Axioms
url: http://arxiv.org/abs/2607.21414v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_15-16-48Z_LogicalRegressionforPlanningwithAxioms.md
generated_at: 2026-07-23 22:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a method for approximating logical regression when planning domains contain axioms. The approach limits conditions to partial states and minimizes the number of variables considered while avoiding repeated axiom recalculation. Experiments show that the resulting execution monitor can generalize partial states across multiple domains, cutting variable usage by up to 70% and recovering over 50% of the time in environments with unexpected changes.

## Key Takeaways
- The logical regression is approximated using only partial states, which reduces complexity compared to full state conditions.  
- Axioms are not recalculated during execution, improving efficiency and robustness.  
- The method achieves a 70% reduction in variables for monitoring while maintaining high recovery rates (>50%) across diverse domains.

## Context
Automated planning often relies on logical regression to generate compact policies that handle non‑deterministic actions. Traditional approaches suffer from high computational cost when axioms are present, limiting scalability. This work addresses those limitations by focusing on partial state representation and axiom reuse.

## Implications
For AI practitioners, this technique offers a practical way to build more efficient execution monitors without sacrificing performance. In industry settings where planning systems must adapt quickly to domain changes, the reduced variable load can lead to faster decision making and lower resource consumption.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21414v1)

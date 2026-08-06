---
title: Reachability in 3-VAS
url: http://arxiv.org/abs/2608.04786v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_12-51-02Z_Reachabilityin3_VAS.md
generated_at: 2026-08-05 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper resolves the reachability problem for vector addition systems in fixed low dimensions by establishing PSPACE-completeness. It proves PSPACE-hardness of symmetric 3-VAS reachability and combines this with known upper bounds to show PSPACE-complete status for 3- and 4-dimensional VAS as well as their symmetric fragments.

## Key Takeaways
- The authors demonstrate that the reachability problem in symmetric vector addition systems of dimension three is PSPACE-hard, establishing a lower bound that matches the previously known PSPACE upper bound.
- This result extends to both 3-VAS and 4-VAS, confirming that reachability remains PSPACE-complete across these fixed dimensions.
- The findings settle the complexity classification for these systems, removing any remaining uncertainty between NP and PSPACE.

## Context
Vector addition systems are a class of abstract dynamical systems studied in theoretical computer science and AI for modeling decision processes. Understanding their computational limits is crucial because they serve as models for various algorithmic problems, including those relevant to planning and control.

## Implications
These results have direct implications for researchers designing algorithms that must solve reachability queries on such systems, ensuring they are not expected to run in polynomial time unless P=PSPACE.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04786v1)

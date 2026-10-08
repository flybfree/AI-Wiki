---
title: Large-scale Repository Engineering via Agent-Native Reusable Code Primitives
url: http://arxiv.org/abs/2610.09079v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-06_20-20-50Z_Large_scaleRepositoryEngineeringviaAgent_NativeReu.md
generated_at: 2026-10-07 21:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Code Primitives, agent-native reusable executable components equipped with interface contracts, dependency closures, validation tests, and provenance metadata, organized into a searchable library called CodeFace containing 1,424 validated primitives. The authors present LEGO, a framework that activates task-relevant primitives, adapts their implementations to target repositories while resolving cross-component constraints, and iteratively revises results against executed tests, demonstrating substantial improvements in repository-scale code generation across 522 benchmark tasks spanning seven software domains.

## Key Takeaways
- Code Primitives represent a structured, agent-native approach to reusable code components where each primitive uses a resident LLM to assess relevance and adapt its implementation, interfaces, and dependencies to the specific target repository context, distinguishing them from simple code retrieval or vendoring approaches that the authors show are inferior in controlled comparisons.
- The LEGO-REPO benchmark of 522 executable reconstruction tasks across seven software domains, 22 capability tracks, and five difficulty levels reveals that even the strongest of 13 evaluated backbone models achieves only a 0.318 delivery score and scores zero on 41.0% of tasks, highlighting that repository-scale construction remains a significant open challenge. LEGO improves all 13 backbones by 0.1474 on average and raises GPT-5.6-terra from 0.3180 to 0.5134, a 61.4% relative improvement.
- The performance gains persist against independent repository agents, across three external benchmarks, and with a disjointly re-mined CodeFace library, while a smaller GPT-OSS-20B model for adaptation and diagnosis retains 95.1% of the homogeneous score at 24.0% lower cost, suggesting practical scalability for production deployment.

## Context
This work addresses a critical gap in the evolution of LLM-assisted software engineering, where the field has progressed from single-function generation toward repository-scale construction but struggles with the interplay of modules, interfaces, configurations, tests, and dependencies that must cohere in a working codebase. By formalizing reusable components as validated, contract-bearing primitives with built-in adaptation mechanisms, the paper bridges the divide between retrieval-augmented code generation and true compositional software engineering, offering a structured alternative to monolithic prompt-based approaches.

## Implications
For practitioners building agentic coding systems, the CodeFace library and LEGO framework provide a concrete blueprint for decomposing repository construction into validated, composable units that can be adapted per-task rather than regenerated from scratch, potentially reducing both cost and failure rates in production code generation pipelines. The finding that adapted primitives consistently outperform retrieved code supplied as context or vendored unchanged suggests that future AI coding tools should invest in component-level adaptation and validation infrastructure rather than relying solely on larger context windows or stronger base models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09079v1)

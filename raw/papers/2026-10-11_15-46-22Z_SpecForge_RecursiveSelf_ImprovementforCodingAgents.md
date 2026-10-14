---
title: SpecForge: Recursive Self-Improvement for Coding Agents via Behavioral Specifications
published: 2026-10-11T15:46:22Z
authors: Yutong Cheng, Haifeng Chen, Peng Gao, Wei Cheng
url: http://arxiv.org/abs/2610.15708v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpecForge: Recursive Self-Improvement for Coding Agents via Behavioral Specifications

## Abstract
Coding agents based on frozen language models can improve their performance by refining the external context they rely on, without updating model weights. We study recursive self-improvement through behavioral specifications: natural-language code documentation that describes the behavior of program entities and guides agents in generating correct code. We formulate a self-improvement loop in which an agent generates code from its current specifications, evaluates it with execution-verified tests, and refines the specifications based on observed failures. The improved specifications then guide subsequent generation, progressively improving the agent's understanding of the codebase. However, recursive refinement is challenging because program entities are interdependent. Improving the specification of one entity can inadvertently degrade the correctness of others, a phenomenon we call output coupling. This creates a whack-a-mole effect in which local improvements cause regressions elsewhere, preventing consistent progress. We introduce SpecForge, a multi-frontier tree search framework that addresses this challenge with three mechanisms: (i) Pareto-guided state selection preserves complementary specification states and prevents premature commitment; (ii) dependency-constrained entity selection prioritizes callee-before-caller refinement; and (iii) error-diversified expansion explores multiple refinements using different subsets of test failures. On DevEval+, SpecForge achieves the best performance across five backbone models, including a 94.9% solve rate with Claude-4.5-Sonnet and a 5.7-percentage-point average improvement over the strongest baseline. The improved specifications also make the agent better at tasks outside the loop: they transfer to cross-language translation and to new-feature implementation, where they outperform the benchmark-provided requirement documents.

## Metadata
- **Published**: 2026-10-11T15:46:22Z
- **Authors**: Yutong Cheng, Haifeng Chen, Peng Gao, Wei Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15708v1)
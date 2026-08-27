---
title: InsightSR: Refining Symbolic Regression Search Spaces via Parallel Semantic and Structural LLM Guidance
published: 2026-08-26T02:04:20Z
authors: Yating Ling, Wenjing Cun, Zhitang Chen
url: http://arxiv.org/abs/2608.25291v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# InsightSR: Refining Symbolic Regression Search Spaces via Parallel Semantic and Structural LLM Guidance

## Abstract
Symbolic regression (SR) seeks to discover parsimonious mathematical laws from observational data, yet conventional approaches often struggle with the vast combinatorial search space of physically meaningful expressions. We present InsightSR, a framework that embeds Large Language Models (LLMs) as a guiding layer around the PySR genetic programming engine. Rather than relying on LLMs to generate expressions directly, InsightSR uses LLMs to progressively transform the search space itself through two complementary pathways: a Semantic Seed Pathway that proposes dimensionally consistent functional skeletons, and a Structural Feature Pathway that recommends nonlinear feature transformations. These transformations accumulate over iterations, broadening the input space and shifting the symbolic search from constructing deep expression trees over raw variables to assembling shallow trees over a rich, semantically informed feature set. A post-generation feedback loop evaluates candidates, categorizes features by their empirical utility, and refines the guidance for the next iteration, transforming the discovery process from open-ended generation into iterative, self-correcting refinement. Across three benchmarks, InsightSR achieves a 95% exact recovery rate on the Feynman benchmark and 80.18% accuracy on the LLM-SRBench LSR-Transform task, substantially outperforming state-of-the-art genetic programming and neural-symbolic methods while maintaining strong out-of-distribution generalization on real-world datasets.

## Metadata
- **Published**: 2026-08-26T02:04:20Z
- **Authors**: Yating Ling, Wenjing Cun, Zhitang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25291v1)
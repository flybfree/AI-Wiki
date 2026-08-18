---
title: ATLAS: Scaffold-Free Algorithm Synthesis by LLMs via Embedding-Guided Quality-Diversity Search
published: 2026-08-16T05:43:34Z
authors: Danial Yazdani, Mohammad Nabi Omidvar, Yuan Sun, Maksud Ibrahimov, Xiaodong Li
url: http://arxiv.org/abs/2608.15546v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ATLAS: Scaffold-Free Algorithm Synthesis by LLMs via Embedding-Guided Quality-Diversity Search

## Abstract
Most LLM-based automated algorithm design methods optimize a designated component within a human-specified scaffold, fixing overall organization and component interactions. We present ATLAS, an embedding-guided quality-diversity framework for scaffold-free full-algorithm synthesis in combinatorial optimization. The problem specification supplies objectives and constraints; a minimal I/O interface fixes only instance and solution formats; the LLM chooses and restructures components, interactions, and control flow. This freedom enlarges the search space, risking invalid candidates and premature convergence to one design region. ATLAS independently detects execution, interface, and feasibility failures, recomputes objectives, and applies error-conditioned repair; similarity-based archive management preserves algorithms across embedding-space regions to counter premature convergence. Its three-layer search refines the best design, gives other regions dedicated refinement opportunities, and performs cross-region synthesis to recombine components and their interactions. Across four NP-hard problems, ATLAS outperforms several state-of-the-art component-synthesis methods and a matched full-synthesis baseline while remaining competitive with strong human-designed algorithms. One ATLAS run retains several algorithms with comparable performance from distinct embedding-space regions rather than a single design. Code inspection finds that these multi-component designs differ in their primary construction or global-search backbone. Our results suggest that embedding-guided quality-diversity search can make the enlarged full-algorithm design space practically searchable. Source code and exact executable prompts are available at <https://github.com/Danial-Yazdani/ATLAS>.

## Metadata
- **Published**: 2026-08-16T05:43:34Z
- **Authors**: Danial Yazdani, Mohammad Nabi Omidvar, Yuan Sun, Maksud Ibrahimov, Xiaodong Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15546v1)
---
title: SPOC-SQL: Stage-wise Preference Optimization for Controllable Text-to-SQL
published: 2026-08-24T03:48:05Z
authors: Yingnan Chen, Chun Ding, Tianshi Xu, Xu Yang, Si Wu
url: http://arxiv.org/abs/2608.22772v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPOC-SQL: Stage-wise Preference Optimization for Controllable Text-to-SQL

## Abstract
Text-to-SQL aims to translate natural language questions into executable SQL queries over relational databases, requiring multi-stage structured reasoning over database schemas and query constraints. However, existing methods treat this task as single-step generation, where models optimize entire SQL sequences without targeted feedback at key decision points and lack support for interacting with and controlling the intermediate generation process. To address this issue, we propose SPOC-SQL, which decomposes Text-to-SQL into four sequential subtasks following standard SQL execution logic and designs stage-specific optimization strategies for the model to learn key decisions. Specifically, we propose the implementation of fine-grained preference optimisation at key decision points across SQL stages, with the objective of enhancing structured decision-making during query construction. Furthermore, a structured decomposition strategy is designed, facilitating stage-wise intervention and correction through explicit intermediate representations. This results in more controllable and reliable SQL generation. Experiments demonstrate that incorporating stage-wise human knowledge consistently improves performance, validating the effectiveness of stage perception controllable generation.

## Metadata
- **Published**: 2026-08-24T03:48:05Z
- **Authors**: Yingnan Chen, Chun Ding, Tianshi Xu, Xu Yang, Si Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22772v1)
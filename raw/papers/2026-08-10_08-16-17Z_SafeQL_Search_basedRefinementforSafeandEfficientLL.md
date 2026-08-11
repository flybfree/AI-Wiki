---
title: SafeQL: Search-based Refinement for Safe and Efficient LLM-based Text-to-SQL
published: 2026-08-10T08:16:17Z
authors: Geonho Lee, Min-Soo Kim
url: http://arxiv.org/abs/2608.09260v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SafeQL: Search-based Refinement for Safe and Efficient LLM-based Text-to-SQL

## Abstract
Large language models (LLMs) have advanced Text-to-SQL by enabling natural language interfaces to databases without task-specific fine-tuning. However, existing LLM-based systems remain unreliable, often generating SQL queries that are invalid under the database schema, referencing non-existent tables, attributes, functions, or values. Such errors persist because interactions with the database management system (DBMS) are typically limited to error messages, leaving it in a largely passive role during query refinement. This paper proposes SafeQL, \textit{a search-based refinement paradigm that redefines the role of the DBMS as an active guide in the refinement process}. Instead of regenerating entire queries after execution failure, SafeQL interprets DBMS feedback to incrementally repair only the erroneous components. Each refinement step is formulated as a guided search within a \textit{safe query space}, where candidate queries are progressively validated through DBMS execution, thereby converging to an executable query and preventing repeated regeneration of errors. Experiments on the Bird and Spider benchmarks show that SafeQL significantly improves execution accuracy and efficiency compared to regeneration-based methods.

## Metadata
- **Published**: 2026-08-10T08:16:17Z
- **Authors**: Geonho Lee, Min-Soo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09260v1)
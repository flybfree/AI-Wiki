---
title: A Hybrid Dependency-Aware Framework for Task Decomposition and Dynamic Agent Generation in Oracle-to-PostgreSQL Migration
published: 2026-09-13T10:22:05Z
authors: Oleg Grynets, Oleg Kaskun, Alona Seletska, Daryna Tukalo, Vasyl Lyashkevych
url: http://arxiv.org/abs/2609.14413v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Hybrid Dependency-Aware Framework for Task Decomposition and Dynamic Agent Generation in Oracle-to-PostgreSQL Migration

## Abstract
Large language model (LLM)-based database migration is often treated as direct code transformation, although enterprise Oracle systems contain heterogeneous SQL and PL/SQL artifacts with different dependencies, execution order, complexity, and validation needs. This paper proposes a hybrid dependency-aware framework that identifies migration tasks, builds a cross-file dependency graph, condenses cyclic dependencies, and uses task specifications to generate specialized migration agents at runtime. The deterministic path combines ANTLR-based parsing with typed dependency extraction, while an LLM fallback is invoked only for units that cannot be parsed reliably. On a corpus of 116 Oracle files, the pipeline produced 1,037 units with zero coverage gaps and 1,271 AST-derived dependencies. The fallback processed 165 parse-error units, recovered 496 additional validated dependencies, eliminated unresolved-dependency units, and increased resolved internal edges from 446 to 527. The graph contained four dependency-respecting phases, while cycle handling was validated separately using Tarjan SCC condensation. A complementary experiment on 1,006 PL/SQL files regenerated 623 scripts (~62%), of which 380 (~61%) executed successfully in PostgreSQL 16. Tables achieved about 85% regeneration success, whereas no query regenerations succeeded under the evaluated specification-mediated baseline, and procedural objects remained strongly dependent on schema context. These results motivate dependency-aware context delivery, task-specific validation, and differentiated agent routing. The paper also formalizes task-to-agent mapping, introduces monitoring and diagnostics for execution feedback, and defines a controlled comparison of monolithic, static-decomposition, dependency-aware, and dynamically orchestrated migration strategies.

## Metadata
- **Published**: 2026-09-13T10:22:05Z
- **Authors**: Oleg Grynets, Oleg Kaskun, Alona Seletska, Daryna Tukalo, Vasyl Lyashkevych
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14413v1)
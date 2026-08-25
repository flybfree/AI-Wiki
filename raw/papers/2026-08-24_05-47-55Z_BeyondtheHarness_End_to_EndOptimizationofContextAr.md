---
title: Beyond the Harness: End-to-End Optimization of Context Artifacts for Enterprise Text-to-SQL
published: 2026-08-24T05:47:55Z
authors: Kate Gwimm, Carson Eisenach
url: http://arxiv.org/abs/2608.22830v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Harness: End-to-End Optimization of Context Artifacts for Enterprise Text-to-SQL

## Abstract
Deploying LLMs for enterprise Text-to-SQL is bottlenecked less by the model than by what context reaches it: business logic spans thousands of tables, and no model can ingest a full catalog at once. We argue that the most effective place to intervene is therefore the \emph{knowledge-base context} the model consumes, and that this context should be \emph{constructed} from historical usage rather than tuned for as a fixed input. Using a query-DAG decomposition--the same family of intermediates that enterprise benchmarks like BEAVER annotate, here recovered from production SQL--we compare the value of oracle query graphs versus retrieved knowledge-base context. In this ablation, retrieved knowledge-base context provides the largest marginal improvement when added to the full oracle graph. Building on this, we optimize a distillation procedure that turns historical query profiles into reusable SQL reference cards. On a benchmark of 5176 production queries from a major online retailer, optimizing these context artifacts yields larger gains (${\sim}12$--$25\%$ AST similarity) than optimizing the retrieval harness (${\sim}3$--$12\%$). On the public BEAVER benchmark, which lacks the production-usage signals available in our internal setting, the picture is more mixed: table cards alone perform about the same as raw historical SQL. The best optimized variant retrieves both cards and raw SQL, scoring $9.00\%$ versus $6.33\%$ (p-value $0.12$) for the comparable baseline on a held-out $N{=}300$ subset, using retrieved context and harness changes but no agentic loop.

## Metadata
- **Published**: 2026-08-24T05:47:55Z
- **Authors**: Kate Gwimm, Carson Eisenach
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22830v1)
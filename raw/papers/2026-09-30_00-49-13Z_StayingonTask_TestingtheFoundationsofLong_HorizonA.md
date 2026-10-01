---
title: Staying on Task: Testing the Foundations of Long-Horizon Agent Reliability
published: 2026-09-30T00:49:13Z
authors: Jeffrey Willette, Krishna C. Puvvada, Boris Ginsburg
url: http://arxiv.org/abs/2609.38712v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Staying on Task: Testing the Foundations of Long-Horizon Agent Reliability

## Abstract
Long-horizon agentic workflows require models to sustain repeated state-dependent actions all while the context grows, sub-task complexity changes, and new data arrives. Each situation represents an independent axis along which an agent may fail. An agent reconciling a long ledger, for example, must repeatedly read its state, update the correct record, and preserve alignment across thousands of outputs. A model may accept the entire ledger yet lose its place or stop applying the operation consistently as generation proceeds. We introduce Long-Transduction, a controlled diagnostic that tests a model's ability to stay on task during long generation while continuously reading, mutating, and outputting input-context dependent operations such as arithmetic, sorting, variable lookups, and table transformations. Long-Transduction evaluation independently varies local task complexity, input data formatting, and context length isolate failures along each axis. We evaluate seven open-weight models, finding a 62.8\% decrease when scaling context length from 4-128K, a 36.5\% decrease when varying input format, and a 39.9\% decrease by increasing local task complexity. Together, these failures represent critical liabilities in long-horizon agentic workflows.

## Metadata
- **Published**: 2026-09-30T00:49:13Z
- **Authors**: Jeffrey Willette, Krishna C. Puvvada, Boris Ginsburg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38712v1)
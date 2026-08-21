---
title: Inducing Task Models from Computer-Use Traces
url: http://arxiv.org/abs/2608.20319v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_17-57-00Z_InducingTaskModelsfromComputer_UseTraces.md
generated_at: 2026-08-20 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Task Model Induction (TMI), a method that extracts latent tasks from unstructured computer‑use traces and builds hierarchical task models with both objective decomposition and procedural control flow. On human and agent trajectories, TMI achieves 0.974 agreement with ground‑truth groupings and reconstructs 74.9 % of observed steps, outperforming prior workflow baselines. The induced skills also boost held‑out task accuracy by 30 %.

## Key Takeaways
- TMI discovers concurrent tasks in a trace without predefined goals, separating interleaved activities into distinct latent tasks.
- For each discovered task it creates a model that pairs a recursive goal hierarchy with the execution control flow, enabling structured representation of work.
- The method’s reconstruction accuracy (74.9 %) and skill‑based improvement (30 % boost) exceed those of existing workflow induction approaches.

## Context
Computer‑use traces capture real‑world interaction data that can inform AI agents learning tasks. Current methods often produce flat step summaries, ignoring the multi‑threaded nature of human work, limiting their usefulness for auditing or transferring knowledge across environments.

## Implications
TMI offers a scalable way to turn raw logs into reusable task models, supporting more reliable and adaptable AI assistants in professional settings. Practitioners can leverage these models to audit workflows, improve agent performance, and share knowledge across teams without manual annotation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20319v1)

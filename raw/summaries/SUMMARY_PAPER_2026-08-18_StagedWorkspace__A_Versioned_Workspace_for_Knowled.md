---
title: StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents
url: http://arxiv.org/abs/2608.18050v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_17-44-18Z_StagedWorkspace_AVersionedWorkspaceforKnowledge_Wo.md
generated_at: 2026-08-18 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces StagedWorkspace, a versioned workspace that ties parsed views and review diffs to content hashes of native files. Experiments on OfficeQA Pro and APEX-Agents show dual access improves performance by 8-12 points in Pass@1 and rubric scores.

## Key Takeaways
- The workspace binds parsed records and review diffs to content hashes, ensuring explicit version tracking.
- Dual parsed/native access yields higher point estimates than single view for all tested models.
- SW-AGENT achieves 63.9% on OfficeQA with Gemini 3.1 Pro versus 29.3% baseline.

## Context
Knowledge-work agents often operate on multiple versions of the same artifact, creating ambiguity in search and editing. Current solutions like repository contracts handle code but not mixed formats such as PDFs or spreadsheets. This gap limits performance and reproducibility.

## Implications
The findings suggest that workspace state should be treated as an experimental variable in agent design. Benchmarks must evaluate evidence, staged edits, and artifacts as explicit transitions to better align with real workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.18050v1)

---
title: BlueprintRepair: Typed Local Edits for Failed Lean Proof Blueprints
url: http://arxiv.org/abs/2607.28110v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_12-17-31Z_BlueprintRepair_TypedLocalEditsforFailedLeanProofB.md
generated_at: 2026-07-30 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BlueprintRepair, a repair interface that modifies Lean proof blueprints using ten schema‑checked local operations. It evaluates typed edits, source patches, and module rewrites on a benchmark of 142 controlled failures. The results show typed edit is the most cost effective.

## Key Takeaways
- Typed repair solves almost all localized failures with DeepSeek-V4-Flash while being cheaper than exact patches or full rewrites.
- The repair interface enforces that every edited node is named and that used lemmas are declared, preventing unintended theorem changes.
- Within a 10 000 token budget the typed approach reaches near final coverage whereas free‑form methods lag significantly.

## Context
Proof assistants rely on formal blueprints to guide LLM reasoning. Repairing these graphs after failure is essential for reliable automated proof generation. This work adds a structured, schema‑checked repair mechanism that can be integrated into existing systems.

## Implications
Practitioners can adopt BlueprintRepair to improve the robustness of AI‑assisted theorem proving without sacrificing speed or cost. The approach sets a benchmark for evaluating repair strategies in formal verification pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28110v1)

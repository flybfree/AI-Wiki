---
title: SEPO: Evidence-Grounded Prompt Optimization via Structural Editing
url: http://arxiv.org/abs/2608.28067v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_08-37-34Z_SEPO_Evidence_GroundedPromptOptimizationviaStructu.md
generated_at: 2026-08-30 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
SEPO introduces a multi‑trajectory prompt optimisation framework that records edit‑effect lineage to make improvements interpretable and actionable. On a held‑out suite of 14 tasks it outperforms the leading baseline GEPA by 3.1 pp on Llama‑3.1‑8B‑Instruct and 2.2 pp on Qwen3‑8B, achieving macro accuracy of 61.9 % and 73.3 %. SEPO also uses fewer optimisation tokens (2.9 M vs 4.1 M) and yields prompts up to five times shorter.

## Key Takeaways
- SEPO records edit‑effect lineage for each local edit rather than rewriting the whole prompt, providing a traceable record of what changes are made.
- The framework links target structural operations to examples that are fixed or broken, enabling explainability beyond post‑hoc inspection.
- SEPO achieves higher macro accuracy (61.9 % and 73.3%) while spending fewer optimisation tokens than GEPA.

## Context
Prompt optimisation is a critical task for aligning large language models with user intent, yet existing methods treat each iteration as an opaque whole‑prompt rewrite, limiting interpretability. SEPO’s lineage‑based approach addresses this gap by making the process traceable and actionable within the AI research community.

## Implications
For practitioners, SEPO offers a more transparent tool that can be integrated into automated pipelines without sacrificing performance. Its efficiency and interpretability could set new standards for prompt engineering in industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28067v1)

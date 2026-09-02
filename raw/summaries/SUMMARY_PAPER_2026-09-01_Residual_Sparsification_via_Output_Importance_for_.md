---
title: Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs
url: http://arxiv.org/abs/2609.00575v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_02-11-40Z_ResidualSparsificationviaOutputImportanceforCompre.md
generated_at: 2026-09-01 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PARSER, a residual sparsification method for Mixture-of-Experts LLMs that compresses projection matrices by separating shared base and per‑expert residuals. By focusing on preserving expert output error rather than minimizing isolated matrix errors, PARSER reduces accuracy loss to 1.41× on Qwen and 1.44× on DeepSeek while maintaining the same memory reduction.

## Key Takeaways
- The existing compression objective targets each residual matrix independently, which can cause small errors to propagate through hidden representations and increase expert output error.
- PARSER redefines the objective as preserving the overall expert output error by measuring its contribution via output importance.
- Experiments demonstrate that PARSER narrows the accuracy gap to the uncompressed model by 1.41× on Qwen and 1.44× on DeepSeek without sacrificing peak memory reduction.

## Context
Mixture‑of‑Experts models scale large language models but require huge GPU memory, prompting research into compression techniques that retain performance. Traditional sparsification methods often fail to account for the interdependence of matrix projections within an expert, leading to hidden error propagation and accuracy degradation.

## Implications
For practitioners deploying MoE systems, PARSER offers a practical way to achieve substantial memory savings while keeping model quality high, supporting broader adoption in resource‑constrained environments. The shift from per‑matrix optimization to output‑error preservation sets a new standard for compression objectives in large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00575v1)

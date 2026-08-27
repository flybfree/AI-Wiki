---
title: Unfolding Scientific Papers into Multi-Turn Generation Trajectories for Continued Pre-Training
url: http://arxiv.org/abs/2608.25826v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_14-06-29Z_UnfoldingScientificPapersintoMulti_TurnGenerationT.md
generated_at: 2026-08-26 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a pipeline that transforms full scientific papers into multi‑turn generation trajectories where a teacher model reconstructs the writing process, preserving all original text. It creates a large continued pre‑training (CPT) corpus roughly twice the size of the source material and demonstrates that fine‑tuning on this data improves academic writing benchmarks while maintaining reasoning ability.

## Key Takeaways
- The pipeline preserves every section and abstract verbatim, turning the whole paper into a structured generation trajectory. - It doubles the effective training data size for CPT without adding new content. - The resulting SFT dataset anchors tasks in held‑out papers, forming PAW‑Bench with rubrics.

## Context
Current synthetic‑data research focuses on short web snippets and local thought recovery, leaving document structure untouched. Scientific papers offer a uniform scaffold that can be leveraged for large‑scale pre‑training of language models.

## Implications
This approach enables practitioners to boost writing performance across academic benchmarks while preserving reasoning skills. It also provides a scalable method for generating instruction data and evaluation tasks directly from existing research outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25826v1)

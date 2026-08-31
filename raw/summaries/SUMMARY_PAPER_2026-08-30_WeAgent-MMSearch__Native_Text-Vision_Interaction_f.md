---
title: WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents
url: http://arxiv.org/abs/2608.28062v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_08-28-43Z_WeAgent_MMSearch_NativeText_VisionInteractionforMu.md
generated_at: 2026-08-30 20:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WeAgent-MMSearch, a multimodal search system that enables agents to interact natively with both text and images retrieved from the web. By using persistent disk references for images, the model can continuously cite visual evidence throughout its reasoning trajectory. The authors demonstrate that post‑training with Failure-Aware GSPO boosts performance on VisTarget-Bench by 19.22 points, surpassing comparable open‑source models.

## Key Takeaways
- WeAgent-Harness stores retrieved images as persistent disk references, allowing agents to inspect and cite them throughout a search trajectory.
- The system employs Failure-Aware GSPO to recover salvageable abnormal rollouts and filter invalid ones, improving bounded multimodal planning.
- VisTarget-Bench provides 150 human‑verified tasks that pair questions with held‑out target images, distinguishing image‑retrieval failures from visual‑perception failures.

## Context
Multimodal search agents aim to integrate textual and visual evidence for richer reasoning. Existing frameworks often treat images as ephemeral or omit them from context, limiting the depth of visual grounding. This work addresses those gaps by embedding persistent image references within a robust harness and applying failure‑aware training techniques.

## Implications
The results show that native text‑vision interaction can significantly enhance search accuracy even with modest parameter budgets. Practitioners can adopt similar disk‑reference strategies to retain visual context, leading to more reliable and interpretable agentic behavior in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28062v1)

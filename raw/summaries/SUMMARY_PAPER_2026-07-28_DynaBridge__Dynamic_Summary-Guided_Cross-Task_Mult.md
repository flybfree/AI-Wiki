---
title: DynaBridge: Dynamic Summary-Guided Cross-Task Multimodal Fusion for DASS-Structured Mental Health Assessment
url: http://arxiv.org/abs/2607.25679v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_12-55-29Z_DynaBridge_DynamicSummary_GuidedCross_TaskMultimod.md
generated_at: 2026-07-28 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DynaBridge, a dynamic summary‑guided cross‑task multimodal framework designed to predict depression, anxiety, and stress risk from DASS‑21 structured questionnaires. It combines acoustic, visual, and textual cues across sessions with LLM‑generated semantic summaries to improve ordinal item distribution prediction and overall risk assessment.

## Key Takeaways
- DynaBridge encodes multiple modalities and augments them with frozen‑LLM generated DASS‑aware summaries that serve as participant‑level semantic evidence.  
- The model predicts ordinal item distributions from soft scores and reconstructs risk evidence for depression, anxiety, and stress before fusing it with direct multimodal predictions.  
- A confidence‑aware refinement strategy adds high‑confidence semantic cues only when they are reliable, preserving conservatism in the final output.

## Context
The integration of structured mental‑health questionnaires like DASS‑21 into AI systems requires modeling their psychometric mapping between items and subscale risk labels. Current fusion approaches often treat these mappings as static, limiting performance on real‑world clinical data where session dynamics vary.

## Implications
This work demonstrates that bridging multimodal cues with semantically informed summaries can boost both high‑level risk prediction and fine‑grained item scoring. Practitioners in mental‑health AI may adopt similar dynamic fusion strategies to improve diagnostic accuracy while respecting questionnaire structure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25679v1)

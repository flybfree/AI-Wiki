---
title: CueMem: Cue-Guided Context Reconstruction for Long-Term Conversational Memory
url: http://arxiv.org/abs/2609.12354v1
type: paper-summary
date: 2026-09-13
source_paper: 2026-09-11_02-27-22Z_CueMem_Cue_GuidedContextReconstructionforLong_Term.md
generated_at: 2026-09-13 23:24
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
CueMem addresses the limitations of long-term conversational memory by introducing a cue-guided framework that reconstructs query-relevant dialogue context from source turns rather than relying on compressed summaries or full histories. The method extracts fine-grained cues linked to specific turns and expands them via a turn graph during retrieval, enabling LLMs to generate answers from compact, reconstructed evidence. Experiments demonstrate superior performance over baselines while significantly reducing token usage and latency compared to full-history approaches.

## Key Takeaways
- Current long-term memory approaches struggle with the trade-off between high costs and unreliability of full dialogue histories versus the loss of fine-grained evidence in compressed memory units; CueMem mitigates this by treating extracted records as retrieval cues that guide the reconstruction of query-relevant context from original source turns.
- The framework operates by extracting fine-grained memory cues during construction and linking them to specific source turns, then at query time retrieving relevant cues, mapping them to anchors, and expanding across a turn graph

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.12354v1)

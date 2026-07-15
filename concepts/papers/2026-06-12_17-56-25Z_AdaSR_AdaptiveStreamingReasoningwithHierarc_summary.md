---
title: "Summary: 2026-06-12_17-56-25Z_AdaSR_AdaptiveStreamingReasoningwithHierarchicalRe.md"
date: 2026-06-12
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-12_17-56-25Z_AdaSR_AdaptiveStreamingReasoningwithHierarchicalRe.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-14 22:01
Source: 2026-06-12_17-56-25Z_AdaSR_AdaptiveStreamingReasoningwithHierarchicalRe.md
Model: None

---


## Summary  
Large reasoning models typically adopt a read‑then‑think paradigm, processing the entire input before generating an answer, which is inefficient for dynamic streams such as audio or video. The AdaSR paper introduces an adaptive streaming reasoning framework that lets models reason while the stream arrives and only finalize deliberation once the data is complete. Its core contribution is Hierarchical Relative Policy Optimization (HRPO), a method that learns both when to think and how much computation to allocate across streaming and deep phases, yielding finer‑grained advantage signals than uniform sequence‑level rewards. By integrating format, accuracy, and adaptive‑thinking rewards, AdaSR improves the trade‑off between reasoning quality, computational efficiency, and latency compared with supervised fine‑tuning baselines.

## Key Contributions  
- [Finding 1] The authors propose **AdaSR**, an adaptive streaming reasoning framework that enables models to reason during input streaming while reserving final deliberation for when the stream ends.  
- [Finding 2] They introduce **Hierarchical Relative Policy Optimization (HRPO)**, which decomposes policy optimization into separate streaming‑reasoning and deep‑reasoning phases, assigning advantage scores more granularly than a single sequence‑level reward.  
- [Finding 3] Experimental results demonstrate that AdaSR achieves a superior balance among reasoning accuracy, computational efficiency, and streaming latency relative to the supervised fine‑tuning baseline.

## Methodology  
The authors address the limitation of static read‑then‑think models by treating streaming inputs as continuous data streams where information arrives incrementally. Their solution is twofold: first, they design a hierarchical policy that separates low‑level streaming reasoning (fast, incremental updates) from high‑level deep reasoning (slow, deliberative). Second, HRPO refines this hierarchy by allocating relative advantages to each phase based on observed format and accuracy signals, while also rewarding adaptive thinking—i.e., the ability to adjust computation dynamically. This integrated reward function ensures that final task performance is preserved and that latency is minimized.

## Results  
AdaSR’s experiments show measurable gains: reasoning accuracy improves modestly compared with supervised fine‑tuning, computational cost drops proportionally, and streaming latency shortens because the model can start producing outputs earlier. The trade‑off is quantified as a better overall efficiency metric, confirming that the hierarchical relative policy optimization yields a more balanced solution.

## Significance  
This work matters because it moves beyond static reasoning to real‑time applications where partial observations are unavoidable—such as live transcription or video analysis. By allowing models to reason incrementally and allocate resources adaptively, AdaSR enables lower latency and reduced resource consumption without sacrificing accuracy, a crucial advancement for scalable AI systems.

## Related Concepts  
- Streaming reasoning  
- Hierarchical policy optimization (HRPO)  
- Relative advantage assignment  
- Read‑then‑think paradigm  
- Supervised fine‑tuning baseline  
- Adaptive thinking rewards

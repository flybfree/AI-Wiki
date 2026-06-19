---

title: "Summary: AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization"
url: http://arxiv.org/abs/2606.14694v1
type: paper-summary
date: 2026-06-14
source_paper: 2026-06-12_17-56-25Z_AdaSR_AdaptiveStreamingReasoningwithHierarchicalRe.md
generated_at: "2026-06-14 22:00"
model: nvidia/nemotron-3-nano-4b

---


## Summary
AdaSR introduces an adaptive streaming reasoning framework that allows models to reason while receiving continuous input, learning when and how much computation to allocate. The method uses Hierarchical Relative Policy Optimization (HRPO) to refine the decision process, achieving a superior balance between reasoning accuracy, computational efficiency, and streaming latency compared with supervised fine‑tuning baselines.

## Key Takeaways
- AdaSR learns dynamic thinking schedules that adapt to incoming data, enabling real‑time updates without pre‑defined trajectories.  
- HRPO decomposes optimization into separate streaming and deep reasoning phases, assigning advantages more granularly than a single sequence‑level reward.  
- The framework improves the trade‑off among accuracy, latency, and resource usage over supervised fine‑tuning approaches.

## Context
Streaming reasoning is essential for applications involving audio, video, or other time‑varying data where inputs arrive incrementally. Prior work often relies on manually crafted trajectories, limiting flexibility and scalability in dynamic environments.

## Implications
This research offers practitioners a more efficient way to deploy large models in real‑time settings, reducing latency while preserving performance. The approach can lower computational costs for industry‑grade streaming services that require continuous inference without sacrificing quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.14694v1)

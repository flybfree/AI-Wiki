# Summary: 2026-04-23_17-59-54Z_TemporalTaskificationinStreamingContinualLearning_.md
Saved: 2026-04-29 02:51
Source: 2026-04-23_17-59-54Z_TemporalTaskificationinStreamingContinualLearning_.md
Model: qwen3.6:35b

---

## Summary
This paper challenges the assumption that temporal partitioning in Streaming Continual Learning (CL) is a neutral preprocessing step. The authors argue that the process of converting a continuous data stream into discrete tasks—termed temporal taskification—is a structural component of evaluation, capable of inducing significant variability in CL outcomes. They introduce formal metrics to quantify this instability and demonstrate experimentally that varying the boundaries of these tasks can materially alter performance metrics like forgetting and backward transfer across established CL models.

## Key Contributions
1. **Taskification-Level Framework:** Introduction of a framework utilizing plasticity and stability profiles, profile distance, and Boundary-Profile Sensitivity (BPS) to rigorously diagnose how sensitive CL regimes are to changes in task boundaries.
2. **Demonstration of Instability:** Empirical evidence showing that the choice of temporal split for streaming data can drastically change the reported performance

[[Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability]]
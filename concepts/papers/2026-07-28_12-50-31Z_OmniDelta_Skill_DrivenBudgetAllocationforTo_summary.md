# Summary: 2026-07-28_12-50-31Z_OmniDelta_Skill_DrivenBudgetAllocationforTokenComp.md
Saved: 2026-07-28 20:29
Source: 2026-07-28_12-50-31Z_OmniDelta_Skill_DrivenBudgetAllocationforTokenComp.md
Model: None

---

## Summary  
OmniModal Large Language Models (OmniLLMs) integrate text, audio, and video into a single system but suffer from high memory and inference costs due to long token sequences. Existing compression techniques allocate a fixed budget per modality, which often leads to either under‑utilized evidence or redundant content retention. This paper introduces OmniDelta, a training‑free skill‑driven framework that reallocates the retained‑token budget based on query intent and local complexity. The approach enables more efficient memory usage while preserving accuracy across various pruning ratios.

## Key Contributions  
- [Finding 1] Direct query‑to‑audio/video similarity is unreliable for inter‑modal budget allocation, causing suboptimal token selection.  
- [Finding 2] Uniform intra‑modal budgets miss key evidence and retain redundant content, degrading compression quality.  
- [Finding 3] OmniDelta establishes a new accuracy‑efficiency Pareto frontier across pruning ratios, demonstrating superior trade‑offs.

## Methodology  
OmniDelta first builds audio and video skill pools that map query demand to the retained‑token budget, thereby shifting the fixed allocation dynamically. It then reallocates modality budgets over audio segments and video frames using local complexity measures and temporal redundancy detection. The resulting local budgets are integrated with existing pruning strategies, allowing the total retained‑token ratio to remain constant while redistributing resources where they matter most.

## Results  
Experiments on four audio‑video benchmarks with two Qwen2.5‑Omni models show that at 25 % token retention, OmniDelta reduces GPU memory consumption by 22.0 % and provides a 1.64× end‑to‑end speedup compared to full‑token inference. The framework maintains or improves accuracy across all pruning ratios, establishing a new state‑of‑the‑art Pareto frontier.

## Significance  
By decoupling budget allocation from static quotas, OmniDelta tackles the core bottleneck of memory and latency in OmniLLMs, enabling scalable deployment on resource‑constrained hardware. The method’s training‑free nature lowers development overhead, making high‑quality compression accessible to a broader range of applications.

## Related Concepts  
- Token compression  
- Budget allocation  
- Inter‑modal similarity  
- Intra‑modal redundancy  
- Skill pools  
- Pareto frontier  
- Qwen2.5‑Omni models

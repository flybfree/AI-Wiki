---

title: "Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation"
url: http://arxiv.org/abs/2605.21125v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-20_12-57-37Z_AdvantageCollapseinGroupRelativePolicyOptimization.md
generated_at: "2026-06-11 10:43"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper diagnoses advantage collapse in Group Relative Policy Optimization (GRPO), a failure mode where homogeneous rewards produce near‑zero advantages and vanishing gradients, and introduces the Advantage Collapse Rate as a diagnostic metric. It demonstrates that ACR predicts training stagnation across models from 0.5B to 14B parameters on mathematical reasoning benchmarks. The authors then propose Adaptive Virtual Sample Policy Optimization (AVSPO), which reduces advantage collapse by 58‑63% and yields consistent accuracy gains of 4‑6 percentage points while preserving out‑of‑domain generalization.

## Key Takeaways
- Advantage collapse causes homogeneous groups to generate ineffective gradients, leading to training stagnation.  
- The Advantage Collapse Rate quantifies the proportion of batches with near‑zero advantages as a reliable diagnostic tool.  
- AVSPO mitigates collapse by injecting virtual reward samples guided by real‑time ACR monitoring without extra rollouts.

## Context
Advantage collapse undermines progress in RL from verifiable rewards, especially for large language models that rely on group‑wise reasoning. This issue is critical because it limits the scalability of methods that improve model performance through collective feedback.

## Implications
For practitioners, detecting and mitigating advantage collapse can unlock consistent improvements across model sizes without costly rollouts. The findings suggest a path toward more robust RL training pipelines in AI research and industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.21125v1)

# Summary: 2026-08-10_07-43-05Z_BeyondSolvability_TaskLearnabilityasaStaticPriorfo.md
Saved: 2026-08-10 23:40
Source: 2026-08-10_07-43-05Z_BeyondSolvability_TaskLearnabilityasaStaticPriorfo.md
Model: None

---

## Summary  
The paper investigates why uniform task sampling in reinforcement‑learning post‑training of large language models is inefficient and proposes learning‑ability as a static prior to guide selection. It defines learnability as the expected positive response of a task to continued training under a fixed RL regime, measured from reward trajectories. The authors introduce TrajVal, a lightweight probe‑based estimator that captures this metric with only a short probe run and two endpoint evaluations. Their work shows that using learnability improves data efficiency and complements existing online schedulers.

## Key Contributions  
- [Finding 1] Uniform task sampling ignores differences in how tasks respond to optimization, leading to wasted compute.  
- [Finding 2] Learnability is a reproducible, regime‑conditional measure of expected positive response to further training and predicts downstream utility.  
- [Finding 3] TrajVal provides a lightweight probe‑based estimator that approximates per‑task learnability from minimal data.

## Methodology  
The authors analyze reward trajectories across many tasks to discover that some tasks improve dramatically with additional RL steps while others plateau quickly, yet both may have similar current pass rates. They formalize this residual axis as “learnability,” a static prior that quantifies expected improvement. To estimate it before training begins, they develop TrajVal: run a short probe on the task, evaluate its reward at the start and end of a fixed RL post‑training window, and compute an approximate learnability score from these two points plus the probe result.

## Results  
Experiments on mathematical and logical reasoning benchmarks across multiple model scales demonstrate that tasks selected by TrajVal achieve higher pass rates with fewer RL steps than uniform sampling. Moreover, when combined with online schedulers, TrajVal yields complementary gains in data efficiency without sacrificing performance.

## Significance  
By turning learnability into a static prior, the paper reduces unnecessary compute allocation and enables smarter task selection for LLMs, which is crucial as model sizes grow. This approach makes reinforcement‑learning post‑training more scalable and cost‑effective, supporting broader adoption of RL in language model development.

## Related Concepts  
RL post‑training, task learnability, static prior, reward trajectories, probe‑based estimator, uniform sampling, online scheduling, data efficiency, LLMs.

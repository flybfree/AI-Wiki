---
title: One Rollout Is All You Get: Fully Test-Time Adaptation for GUI Agents
url: http://arxiv.org/abs/2609.34321v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_05-00-45Z_OneRolloutIsAllYouGet_FullyTest_TimeAdaptationforG.md
generated_at: 2026-09-28 23:04
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces SOLO, a fully test-time adaptation method for GUI agents that operates under strict constraints: no ground truth, irreversible actions requiring single-rollout execution, and no pre-deployment learning phase. By leveraging auxiliary models to judge success and relabel subtasks within a sliding window of admitted episodes, SOLO enables continuous weight updates via self-distillation, yielding significant performance gains over frozen baselines on standard web and mobile benchmarks.

## Key Takeaways
- Real-world GUI deployment imposes unique constraints where agents face irreversible actions with only one attempt per task, necessitating a new adaptation paradigm called fully test-time adaptation that discards assumptions about ground truth availability or multiple rollout opportunities.
- The proposed SOLO method utilizes auxiliary models to process episodes in real-time: a judge identifies successful interactions while a proposer-verifier pair relabels prefixes of failed attempts with completed subtasks, allowing the system to update weights through top-K self-distillation on the agent's own predictions within a sliding window.
- Empirical evaluations across WebArena, VisualWebArena, and MobileWorld demonstrate that SOLO improves success rates by three to six points compared to frozen agents using UI-TARS-7B and Qwen3-VL-8B backbones, out

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34321v1)

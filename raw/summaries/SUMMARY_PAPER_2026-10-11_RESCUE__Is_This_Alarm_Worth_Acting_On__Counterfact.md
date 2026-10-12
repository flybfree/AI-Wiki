---
title: RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors
url: http://arxiv.org/abs/2610.13516v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_12-38-35Z_RESCUE_IsThisAlarmWorthActingOn_CounterfactualEval.md
generated_at: 2026-10-11 21:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces RESCUE, a counterfactual evaluation framework that assesses whether runtime failure monitors for Vision-Language-Action (VLA) robot policies produce alarms that actually enable useful interventions, rather than merely classifying executions as failed or successful. By restoring simulator and policy states at execution checkpoints and comparing alternative actions across 128,340 counterfactual branches, the authors demonstrate that a monitor's practical value depends jointly on the specific intervention available and the workload in which it is deployed, not simply on detection accuracy.

## Key Takeaways
- Recoverability is determined by the state-intervention pair rather than by robot state alone: at a recovery threshold of τ=0.5, only 14 of 66 OpenVLA-OFT/LIBERO-Plus failures contain a recoverable checkpoint under continuation, compared with 34 of 66 when both continuation and scripted recovery are permitted, showing that the type of intervention fundamentally changes which failures are actionable.
- Even an idealized detector operating under a stop-and-reset intervention model can tolerate only a 2.0–3.3% false-alarm rate before unnecessary resets outweigh the savings gained from stopping failures early, meaning that high detection scores alone do not guarantee lower intervention cost in strong-policy conditions.
- RESCUE identifies the latest checkpoint satisfying a specified recovery criterion and evaluates whether acting on alarms reduces expected task-completion cost, revealing that recovery actions can paradoxically reduce recoverability in certain conditions, undermining the assumption that earlier intervention is always beneficial.

## Context
Runtime monitors for robot policies have traditionally been evaluated through classification metrics such as precision and recall, which measure how well a monitor distinguishes failed from successful executions. This paper challenges that paradigm by arguing that classification accuracy is insufficient for practical deployment, since a correctly identified failure may arrive too late for recovery, and a false alarm may disrupt an otherwise successful execution. The work sits at the intersection of VLA policy safety, counterfactual reasoning, and intervention cost analysis, addressing a gap in how the robotics and embodied AI community evaluates monitoring systems for deployed agents.

## Implications
For practitioners deploying VLA-based robot policies in production settings, these findings warn against selecting runtime monitors based solely on detection benchmarks, as the actual intervention mechanism and task workload determine whether monitoring provides net benefit. The extremely low tolerable false-alarm rate under stop-and-reset policies suggests that current monitoring approaches may need to incorporate intervention-aware evaluation before deployment, and that designing recovery strategies jointly with monitors is essential. The framework also signals to the broader embodied AI community that safety evaluation must move beyond binary failure detection toward cost-aware, counterfactual assessment of monitoring systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13516v1)

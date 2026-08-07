# Summary: 2026-08-05_10-50-46Z_WhenPrivilegedGuidanceMisaligns_State_MatchedRouti.md
Saved: 2026-08-06 20:25
Source: 2026-08-05_10-50-46Z_WhenPrivilegedGuidanceMisaligns_State_MatchedRouti.md
Model: None

---

## Summary  
The paper tackles the problem of “privileged guidance misalignment” in multi‑turn agents, where a teacher’s reference trajectory may describe states that are never reached by the student because its actions and subgoal ordering differ. To resolve this mismatch, the authors propose State‑Matched Routing and Contextualized Self‑Distillation (SMRC‑SD), which only applies teacher guidance when the current execution state aligns with a supported reference state and builds teacher context that is conditioned on that actual state. By doing so, SMRC‑SD avoids unreliable supervision and improves learning efficiency in interactive environments.

## Key Contributions  
- [Finding 1] State‑Matched Routing explicitly selects turns where the student’s current execution state matches a state along the successful reference trajectory, discarding mismatched turns.  
- [Finding 2] Contextualized Self‑Distillation constructs teacher context that is conditioned on the actual state reached, grounding supervision in locally compatible information.  
- [Finding 3] SMRC‑SD consistently outperforms unconditional full‑path distillation, boosting task success from 0.746 to 0.865 on ALFWorld and from 0.574 to 0.693 on WebShop for Qwen3‑1.7B.

## Methodology  
SMRC‑SD operates at each turn by first checking whether the student’s execution state is present in a pre‑computed set of supported states derived from the teacher’s trajectory. If a match exists, the algorithm routes distillation to that turn and simultaneously generates a teacher context vector built from the corresponding segment of the successful reference path, ensuring the guidance reflects the actual state. This dual verification—state matching plus context conditioning—filters out irrelevant supervision while preserving dense, state‑aware feedback.

## Results  
Empirical evaluations on ALFWorld and WebShop show that SMRC‑SD improves Qwen3‑1.7B’s task success rates by 0.119 (ALFWorld) and 0.119 (WebShop), respectively, compared to baseline unconditional successful full‑path distillation. Controlled ablations demonstrate that both the state‑matching routing and the context‑conditioned teacher guidance contribute positively to these gains.

## Significance  
By aligning privileged guidance with the student’s actual execution state, SMRC‑SD mitigates a critical flaw in conventional on‑policy distillation: reference‑state mismatch. This leads to more reliable, efficient learning for multi‑turn agents that must navigate dynamic and interactive environments where trajectories diverge from the teacher’s plan.

## Related Concepts  
- Privileged on‑policy distillation  
- State‑matched routing  
- Contextualized self‑distillation  
- Multi‑turn agents  
- ALFWorld benchmark  
- WebShop benchmark

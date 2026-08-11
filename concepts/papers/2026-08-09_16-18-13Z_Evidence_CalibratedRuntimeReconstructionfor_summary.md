# Summary: 2026-08-09_16-18-13Z_Evidence_CalibratedRuntimeReconstructionforAgentSk.md
Saved: 2026-08-10 23:24
Source: 2026-08-09_16-18-13Z_Evidence_CalibratedRuntimeReconstructionforAgentSk.md
Model: None

---

## Summary  
The paper introduces Skill Runtime Intelligence (SRI), a passive runtime‑intelligence system that reconstructs the supported lifecycle stages of reusable “Skill” instructions across heterogeneous coding agents while marking unsupported stages as unknown. By separating immutable events, deterministic relations, inferred diagnoses, and controlled outcomes into four evidence grades, SRI enables interpretable observability without overwriting underlying facts. The contribution is a unified framework—Run Panorama—that logs these evidence grades and supports trace import/export via OTLP or HTTP, allowing developers to qualify adapters based on concrete event patterns rather than abstract success/failure scores.

## Key Contributions  
- [Finding 1] Skill Runtime Intelligence reconstructs supported Skill‑lifecycle stages across heterogeneous harnesses while preserving unsupported stages as unknown.  
- [Finding 2] The Run Panorama system distinguishes four evidence grades (immutable events, deterministic relations, inferred diagnoses, controlled outcomes) and adapters expose three distinct semantics: no runs, complete runs without failure‑like events, or failure‑like events in every operational‑failure/clean session.  
- [Finding 3] Executable adapter qualification reveals that event presence is not a proxy for boundary fidelity; composite exact scores mask distinct errors, and model explanations must not overwrite deterministic facts.

## Methodology  
The authors deployed SRI on six frozen repository profiles using three coding agents under seven clean or fault‑injected conditions. Each execution preserved the source worktree and correlated to exactly one session. Trace data were exported via OTLP/HTTP for inspection. The Run Panorama records immutable events, deterministic relations, inferred diagnoses, and controlled outcomes with four evidence grades, enabling passive reconstruction of skill activity without modifying the agents.

## Results  
All 126 executions preserved source worktrees and each mapped to a single session. Adaptors displayed three semantics across sessions: no Skill runs; complete runs but no failure‑like events; or failure‑like events in every operational‑failure/clean session. In a seven‑template diagnostic study, the Raw view emitted a failure status on all 18 clean cases, whereas Panorama emitted none, indicating that deterministic facts were not overwritten by model explanations. A known‑rule graph conformed to 126/126 frozen contracts, while a second model completed only 228/378 calls.

## Significance  
SRI provides executable adapter qualification by grounding success/failure judgments in concrete event evidence rather than opaque scores. This clarifies skill boundaries across heterogeneous agents, reduces false positives from composite exact metrics, and improves observability pipelines through standardized trace export formats.

## Related Concepts  
Skill Runtime Intelligence, Run Panorama, evidence grades (immutable events, deterministic relations, inferred diagnoses, controlled outcomes), observable adapters, trace import/export via OTLP/HTTP, event presence vs. boundary fidelity, composite exact scores, deterministic facts.

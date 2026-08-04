# Summary: 2026-08-03_17-03-19Z_SWE_Touch_BenchmarkingCodingAgentsWhenUsersTouchth.md
Saved: 2026-08-04 00:50
Source: 2026-08-03_17-03-19Z_SWE_Touch_BenchmarkingCodingAgentsWhenUsersTouchth.md
Model: None

---

## Summary  
The paper addresses the gap where coding agents are evaluated in isolation, yet real‑world collaboration involves users editing code concurrently within a shared workspace. To stress‑test this setting, the authors introduce SWE‑Touch, a framework that injects plausible Counter‑Edits—conflicting modifications to task‑relevant code—together with user messages at appropriate moments. By mining task‑critical regions across multiple repair trajectories and generating these edits, they create a benchmark that forces agents to detect and reconcile workspace changes. The study evaluates nine coding models on SWE‑bench Verified and longer benchmarks such as SWE‑bench Pro and DeepSWE. Findings show an average 7.7 percentage point drop in resolve rates due to limited state awareness.

## Key Contributions  
- Counter‑Edit framework and its generation pipeline that mines task‑critical regions from repair trajectories.  
- Demonstration of a 7.7 percentage point reduction in average resolution across all models on SWE‑bench Verified, with similar degradation observed on longer‑horizon tasks.  
- Identification of three critical capabilities—workspace change detection, edit reconciliation, and behavior verification—as essential for collaborative coding agents.

## Methodology  
The authors construct SWE‑Touch by extracting task‑relevant code regions from multiple repair trajectories using the SWE‑bench Verified dataset; a separate User Patch Generator creates plausible edits that conflict with the original solution; these edits are injected into the agent’s workspace at points where user messages would normally appear, simulating real‑time collaborative editing.

## Results  
On SWE‑bench Verified, the average resolve rate falls by 7.7 percentage points compared to baseline models; similar degradation is observed on both SWE‑bench Pro and DeepSWE. Trajectory analysis reveals that agents often retain old code or replace it without re‑inspection, indicating a failure to reconcile conflicting edits with the evolving task.

## Significance  
This work demonstrates that strong autonomous performance does not guarantee effective shared‑workspace collaboration; detecting workspace changes, reconciling conflicting edits, and verifying affected behavior are key challenges for future optimization. The findings guide researchers toward agents that maintain coherent state awareness in dynamic coding environments.

## Related Concepts  
- Shared workspace collaboration  
- Counter‑Edit benchmark  
- SWE‑bench Verified / Pro / DeepSWE  
- Workspace state awareness  
- Edit reconciliation  
- Task verification

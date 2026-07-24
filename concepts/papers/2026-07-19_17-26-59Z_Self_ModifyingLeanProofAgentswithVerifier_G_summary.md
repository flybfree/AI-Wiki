# Summary: 2026-07-19_17-26-59Z_Self_ModifyingLeanProofAgentswithVerifier_Grounded.md
Saved: 2026-07-24 00:12
Source: 2026-07-19_17-26-59Z_Self_ModifyingLeanProofAgentswithVerifier_Grounded.md
Model: None

---

## Summary  
The paper proposes a self‑modifying Lean proof agent that evolves both its internal workflow and an associated verification benchmark through coevolution. By embedding the proof process inside a trusted runtime, the system can rewrite prompts, tools, and task distributions while guaranteeing that every generated proof remains verifiable under a snapshot of Lean. The authors evaluate this coevolving trajectory against a fixed‑benchmark baseline on a held‑out miniF2F test split, demonstrating substantial gains in solve rates.  

## Key Contributions  
- [Finding 1] A self‑evolving Lean proof agent that rewrites its prompt and tool usage while preserving a verified proof context.  
- [Finding 2] A mastery‑throttled curriculum update where the champion agent only faces harder obligations after mastering the current level, enabling progressive difficulty scaling.  
- [Finding 3] A single‑anchor recalibration that re‑runs the champion on the updated benchmark to keep scores comparable across generations.  

## Methodology  
The authors construct a minimal trusted runtime that wraps a mutable workspace containing the proof workflow, prompts, and tools. The agent operates within this sandbox, producing machine‑readable Lean contexts for each attempt. Between generations, the highest‑scoring champion is selected to drive curriculum updates: it generates new harder tasks, which are inserted into the benchmark; then the champion’s performance on the revised benchmark is measured. This coevolution loop repeats 15 times, with a fixed‑benchmark baseline (seed and best static agent) serving as control. The evaluation uses the miniF2F test split to compute solve rates.  

## Results  
Over 15 active generations, the coevolving system achieves a held‑out solve rate of **45.1 %**, compared with **12.7 %** for the seed agent and **32.0 %** for the best fixed‑benchmark agent. The improvement is attributed to the dynamic difficulty scaling and continuous verification grounding that keep the benchmark aligned with the evolving agent.  

## Significance  
The work shows that self‑modifying agents can outperform static baselines when their evolution is guided by a verifier‑grounded, coevolving benchmark. This approach bridges code‑level self‑evolution research and formal verification, offering a template for other proof assistants and automated reasoning systems.  

## Related Concepts  
- Lean proof assistant (Lean)  
- Self‑modifying agents / code‑level evolution  
- Verifier‑grounded benchmark coevolution  
- Mastery‑throttled curriculum learning  
- Single‑anchor recalibration  
- MiniF2F benchmark suite

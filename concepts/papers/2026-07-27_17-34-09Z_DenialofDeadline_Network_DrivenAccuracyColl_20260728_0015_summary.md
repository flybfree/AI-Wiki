# Summary: 2026-07-27_17-34-09Z_DenialofDeadline_Network_DrivenAccuracyCollapseinD.md
Saved: 2026-07-28 00:15
Source: 2026-07-27_17-34-09Z_DenialofDeadline_Network_DrivenAccuracyCollapseinD.md
Model: None

---

## Summary  
The paper investigates how the coordination layer that merges predictions from a fast‑path and a slow‑path inference pipeline can be exploited by shaped workload attacks, causing “denial of deadline” where benign users’ slow‑path predictions are delayed beyond their latency deadlines. This forces the merger to discard those predictions, resulting in accuracy collapse without requiring access to model weights or victim data. The authors demonstrate this attack on a two‑tier edge‑cloud multi‑object tracking system used for autonomous driving. Their experiments show that burst‑shaped requests can push p99 latency from 92 ms to about 2 seconds, eliminating the cloud inference benefit.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Shaped workload attacks (e.g., Yo‑Yo bursts) can cause slow‑path predictions to miss their latency deadlines without any access to model weights or victim data.  
- [Finding 2] The merger discards delayed slow‑path predictions, leading to a measurable loss of tracking quality expressed in HOTA points.  
- [Finding 3] The severity of accuracy degradation varies with the targeted video intervals; rare classes such as stop signs can lose up to roughly half their pre‑attack prediction accuracy.

## Methodology  
The authors abstracted the inference pipeline into three components: a fast path that returns predictions quickly, a slow path that runs higher‑accuracy cloud models on remote hardware, and a coordination layer consisting of a router that invokes the slow path and a merger that decides whether to incorporate its results. To study the vulnerability, they simulated a realistic two‑tier edge‑cloud multi‑object tracking system under normal traffic and then injected 4 000 burst‑shaped requests designed to saturate shared resources on the slow path. They measured p99 latency and HOTA accuracy before and after the attack to quantify the impact.

## Results  
In the simulation, the benign p99 latency rose from 92 ms to approximately 2 seconds when the burst attacks were active, effectively nullifying the cloud inference benefit. The average HOTA dropped by about 7.0 points, with degradation ranging from 2.0 to 18.7 points depending on which video intervals were targeted. Notably, stop‑sign class accuracy fell by roughly 50 % compared with the pre‑attack baseline.

## Significance  
These findings reveal that coordination mechanisms in distributed inference pipelines expose a new attack surface: workload attacks can degrade both latency and prediction quality without compromising privacy or model confidentiality. The results motivate research into defenses for routing, merging, scheduling, and resource isolation to protect these emerging architectures.

## Related Concepts  
fast path, slow path, coordination layer (router + merger), latency deadline, shaped workload attacks (Yo‑Yo bursts), contention on shared resources, accuracy collapse, multi‑object tracking, HOTA metric, edge‑cloud inference.

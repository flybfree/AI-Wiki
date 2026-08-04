# Summary: 2026-07-31_20-18-25Z_LoopsBench_FromHarnessEngineeringtoLoopEngineering.md
Saved: 2026-08-03 20:20
Source: 2026-07-31_20-18-25Z_LoopsBench_FromHarnessEngineeringtoLoopEngineering.md
Model: None

---

## Summary  
LoopsBench is a long‑horizon benchmark designed to evaluate coding agents in the context of sustained loop engineering, moving beyond isolated harness tasks toward full program development cycles. It treats each task as a dependency DAG composed of testable units linked by source‑evidence‑backed prerequisite edges. The framework releases tests at the ready frontier and retains completed nodes as regression obligations, providing a realistic view of long‑term execution. By pairing frontier coding agents with loop implementations, LoopsBench measures both success rates and plan recovery quality.

## Key Contributions  
- [Finding 1] Introduces LoopsBench as a comprehensive benchmark for loop engineering in coding agent evaluation.  
- [Finding 2] Provides 112 tasks spanning eight programming languages and nine domains, each modeled as a source‑evidence DAG with flow‑aware runtime releases.  
- [Finding 3] Demonstrates that the strongest configuration (Opus‑4.7 + Claude Code with outer continuation) resolves only about 25 % of tasks, while plan recovery captures only part of the prerequisite DAG and regression events persist across loop profiles.

## Methodology  
The authors approached the problem by constructing a dependency graph where each node is an independently testable development unit and edges represent source‑evidence prerequisites. Tasks are generated from authentic sources, ensuring linguistic and functional diversity. The flow‑aware runtime releases tests only when all upstream nodes are ready, while completed nodes become regression obligations that must be preserved in later iterations. Evaluation pairs coding agents with widely used loop implementations to measure both task resolution and plan recovery.

## Results  
LoopsBench contains 112 tasks built from more than 5,300 development units across eight languages and nine domains. The best‑performing configuration (Opus‑4.7 paired with Claude Code using outer continuation) resolves approximately 25 % of the benchmark tasks. However, recovered plans capture only a fraction of the source‑recovered prerequisite DAG, and regression events remain visible throughout loop profiles, indicating incomplete plan adherence.

## Significance  
LoopsBench addresses the shift from harness engineering to full loop engineering in coding agent deployment, offering a realistic long‑horizon evaluation that captures test release dynamics and regression obligations. By providing open‑source data—including tasks, development units, and executable tests—the benchmark enables reproducible research and community contributions.

## Related Concepts  
- Harness engineering vs. loop engineering  
- Dependency DAG (directed acyclic graph) modeling of task prerequisites  
- Regression obligations in long‑horizon execution  
- Flow‑aware runtime that releases tests only when ready  
- Coding agent evaluation frameworks  
- Long‑horizon benchmarking for software development

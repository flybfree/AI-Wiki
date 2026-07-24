# Summary: 2026-07-23_11-31-38Z_ICAE_Bench_EvaluatingCodingAgentsasInteractiveProj.md
Saved: 2026-07-24 02:42
Source: 2026-07-23_11-31-38Z_ICAE_Bench_EvaluatingCodingAgentsasInteractiveProj.md
Model: None

---

## Summary  
The paper introduces ICAE‑Bench, a benchmark designed to evaluate coding agents in interactive project‑building scenarios where requirements are initially vague and evolve through user interaction. It shifts evaluation from static, fully specified tasks to dynamic, repository‑level construction that mimics real‑world vibe‑coding workflows. By grounding each task on an existing open‑source repository with executable behavior, ICAE‑Bench provides a realistic yet reproducible testing environment for agents tasked with turning fuzzy product intent into functional software.

## Key Contributions  
- **Realistic Fuzzy Requirements**: Tasks are derived from precise open‑source repositories, eliminating ambiguity while preserving genuine user constraints.  
- **User Agent Data**: A standardized data pipeline supplies hidden constraints to the simulated User Agent without inventing new requirements or leaking implementation details.  
- **Multi‑dimensional Diagnostics**: Evaluation combines black‑box functional tests with metrics for semantic/API similarity, structural fidelity, design quality, and interaction quality.

## Methodology  
ICAe‑Bench constructs each evaluation round by selecting a real open‑source project that exhibits the intended behavior, then defines an initial fuzzy requirement. The automated User Agent iteratively asks clarifying questions, receives user responses encoded in User Agent Data, and guides the coding agent to produce code updates. After each iteration, the system runs standardized black‑box tests and computes the six diagnostic scores, ensuring reproducibility across runs.

## Results  
Experiments on ten representative repositories show that agents trained on ICAE‑Bench achieve higher functional correctness (average 78 % pass rate) than comparable baselines (62 %). Semantic similarity scores improve by 15 %, and interaction quality metrics rise from 4.2 to 5.0 on a 6‑point scale, indicating better alignment with user intent.

## Significance  
ICAe‑Bench addresses the gap between existing benchmarks that test static code completion and the emerging need for agents that collaboratively build projects under ambiguous, evolving requirements. By providing a unified framework, it enables fair comparison of coding agents’ planning, clarification, tool use, debugging, and repository construction abilities.

## Related Concepts  
vibe‑coding, interactive project building, open‑source repositories, black‑box testing, multi‑dimensional evaluation metrics, automated user agent simulation.

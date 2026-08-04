# Summary: 2026-08-01_18-17-47Z_AgentSLABench_EvaluatingandBenchmarkingAgenticSyst.md
Saved: 2026-08-03 20:31
Source: 2026-08-01_18-17-47Z_AgentSLABench_EvaluatingandBenchmarkingAgenticSyst.md
Model: None

---

## Summary  
AgentSLABench introduces a resource‑aware evaluation framework for autonomous AI agents that measures not only correctness but also latency, cost, compute, memory, and network usage against declared budgets. The authors create 16 task environments across five core categories (multi‑hop QA, retail substitution, code generation, web shopping, travel planning) and eleven extended tasks, each isolated in Docker containers with sealed test sets and SHA256 hashes. A standardized profiling protocol mirrors tools like perf and pprof while adding a correctness dimension to the profile. By profiling both general‑purpose baselines (ReAct, PlanAndSolve, Reflexion, CoT, Random) and four task‑specialized agents, the study reveals stark performance trade‑offs under resource constraints.

## Key Contributions  
- [Finding 1] Specialized agents achieve 100 % success on three core tasks (fact_qa, web_shopping, travel_planning) while general baselines fail entirely on four of five domain tasks.  
- [Finding 2] The Efficiency‑Adjusted Success Rate (EASR) quantifies viability by weighting success against resource consumption relative to declared budgets, showing that high accuracy at unbounded cost is not production‑viable.  
- [Finding 3] Full infrastructure, sealed test sets, and profiling results are released to enable reproducible, resource‑aware agent evaluation.

## Methodology  
The authors built a comprehensive benchmark comprising 16 environments (5 core + 11 extended) each with isolated Docker containers, explicit CPU/memory/time/network budgets, and sealed test sets whose SHA256 hashes guarantee integrity. A standardized profiling protocol records latency, compute, memory, network usage, and correctness per task execution. The framework profiles five general‑purpose agents (ReAct, PlanAndSolve, Reflexion, CoT, Random) alongside four domain‑specific agents, ensuring a balanced comparison across baseline and specialized approaches.

## Results  
Specialized agents achieve 100 % success on fact_qa, web_shopping, and travel_planning; retail substitution and code generation show 66.7–83.3 % success rates. General‑purpose baselines fail entirely on four of the five core tasks. The EASR metric demonstrates that agents with high accuracy but excessive resource usage score poorly when budgets are respected, highlighting a critical gap between benchmarked performance and real‑world deployment constraints.

## Significance  
AgentSLABench provides the first multi‑dimensional profile of autonomous systems under explicit resource limits, moving evaluation beyond raw accuracy to include latency, cost, compute, memory, and network impact. This framework informs realistic design decisions, guides trade‑off analysis, and opens a reproducible benchmark for future agentic research.

## Related Concepts  
- Resource constraints (CPU, memory, time, network)  
- Efficiency‑Adjusted Success Rate (EASR)  
- Profiling tools (perf, pprof, cProfile) extended with correctness dimension  
- Docker containers and sealed test sets for reproducible benchmarking  
- Core tasks: multi‑hop QA, retail substitution, code generation, web shopping, travel planning

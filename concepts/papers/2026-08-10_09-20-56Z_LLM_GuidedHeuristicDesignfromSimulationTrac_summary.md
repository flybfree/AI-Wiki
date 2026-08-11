# Summary: 2026-08-10_09-20-56Z_LLM_GuidedHeuristicDesignfromSimulationTraces_ACas.md
Saved: 2026-08-10 23:44
Source: 2026-08-10_09-20-56Z_LLM_GuidedHeuristicDesignfromSimulationTraces_ACas.md
Model: None

---

## Summary  
The paper proposes an LLM‑guided heuristic design framework that leverages repeated simulations and event‑level trace analysis to improve policies for dynamic production and AGV scheduling beyond traditional black‑box optimization. By extracting diagnostic evidence from the lowest‑scoring simulation replication, a manager LLM formulates bottleneck hypotheses while editing agents generate parallel code revisions; only policies with demonstrable improvement are retained as best‑so‑far candidates. This iterative process integrates an LLM revision step between evaluation batches under a fixed policy control, yielding targeted policy enhancements that surpass conventional methods.

## Key Contributions  
- [Finding 1] An LLM‑guided heuristic design framework that uses simulation traces to diagnose and guide targeted policy improvements.  
- [Finding 2] The integration of event‑level trace analysis with parallel LLM editing agents to produce code‑level revisions between evaluation batches.  
- [Finding 3] Demonstrated superiority over rolling‑MILP, rule‑based, and metaheuristic baselines across multiple optimization runs and fault conditions.

## Methodology  
The authors treat the simulator as a black box but augment it with repeated replications of each incumbent policy. After each run, the lowest‑scoring replication generates an event‑level trace that is accessible to a manager LLM which formulates bottleneck hypotheses (e.g., charging constraints, AGV assignment inefficiencies). Editing agents then generate parallel code modifications addressing these hypotheses. A fixed policy controls all simulation executions, and the best‑so‑far selection retains only policies with measurable improvement. This cycle repeats across evaluation batches, with LLM revisions occurring between them.

## Results  
Across five independent optimization runs using Gemini‑3.1‑Pro, the framework achieved a mean score of 77.51 on a 0‑100 scale. In the best run, trace‑based diagnoses motivated proactive charging, distance‑aware AGV assignment, and rebalanced dispatch priorities, raising the best‑so‑far mean from 62.49 to 78.61. On 100 matched seeds, the final policy outperformed all baselines on every seed and retained its advantage under random faults without re‑optimization. Even with longer horizons or variable interarrival times, the policies remained superior.

## Significance  
This work demonstrates that simulation traces can serve as a diagnostic source for complex stochastic scheduling problems, enabling targeted code‑level improvements that surpass traditional optimization methods. It bridges black‑box evaluation with interpretable policy engineering, offering a scalable path to better SBO in dynamic production environments where interpretability and robustness are critical.

## Related Concepts  
Simulation‑Based Optimization (SBO), event‑level trace analysis, LLM‑guided heuristic design, best‑so‑far selection, bottleneck hypothesis generation, parallel code editing agents, stochastic scheduling, AGV dispatching, discrete‑event simulation.

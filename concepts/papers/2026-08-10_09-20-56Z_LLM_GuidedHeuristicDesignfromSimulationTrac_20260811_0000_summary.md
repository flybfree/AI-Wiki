# Summary: 2026-08-10_09-20-56Z_LLM_GuidedHeuristicDesignfromSimulationTraces_ACas.md
Saved: 2026-08-11 00:00
Source: 2026-08-10_09-20-56Z_LLM_GuidedHeuristicDesignfromSimulationTraces_ACas.md
Model: None

---

## Summary  
The paper proposes an LLM‑guided heuristic design framework that leverages event‑level traces from repeated simulations to diagnose and improve policies in dynamic production and AGV scheduling problems. By moving beyond the black‑box nature of traditional simulation‑based optimization (SBO), it uses trace analysis to pinpoint specific policy failures, then iteratively refines code through LLM‑driven revisions while a fixed controller runs new simulations. This hybrid approach yields measurable score gains across multiple optimization runs compared with conventional baselines.

## Key Contributions  
- [Finding 1] Simulation traces provide targeted diagnostic insights that reveal why an incumbent policy scores low, enabling precise hypothesis generation about bottlenecks in the scheduling logic.  
- [Finding 2] An iterative LLM revision loop—manager agents formulate hypotheses from trace evidence and editing agents generate parallel code‑level changes—improves policies without re‑optimizing the entire problem each time.  
- [Finding 3] The framework consistently outperforms rolling‑MILP, rule‑based, and metaheuristic methods on every seed and retains its advantage under random faults without requiring additional re‑optimization.

## Methodology  
The authors built a discrete‑event simulation of dynamic production with stochastic interarrival times to model AGV scheduling. For each incumbent policy they executed multiple simulations, collected the lowest‑scoring trace as diagnostic evidence, fed it into an LLM manager that identified bottleneck hypotheses, and then used editing agents to produce parallel code revisions. After each revision batch a fixed policy controlled new simulation runs; only improvements were retained in the best‑so‑far selection process. This cycle repeats until convergence.

## Results  
Across five independent optimization runs with Gemini‑3.1‑Pro, the final mean scores averaged 77.51 out of 100. The highest‑scoring run improved from a baseline of 62.49 to 78.61 by applying trace‑driven diagnoses that motivated proactive charging, distance‑aware AGV assignment, and rebalanced dispatch priorities. On 100 matched seeds the best policy beat all baselines on every seed and maintained its lead under random faults without further re‑optimization. Ablations showed that removing either parallel candidate generation or trace‑database access reduced final mean scores.

## Significance  
This work shows that simulation traces can guide targeted, code‑level improvements in complex SBO settings, offering a more interpretable and efficient alternative to black‑box optimization—particularly valuable for real‑time scheduling where frequent re‑optimizations are costly. The approach bridges the gap between high‑level policy design and low‑level implementation, enabling continuous improvement without sacrificing performance.

## Related Concepts  
- Simulation‑based optimization (SBO)  
- Discrete‑event simulation  
- Event trace analysis  
- LLM‑driven heuristic design  
- Bottleneck hypothesis generation  
- Parallel code editing agents  
- Best‑so‑far selection  
- Stochastic scheduling  
- Rolling MILP  
- Rule‑based heuristics  
- Metaheuristics

# Summary: 2026-08-06_15-43-31Z_MicroEvo_Knowledge_GuidedLLMSamplingforEfficientMi.md
Saved: 2026-08-06 22:19
Source: 2026-08-06_15-43-31Z_MicroEvo_Knowledge_GuidedLLMSamplingforEfficientMi.md
Model: None

---

## Summary  
Microarchitecture design space exploration is hampered by expansive search spaces and expensive PPA evaluations, leaving only a limited simulation budget for decision‑making. This paper introduces **MicroEvo**, a knowledge‑guided framework that couples off‑the‑shelf large language models with Monte Carlo Tree Search (MCTS) to explore multi‑objective microarchitecture optimization more efficiently. MicroEvo integrates LLM‑driven evolutionary operators, a Pareto‑aware tree policy, an active knowledge accumulation mechanism, and state‑aware directives that adapt online. Experiments show that MicroEvo improves the quality of the Pareto front by up to 36.2 % over NSGA‑II while achieving ten‑fold higher search efficiency.

## Key Contributions  
- [Finding 1] MicroEvo introduces a knowledge‑guided Monte Carlo Tree Search that leverages LLMs to generate evolutionary operators tailored to microarchitectural dependencies.  
- [Finding 2] It employs a Pareto‑aware tree policy that balances contribution to the Pareto front with diversity, preventing premature convergence and wasted evaluations.  
- [Finding 3] The framework includes an active knowledge accumulation mechanism that extracts optimization insights from previous simulations and reuses them in subsequent search steps.

## Methodology  
MicroEvo addresses the problem by first constructing a large design‑space graph where each node represents a microarchitectural configuration. An LLM generates candidate evolutionary operators—such as gene crossover, mutation, or recombination—that respect known hardware constraints and performance trade‑offs. These operators are injected into an MCTS tree whose policy is Pareto‑aware: it selects branches that both advance the objective functions and maintain diversity across the search frontier. A separate knowledge accumulator stores successful design insights (e.g., effective parameter ranges) and feeds them back to the LLM, reducing redundant evaluations. Finally, state‑aware directives dynamically adjust the search depth or exploration rate based on real‑time performance feedback.

## Results  
The authors benchmark MicroEvo against NSGA‑II on a set of microarchitectural trade‑off problems (latency vs. power). MicroEvo’s Pareto front quality is 36.2 % higher, and the number of PPA evaluations required drops to roughly one‑tenth that of NSGA‑II—approximately a ten‑fold efficiency gain. Moreover, the framework scales well to an industrial‑scale core design, demonstrating robust performance across multiple generations.

## Significance  
By integrating LLMs with MCTS and adding knowledge‑driven mechanisms, MicroEvo dramatically reduces the costly PPA budget required for microarchitecture exploration while delivering superior multi‑objective solutions. This approach enables designers to explore vast design spaces within realistic simulation limits, accelerating time‑to‑market for next‑generation processors.

## Related Concepts  
- Microarchitecture design space exploration  
- Multi‑objective optimization (Pareto front)  
- Monte Carlo Tree Search (MCTS)  
- Large Language Models (LLMs)  
- Evolutionary computation  
- Knowledge‑guided search  
- Active learning for optimization  
- State‑aware policies

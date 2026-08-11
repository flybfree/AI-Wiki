# Summary: 2026-07-27_06-48-04Z_HELIOS_AnLLM_DrivenAutonomousIndirectTrajectoryOpt.md
Saved: 2026-07-27 22:54
Source: 2026-07-27_06-48-04Z_HELIOS_AnLLM_DrivenAutonomousIndirectTrajectoryOpt.md
Model: None

---

## Summary  
Low‑thrust trajectory optimization for deep‑space missions is hampered by three practical bottlenecks: deriving transversality conditions case‑by‑case, rewriting code for each dynamics model, and the sensitivity of shooting equations to initial guesses. The authors introduce HELIOS (Heuristic Engine for Low‑thrust Interplanetary Optimization System), an autonomous agent that leverages a large language model to perform PMP symbolic derivation, SymPy verification, C++ shooting‑code generation, and numerical solution from a natural‑language description of the problem. This work unifies constraint handling, supports multiple non‑standard dynamics, and provides a rule set for common derivation pitfalls, enabling fully automated trajectory design without human intervention.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A constraint‑adaptive derivation framework that converts arbitrary constraints into \(\psi(x,p)=0\) form and automatically generates stationarity conditions for free parameters such as gravity‑assist turning angles.  
- [Finding 2] A dynamics‑adaptive four‑module code generator that produces C++ shooting code for diverse propulsion models (solar sail, J₂ perturbation) without altering a single template.  
- [Finding 3] A general derivation rule set covering critical error‑prone points in PMP derivations, which is integrated into the LLM pipeline to ensure correctness.

## Methodology  
HELIOS receives a problem statement written in natural language (e.g., “optimize a multi‑leg stay transfer with solar sail propulsion”). The LLM first parses the description and selects the appropriate physics model. It then invokes SymPy to symbolically derive the PMP stationarity equations, automatically handling constraint adaptation and free parameters. The derived system is compiled into C++ shooting code using the four‑module generator, which respects the chosen dynamics (solar sail, J₂). Finally, HELIOS solves the shooting equations numerically with an adaptive initial guess strategy to mitigate sensitivity issues.

## Results  
The authors evaluated HELIOS on 11 progressive test scenarios ranging from a simple rendezvous (8 variables) to complex multi‑leg stay transfers (48 variables), gravity‑assist trajectories (17 variables), and solar‑sail minimum‑time transfers (8 variables). All 11 compilations succeeded, achieving a 100 % success rate. A multi‑model comparison using eight open‑source LLMs produced total scores between 250 and 905, confirming a positive correlation between model scale and derivation capability.

## Significance  
HELIOS eliminates the manual, error‑prone steps of low‑thrust trajectory optimization, dramatically reducing development time for interplanetary mission design. By automating PMP derivations and code generation, it improves reliability and enables rapid exploration of unconventional propulsion concepts such as solar sails.

## Related Concepts  
Pontryagin’s Minimum Principle (PMP), indirect trajectory optimization, symbolic derivation with SymPy, C++ shooting‑code generation, large language models, constraint adaptation, gravity‑assist turning angles, solar sail dynamics, J₂ perturbation, multi‑leg stay transfers.

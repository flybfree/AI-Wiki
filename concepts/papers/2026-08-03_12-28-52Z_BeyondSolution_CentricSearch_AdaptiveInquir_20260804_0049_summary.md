# Summary: 2026-08-03_12-28-52Z_BeyondSolution_CentricSearch_AdaptiveInquiryandKno.md
Saved: 2026-08-04 00:49
Source: 2026-08-03_12-28-52Z_BeyondSolution_CentricSearch_AdaptiveInquiryandKno.md
Model: None

---

## Summary  
The paper seeks to replace the traditional solution‑centric search paradigm used by LLM agents in autonomous machine learning (ML) engineering with an information‑driven approach that treats knowledge acquisition and revision as the core of decision making. By framing the system’s understanding as an evolving “information state,” it enables more efficient, budget‑aware exploration without prematurely fixing solutions. The authors introduce Iris, a query‑revision loop that autonomously probes critical unknowns (epistemic actions) while maintaining a structured knowledge base that can be updated with new evidence. This paradigm yields measurable gains in performance and flexibility for long‑horizon research tasks.

## Key Contributions  
- **Information paradigm**: The authors replace solution‑centric search with an information‑state driven framework, shifting focus from how solutions are built to how information is gathered and managed.  
- **Iris system**: They implement a concrete inquiry‑revision loop that generates local action plans, uses epistemic actions to probe decision‑critical unknowns, and synthesizes observations into task knowledge composed of revisable claims with explicit scope and status.  
- **Empirical superiority**: Iris achieves the highest any‑medal rate (64.9 %) on MLE‑Bench within a 12‑hour budget and demonstrates cross‑domain generalization across four tasks spanning harness engineering and model post‑training.

## Methodology  
The authors approached the problem by first defining an “information state” that encapsulates what is known about the task at any moment. From this state, Iris creates local action plans that prioritize epistemic actions—queries that target unknowns without altering retained solutions. Observations from experiments are aggregated into a structured knowledge base: each claim has a scope and a status (e.g., tentative, confirmed). As new evidence arrives, the system updates these claims and constructs decision contexts by combining raw data, summaries, or high‑level task knowledge at the appropriate granularity.

## Results  
On the MLE‑Bench benchmark, Iris reaches a 64.9 % any‑medal rate within a 12‑hour budget, outperforming all compared systems. The authors also report that Iris generalizes across four distinct tasks—two related to harness engineering and two to model post‑training—showing robust performance beyond the specific benchmark.

## Significance  
This work matters because long‑horizon autonomous research demands efficient use of limited computational resources while handling interdependent decisions. By decoupling solution construction from information gathering, the information paradigm reduces wasted effort on dead ends and enables continuous knowledge revision. The results demonstrate that such a framework can deliver superior performance and adaptability in real‑world ML engineering scenarios.

## Related Concepts  
- Information paradigm  
- Epistemic actions (queries that probe unknowns)  
- Task knowledge with revisable claims  
- Query‑revision loop  
- Autonomous machine learning engineering  
- MLE‑Bench benchmark

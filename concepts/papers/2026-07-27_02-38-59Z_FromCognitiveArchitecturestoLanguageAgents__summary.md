# Summary: 2026-07-27_02-38-59Z_FromCognitiveArchitecturestoLanguageAgents_AMechan.md
Saved: 2026-07-28 00:01
Source: 2026-07-27_02-38-59Z_FromCognitiveArchitecturestoLanguageAgents_AMechan.md
Model: None

---

## Summary  
The paper conducts a mechanism‑level review that maps ten historical cognitive architectures to eight language‑agent runtime families and forty‑two contemporary systems, reconstructing each mechanism through state, control, transition, persistence, failure, learning, and resource governance. By separating evidence relations (E1–E4) from migration depth (D0–D4), the authors produce a landscape that highlights both convergent capabilities and persistent gaps in modern agents. The review shows that many adaptive features—such as memory, failure recovery, dynamic team selection, workflow search, skill induction, resource scheduling, and uncertainty‑conditioned action—have been operationalized independently rather than through documented inheritance. The strongest remaining opportunities lie in coupling these mechanisms into composable bundles.

## Key Contributions  
- [Finding 1] A distinctive‑mechanism catalog that links each cognitive architecture to its corresponding language‑agent runtime family, revealing lineage, convergence, and migration gaps.  
- [Finding 2] An auditable evidence‑depth framework (E1–E4 for code evidence, D0–D4 for migration depth) that quantifies how far a mechanism has been transferred from older systems to newer agents.  
- [Finding 3] A falsifiable agenda for testing the identified bundles as composable runtime invariants, enabling systematic evaluation of their composability.

## Methodology  
The authors reconstructed every mechanism by examining its state, control flow, transitions, persistence mechanisms, failure handling, learning processes, and resource governance. They then recorded two dimensions: evidence relation (whether the original code is directly reused) and migration depth (how many layers of abstraction separate the original from the current implementation). Using these metrics, they performed a closest‑baseline screening to identify which modern agents already combine multiple mechanisms into cohesive bundles.

## Results  
Modern language agents have independently operationalized substantial parts of adaptive memory, failure recovery, dynamic team selection, workflow search, skill induction, resource scheduling, and uncertainty‑conditioned action. The closest‑baseline analysis shows that GraSP already combines calibrated multi‑skill selection, typed compilation, verification, bounded repair, replanning, or ReAct fallback—closing one proposed gap. Five residual bundles remain: activation with latency and action utility; typed impasse with isolated substates and resolution compilation; bounded content competition with broadcast and admission learning; persistent intention with reconsideration and live method authority; and uncertainty with resource allocation, interruption, and stopping.

## Significance  
This systematic view of lineage, convergence, and migration gaps provides a falsifiable agenda for testing composable runtime invariants, helping researchers design language agents that truly inherit and extend cognitive architectures rather than merely re‑implementing features from scratch. By making the evidence depth and migration depth explicit, the framework supports reproducible benchmarking across generations of systems.

## Related Concepts  
Cognitive architectures; language agents; mechanisms (memory, planning, reflection, tool use); evidence relation (E1–E4); migration depth (D0–D4); runtime families; composable invariants; lineage analysis.

# Summary: 2026-08-10_10-23-42Z_Monotonicity_GuidedBottom_UpPetriNetDiscovery_TheS.md
Saved: 2026-08-11 00:01
Source: 2026-08-10_10-23-42Z_Monotonicity_GuidedBottom_UpPetriNetDiscovery_TheS.md
Model: None

---

## Summary  
The paper proposes a bottom‑up discovery method for process mining that leverages monotonicity to generate high‑quality Petri net models from raw event data, thereby avoiding the exponential explosion of candidate places. By allowing free‑choice constructs and long‑term dependencies to emerge organically, the approach complements top‑down tools such as the Inductive Miner while respecting resource constraints. The SPECpp framework implements concrete strategies for pruning and ranking these candidates, enabling rapid experimentation on both synthetic and real‑world datasets.

## Key Contributions  
- [Finding 1] A monotonicity‑guided bottom‑up discovery algorithm that systematically explores candidate places without assuming predefined sequence structures.  
- [Finding 2] The SPECpp framework, which implements pruning heuristics and ranking criteria to obtain high‑quality models under time and memory limits.  
- [Finding 3] Demonstration that the method can capture complex concurrency patterns, including free‑choice constructs, that are difficult for traditional top‑down methods.

## Methodology  
The authors start from a stream of event logs and generate all possible local place constructions that satisfy monotonicity constraints—i.e., each transition either adds or removes events in a way that preserves the net’s partial order. These candidate places are then combined into larger constructs, but the search space is limited by monotonic pruning: any combination violating monotonicity is discarded early. The framework iteratively refines the model using ranking functions that balance expressiveness against computational cost, allowing users to select models within a predefined time budget.

## Results  
Experimental evaluations on synthetic data sets show that SPECpp discovers models with comparable or superior expressive power to the Inductive Miner while completing in significantly less time (average 30 % faster). On two real‑life event streams, the method produced accurate Petri net representations of key process flows, and its ranking criteria reduced the number of evaluated candidate combinations by up to 85 %. The trade‑off between model quality and runtime remains within acceptable limits for typical process mining workloads.

## Significance  
By grounding discovery in monotonicity, SPECpp tackles the core challenge of combinatorial explosion while preserving the expressive power of Petri nets. This enables practitioners to obtain rich, accurate models without resorting to costly top‑down inference, making large‑scale process mining feasible and scalable for real‑time applications.

## Related Concepts  
- Process mining  
- Petri net modeling  
- Bottom‑up discovery vs. top‑down induction (e.g., Inductive Miner)  
- Monotonicity constraints in event streams  
- Concurrency and free‑choice constructs

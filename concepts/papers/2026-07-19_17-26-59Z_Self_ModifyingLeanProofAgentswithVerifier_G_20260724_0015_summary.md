# Summary: 2026-07-19_17-26-59Z_Self_ModifyingLeanProofAgentswithVerifier_Grounded.md
Saved: 2026-07-24 00:15
Source: 2026-07-19_17-26-59Z_Self_ModifyingLeanProofAgentswithVerifier_Grounded.md
Model: None

---

## Summary  
This paper introduces a self-modifying Lean proof agent that evolves both the agent and its benchmark through coevolution, aiming to improve formal mathematical reasoning beyond static provers. The system enables continuous refinement of proof workflows by dynamically adjusting task distribution based on performance, using a mastery-throttled curriculum within a trusted verification loop. Unlike prior approaches that optimize against fixed benchmarks, this work ensures that all self-evolving changes are grounded in Lean-verified outputs and machine-readable contexts. The coevolution process spans 15 generations, progressively increasing difficulty while maintaining comparability through recalibration.

## Key Contributions  
- [Finding 1] A self-modifying Lean proof agent is designed where the runtime remains fixed but the workspace—including prompts, tools, and proof workflows—is fully mutable, allowing real-time evolution of reasoning strategies.  
- [Finding 2] The system implements coevolution by having the highest-scoring agent (champion) revise its task distribution after mastering current levels, introducing harder obligations only when appropriate, while a recalibration re-runs the champion on an updated benchmark to stabilize performance metrics.  
- [Finding 3] All evolution is constrained within a Lean-grounded verification loop: every self-revision must produce proofs that are verifiable under a trusted snapshot and emit machine-readable proof contexts whose representation may evolve but whose correctness is enforced.

## Methodology  
The authors approached the problem by treating the proof workflow as an evolving system rather than a static pipeline. They introduced a small, trusted runtime that wraps a mutable workspace containing the agent’s prompts, tools, and proof state. The coevolution process begins with a seed agent and benchmark, then iteratively improves both: after each generation, the champion agent updates its task distribution using mastery-throttled curriculum learning—only adding harder tasks once current ones are solved reliably. A single-anchor recalibration re-runs the champion on the updated benchmark to ensure score comparability across generations. Crucially, all self-modifications are validated by a trusted verification snapshot that confirms Lean-verified proofs and machine-readable output.

## Results  
Over 15 active generations, the coevolving system achieved a 45.1% hold-out solve rate on the miniF2F test split, significantly outperforming the seed agent (12.7%) and the best fixed-benchmark agent (32.0%). This improvement demonstrates that verifier-grounded self-evolution can enhance Lean proof workflows by aligning agent evolution with actual reasoning performance under dynamic difficulty.

## Significance  
This work matters because it bridges the gap between code-level self-improvement and formal verification, showing that real-time adaptation in proof agents can be both effective and safe when grounded in verifiable outputs. By coevolving the agent and benchmark within a Lean-verified loop, the system avoids the pitfalls of unchecked evolution—such as breaking proof correctness or introducing non-verifiable changes—while still enabling continuous improvement. The results suggest that self-modifying agents can achieve substantial gains in formal reasoning when their evolution is tightly coupled to verification.

## Related Concepts  
- Lean Proof Agents: Systems that generate proofs using the Lean theorem prover, requiring both logical soundness and workflow coherence.  
- Self-Modifying Agents: AI systems that update their own code or behavior during operation.  
- Verifier-Grounded Benchmark Coevolution: A process where an agent and its benchmark evolve together based on performance under verification constraints.  
- Mastery-Throttled Curriculum Learning: An educational-inspired approach to difficulty scheduling in learning systems.  
- Lean-Verifiable Outputs: Proofs that are both syntactically correct (according to Lean) and semantically verifiable by a trusted system.

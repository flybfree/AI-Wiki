# Summary: 2026-08-08_13-07-51Z_NeurosymbolicDiscoveryofAlgebraicGraphConstruction.md
Saved: 2026-08-10 22:55
Source: 2026-08-08_13-07-51Z_NeurosymbolicDiscoveryofAlgebraicGraphConstruction.md
Model: None

---

## Summary  
The paper proposes a neurosymbolic agent that automatically discovers short algebraic descriptions of graphs given only raw adjacency data, aiming to replace brute‑force enumeration with symbolic constructions like Cayley graphs or lexicographic products. It introduces an agent that runs on a large language model interfaced with SageMath via MCP, iteratively proposing and testing graph constructions until they match the target exactly. The approach is tested on 100 highly symmetric two‑orbit graphs up to 25 vertices, all of which are solved without falling back to raw encodings. A concrete application demonstrates that the agent identifies a known counterexample to the Bernhart‑Kainen dispersability conjecture.

## Key Contributions  
- [Finding 1] Automatic discovery of algebraic graph constructions from adjacency data using a neurosymbolic agent.  
- [Finding 2] Demonstration that the agent can solve all 100 benchmark graphs without resorting to raw encodings, outperforming enumeration baselines.  
- [Finding 3] Identification of the smallest known counterexample to the Bernhart‑Kainen dispersability conjecture via an explicit algebraic construction.

## Methodology  
The authors built a general‑purpose agent that combines a large language model with SageMath through a Model Context Protocol (MCP) server. The agent receives the target graph as raw adjacency data, analyses it symbolically, proposes candidate constructions such as Cayley graphs or lexicographic products, and tests each via an exact isomorphism check performed by SageMath. Iteration continues until a construction matches the target exactly. No fine‑tuning of the language model is required; the symbolic verification ensures correctness.

## Results  
On the benchmark of 100 two‑orbit graphs (up to 25 vertices), the agent found verified algebraic constructions for every graph, achieving near‑perfect coverage while a template‑enumeration baseline reached only ~20% success. The catalog lookup failed entirely. For the 16‑vertex counterexample to the dispersability conjecture, the agent produced an explicit construction that enumeration missed. The method scales with symmetry; when symmetry is removed performance degrades.

## Significance  
This work bridges raw graph data and symbolic algebraic insight, enabling automated discovery of meaningful structural descriptions rather than mere existence proofs. It reduces reliance on exhaustive search, offers a reusable MCP bridge for future AI‑symbolic integration, and provides concrete examples where symbolic constructions outperform brute force, advancing both theoretical understanding and practical algorithm design.

## Related Concepts  
- Neurosymbolic computing: integration of neural networks with symbolic reasoning.  
- Algebraic graph theory: Cayley graphs, lexicographic products, dispersability.  
- Model Context Protocol (MCP): a framework for secure, programmatic communication between AI models and external tools.  
- Two‑orbit graphs: highly symmetric vertex‑transitive graphs used as a benchmark.

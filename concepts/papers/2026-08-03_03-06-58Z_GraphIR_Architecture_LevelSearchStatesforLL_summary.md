# Summary: 2026-08-03_03-06-58Z_GraphIR_Architecture_LevelSearchStatesforLLM_Guide.md
Saved: 2026-08-03 23:18
Source: 2026-08-03_03-06-58Z_GraphIR_Architecture_LevelSearchStatesforLLM_Guide.md
Model: None

---

## Summary  
The paper introduces **GraphIR**, an architecture‑aware intermediate representation that supplies a mutation‑aligned candidate state for large language model (LLM)–guided neural architecture search (NAS). By complementing executable programs with three complementary views—computation skeleton, mutation surface, and validity envelope—GraphIR resolves the mismatch between code‑level flexibility and the architectural states required for effective mutation. The authors demonstrate that this representation enables LLMs to reason about tensor dependencies, editable components, and compatibility constraints directly from program execution.

## Key Contributions  
- **Proposes GraphIR**, an IR with three views (computation skeleton, mutation surface, validity envelope) that provides a concrete architectural state for LLM‑driven NAS.  
- **Builds NAS‑Dependency**, a 120‑question benchmark covering six dependency‑reasoning dimensions to evaluate exact producer identification, propagation tracing, and interface risk detection.  
- **Shows superior search performance** on six downstream benchmarks (including CLRS) while keeping model size comparable and end‑to‑end NAS efficiency favorable when integrated into OpenEvolve.

## Methodology  
The authors first analyze executable neural programs to extract a *computation skeleton* that describes the tensor flow, then generate a *mutation surface* exposing editable modules and operations, and finally construct a *validity envelope* that captures interface contracts, propagated shapes, and downstream dependencies. These three views are combined into a single candidate state that LLMs can reason over during architecture evolution. The diagnostic tool NAS‑Dependency supplies 120 questions across six complementary dimensions to measure how well GraphIR identifies exact producer occurrences, traces dependency propagation, and diagnoses interface failures.

## Results  
GraphIR achieves the best overall search performance on the CLRS benchmark and several other standard NAS suites, outperforming prior LLM‑guided methods. The added representation does not increase model size substantially and maintains favorable end‑to‑end efficiency when used within OpenEvolve’s evolutionary framework. Diagnostic analysis of NAS‑Dependency confirms that GraphIR excels at pinpointing exact producer instances, tracing how tensor shapes propagate through the network, and flagging interface or failure risks.

## Significance  
By providing a mutation‑oriented architecture state, GraphIR creates an effective bridge between executable neural programs and high‑level LLM reasoning, enabling more reliable and efficient NAS driven by language models. This work advances the field of AI‑assisted system design by making architectural evolution more interpretable and controllable.

## Related Concepts  
Neural Architecture Search (NAS), Large Language Models (LLMs), Intermediate Representation (IR), Mutation Surface, Computation Skeleton, Validity Envelope, Tensor Dependencies, Interface Contracts, OpenEvolve.

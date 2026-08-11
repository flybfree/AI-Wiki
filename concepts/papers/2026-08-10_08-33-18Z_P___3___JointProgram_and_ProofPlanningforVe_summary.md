# Summary: 2026-08-10_08-33-18Z_P___3___JointProgram_and_ProofPlanningforVerifiedC.md
Saved: 2026-08-10 23:42
Source: 2026-08-10_08-33-18Z_P___3___JointProgram_and_ProofPlanningforVerifiedC.md
Model: None

---

## Summary  
Verified code generation seeks to produce both an executable program and a machine‑checkable proof that the program satisfies a formal specification. The current workflow treats these tasks sequentially—first generating code, then trying to prove it correct—which often leads to brittle repairs and high cost. This paper introduces **P³**, an LLM‑based agentic approach that jointly plans the program and its proof from a single unified plan derived from the specification. By developing implementation and proof scaffolds together, P³ avoids the back‑and‑forth between patching code and patching proofs. The authors evaluate this joint planning on Verina, AlgoVeri, and a new benchmark called Lean4Commit0 that extracts real‑world API requirements into Lean tasks.

## Key Contributions  
- **Joint Program-and-Proof Planning**: P³ first derives a unified plan that simultaneously specifies the program structure and its corresponding proof strategy.  
- **Agentic Workflow with Unified Scaffold**: The system generates both code and proof artifacts under this shared plan, integrating them into a single pipeline.  
- **Benchmark‑Specific Evaluation on Lean4Commit0**: The authors create Lean4Commit0, a library‑level benchmark that translates real‑world API requirements into Lean specifications, enabling fair comparison across four frontier LLM backends.

## Methodology  
The authors adopt an agentic design where the LLM acts as a coordinator: it receives a specification, generates a high‑level plan that outlines required data structures and algorithmic steps for both code and proof, then iteratively refines this plan while producing concrete implementation snippets and Lean formalizations. The unified scaffold ensures that any deviation in the program automatically triggers corresponding adjustments in the proof, preserving correctness throughout generation. Experiments are conducted by feeding the same specification to four state‑of‑the‑art LLMs (e.g., GPT‑4‑Turbo, Claude 2, Gemini 1.5, and Llama 3) using P³’s planning module versus a baseline that only produces code.

## Results  
Across Verina, AlgoVeri, and Lean4Commit0, P³ achieves the highest solve rate in every benchmark setting, improving performance by 4.6–11.2 percentage points compared with the strongest baseline. The per‑task API cost is reduced by up to roughly 40 % and wall‑clock time by about 37 % on the most difficult tasks. A targeted ablation further confirms that joint planning adds 3.3–8.3 solve points over a planless implementation‑only approach, isolating the benefit of simultaneous program‑proof synthesis.

## Significance  
Jointly planning programs and proofs addresses a fundamental bottleneck in verified code generation: the sequential, error‑prone pipeline. By embedding proof considerations into the generation process, P³ enables higher correctness rates with fewer resources, making automated verification more practical for real‑world software development. The work also demonstrates that structured, agentic LLMs can outperform purely code‑focused models when tasked with producing both executable and formal artifacts.

## Related Concepts  
- Verified Code Generation  
- LLM Agentic Workflows  
- Joint Program-and-Proof Planning  
- Lean4Commit0 Benchmark  
- Unified Scaffold for Implementation & Proof

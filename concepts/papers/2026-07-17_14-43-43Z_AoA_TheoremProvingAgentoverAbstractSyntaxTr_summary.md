# Summary: 2026-07-17_14-43-43Z_AoA_TheoremProvingAgentoverAbstractSyntaxTreeofRed.md
Saved: 2026-07-23 23:53
Source: 2026-07-17_14-43-43Z_AoA_TheoremProvingAgentoverAbstractSyntaxTreeofRed.md
Model: None

---

## Summary  
The paper proposes AoA, a theorem‑proving agent that operates on the abstract syntax tree (AST) of Minilang instead of serialized source text, thereby reducing token usage and API costs while improving proof generation speed and coverage. It tackles two problems: high token consumption caused by line‑number‑based state management and the lack of training data for the newly introduced Minilang language.

## Key Contributions  
- [Finding 1] AoA lifts the agent off concrete syntax onto an AST, enabling proofs to be emitted as JSON representations that are natively tool‑callable.  
- [Finding 2] It integrates proof operations and proof states into a unified proof tree, so each operation carries its own subgoal’s state without line‑number dependencies.  
- [Finding 3] Empirically AoA reduces API cost by 2.3–4.7×, token usage by 2.9–6.9×, tool calls by 3.9–8.9×, and proof generation time by 1.4–2.0× compared to Amazon’s Isabelle Agent on standard benchmarks.

## Methodology  
The authors designed AoA as a model that takes Minilang source code, parses it into an AST, then generates proofs as structured JSON trees using a tree‑edit model. The unified proof tree stores both operation metadata and subgoal states locally, eliminating the need for separate line‑number queries. Evaluation is performed by feeding Isabelle’s miniF2F and NTP4VC‑Pearl common success sets to Amazon’s Isabelle Agent, measuring input‑cache accounting, token count, tool calls, and runtime.

## Results  
Experimental results show that AoA achieves a 2.3–4.7× reduction in normalized API cost, uses 2.9–6.9× fewer tokens, makes 3.9–8.9× fewer tool calls, and runs 1.4–2.0× faster than the baseline Isabelle Agent. Moreover, AoA solves a larger fraction of problems on the harder verification benchmark (e.g., NTP4VC‑Pearl), indicating broader applicability.

## Significance  
By decoupling proof generation from line numbers and leveraging AST‑based JSON output, AoA mitigates the scalability bottleneck that plagues LLM‑driven theorem provers. This design opens the door for newer languages like Minilang to be integrated into automated verification pipelines without costly token overhead or manual state tracking.

## Related Concepts  
- Interactive Theorem Proving (ITP)  
- Abstract Syntax Tree (AST)  
- Token‑efficient prompting  
- Unified proof trees  
- LLM tool‑calling agents

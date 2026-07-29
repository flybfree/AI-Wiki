# Summary: 2026-07-28_04-41-13Z_ContractHIL_HLS_Contract_AlignedMulti_AgentWorkflo.md
Saved: 2026-07-28 22:30
Source: 2026-07-28_04-41-13Z_ContractHIL_HLS_Contract_AlignedMulti_AgentWorkflo.md
Model: None

---

## Summary  
ContractHIL‑HLS is a contract‑aligned multi‑agent workflow that extends LLM‑assisted high‑level synthesis (HLS) from kernel code to full system and board‑level closure by incorporating hardware‑in‑the‑loop feedback. The framework creates structured contracts from natural language requirements, renders them as persistent HTML, and executes the design on a HIL platform while continuously refining the model based on measured evidence. Evaluation shows measurable gains in testbench pass rates and real‑world performance improvements.

## Key Contributions  
- Structured contract as semantic‑alignment artifact that translates natural‑language requirements into explicit interfaces, constraints, validation checks, and rollback rules.  
- Hardware‑in‑the‑loop feedback loop that feeds HLS, Vivado, PYNQ runtime, power, and failure evidence back into the generation process to enable system‑level closure.  
- Decomposition of agents by semantic lowering and execution tasks rather than conversational roles: Contract Agent, HTML Agent, and Hardware‑in‑the‑Loop Agent.

## Methodology  
The authors decompose the workflow into three specialized agents. The Contract Agent parses natural language into a formal contract; the HTML Agent renders this contract as structured HTML for persistence; the Hardware‑in‑the‑Loop Agent implements the design on a HIL board, measures hardware evidence (e.g., runtime, power), and iteratively revises the model using that feedback. This agent‑centric approach replaces traditional conversational roles with task‑oriented responsibilities.

## Results  
On 94 locally executable HLS‑Eval tasks, ContractHIL‑HLS achieves a pass@1 rate of 70.4 % and pass@5 of 76.6 %, compared to the baseline 64.0 % single‑sample testbench pass rate. On a board‑tested ML‑KEM/ML‑DSA post‑quantum cryptography accelerator, the dual‑bitstream organization reduces six‑message average text runtime from 207.3 ms to 52.4 ms while maintaining positive routed WNS and preserving decrypted‑message verification.

## Significance  
By integrating hardware evidence into LLM‑driven HLS, ContractHIL‑HLS bridges the gap between high‑level code generation and practical board implementation, delivering both design robustness and tangible performance benefits. The approach demonstrates that contract‑based alignment can improve testbench success and enable real‑world system optimizations.

## Related Concepts  
- High‑Level Synthesis (HLS)  
- Hardware‑in‑the‑Loop (HIL) feedback  
- Multi‑agent workflow design  
- Natural language to formal contracts  
- LLM‑assisted code generation  
- Testbench pass rates and pass@k metrics

# Summary: 2026-07-30_14-25-23Z_AgenticMethodforDeterministicValidationofLegacyCod.md
Saved: 2026-07-30 20:38
Source: 2026-07-30_14-25-23Z_AgenticMethodforDeterministicValidationofLegacyCod.md
Model: None

---

## Summary  
The paper proposes the Locksmith Loop, an agentic test‑synthesis method for deterministic validation of legacy COBOL‑to‑Java migrations. It addresses the challenge of limited test data and corner‑case coverage by instrumenting both source and target code with mocks and running them on commodity hardware. An iterative loop performs Witness Search to explore program branches, followed by parity‑preserving mutations when routing boundaries are reached. The method systematically uncovers hidden execution paths that conventional input search cannot reach.  

## Key Contributions  
- Finding 1: The Locksmith Loop breaks input‑search plateaus by employing a deterministic oracle and parity checks to generate comprehensive test cases.  
- Finding 2: It identifies “Locked Paragraph” conditions that block deeper exploration, enabling the method to continue testing beyond those points.  
- Finding 3: Empirically, the approach achieves near‑complete coverage on open‑source COBOL programs (430–1,674 lines) and reaches 91.90% branch coverage on a production‑like program (up to 4,114 lines).  

## Methodology  
The authors instrumented the original COBOL source with mocks that simulate external I/O, then compiled it to Java while preserving runtime semantics. Both binaries were executed on commodity hardware in parallel environments. The Locksmith Loop iteratively feeds input mocks into the system, records execution traces, and uses a Witness Search algorithm to traverse branches not previously covered. When a “Locked Paragraph” is detected—signifying that further exploration would violate deterministic parity—the method applies parity‑preserving mutations to restore coverage without altering observable behavior.  

## Results  
Across three case studies spanning 430 to 4,114 source lines, the generated Java code matched the COBOL reference under deterministic parity checks in every accepted test case. Coverage improved beyond input‑search limits: two open‑source programs reached near‑complete line coverage, and the internal program achieved 91.90% branch coverage.  

## Significance  
This work demonstrates a novel, deterministic validation framework that can be applied to any legacy migration where traditional testing is limited by test data scarcity. By integrating agentic synthesis with parity preservation, it reduces reliance on exhaustive manual testing and accelerates confidence in automated code‑generation pipelines.  

## Related Concepts  
- Agentic test‑synthesis: programs that generate tests automatically.  
- Witness Search: algorithm for exploring execution paths using mock inputs.  
- Deterministic oracle: a reference implementation used to verify generated code matches original behavior.  
- Locked Paragraph: a runtime condition that prevents deeper exploration without violating parity.  
- Parity‑preserving mutation: modifications that keep observable output unchanged.

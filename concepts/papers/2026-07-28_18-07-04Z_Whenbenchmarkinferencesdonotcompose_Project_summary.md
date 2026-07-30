# Summary: 2026-07-28_18-07-04Z_Whenbenchmarkinferencesdonotcompose_Projectibility.md
Saved: 2026-07-29 21:29
Source: 2026-07-28_18-07-04Z_Whenbenchmarkinferencesdonotcompose_Projectibility.md
Model: None

---

## Summary  
The paper argues that AI benchmark inferences rarely justify downstream claims simply because they are valid in isolation; instead, a “projectibility” problem arises when the logical chain linking benchmarks to real‑world uses collapses. Its contribution is a non‑composition principle that demands alignment of endpoints, assumptions, and uncertainty across linked studies before their results can be combined. The authors also introduce an argument‑based validity framework designed to test whether such links are warranted rather than assumed. By exposing how parallel but sound studies can produce misleading aggregate stability, the work offers a diagnostic audit for unsupported joins in benchmark‑to‑use arguments.

## Key Contributions  
- **Non‑composition principle**: A bounded extension from observed benchmarks to unobserved tasks is only valid when endpoints and underlying assumptions are identical and all dependencies and uncertainties are explicitly carried through.  
- **Argument‑based validity framework**: Provides a systematic method for evaluating whether the logical links between studies constitute warranted projections rather than mere coincidences.  
- **Projectibility audit**: A diagnostic tool that identifies unsupported joins in benchmark‑to‑use reasoning, highlighting where parallel evidence can be mistakenly composed.

## Methodology  
The authors adopt a validity‑centred approach, treating each claim as an argument with premises (benchmark results), inference steps (generalizations), and conclusions (deployment outcomes). They construct “rival extensions” analogous to Goodman’s problem of rival extensions: alternative ways to project from observed data. Using this framework, they model the dependencies between studies—system, population, outcome, and conditions—as variables that may shift at each interface. A reanalysis simulation then demonstrates how aggregating parallel benchmarks can erase distinctions required for a later projection, thereby eroding projectibility.

## Results  
Through a legal‑research case study, the authors show that two independent studies—one benchmarking model performance on a fixed dataset and another evaluating deployment impact in a new environment—are each internally sound but cannot be composed to support a single claim about overall capability. The simulation reveals that aggregate stability metrics mask the loss of endpoint alignment, producing an illusion of continuity where none exists. Consequently, the projectibility audit flags two unsupported joins: (1) using benchmark scores as evidence for deployment efficacy without accounting for differing conditions, and (2) assuming shared model lineage when it is not.

## Significance  
This work matters because AI evaluation often treats benchmark results as self‑evident proof of capability, ignoring the epistemic gaps that arise at each projection step. By formalizing projectibility and providing a diagnostic audit, the paper mitigates overconfidence in AI systems, improves trustworthiness of downstream claims, and offers a methodological safeguard against false composition of evidence.

## Related Concepts  
- **Validity‑centred evaluation** – focusing on logical soundness rather than raw performance.  
- **Projectibility** – the ability to justify bounded extensions from observed to unobserved cases.  
- **Goodman’s problem of rival extensions** – alternative ways to infer new conclusions from data.  
- **Argument‑based validity** – a framework for testing whether logical links are warranted.  
- **Dependency and uncertainty propagation** – ensuring all assumptions and stochastic elements travel through the chain.

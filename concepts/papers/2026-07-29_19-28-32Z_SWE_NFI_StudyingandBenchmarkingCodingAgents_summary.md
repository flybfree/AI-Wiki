# Summary: 2026-07-29_19-28-32Z_SWE_NFI_StudyingandBenchmarkingCodingAgentsforNon_.md
Saved: 2026-07-30 20:22
Source: 2026-07-29_19-28-32Z_SWE_NFI_StudyingandBenchmarkingCodingAgentsforNon_.md
Model: None

---

## Summary  
The paper introduces SWE‑NFI, a benchmark designed to evaluate coding agents on non‑functional improvements (NFIs) that preserve observable behavior yet enhance software quality. By operationalizing developer‑oriented NFIs into executable rules and combining functional correctness testing with rule‑based NFI evaluation, the authors demonstrate that current agents lag behind human developers in overall NFI capability, especially for structural code enhancements.

## Key Contributions  
- [Finding 1] SWE‑NFI provides a reproducible benchmark of 188 tasks derived from real merged pull requests in open‑source Python projects, operationalized into 92 executable non‑functional improvement rules.  
- [Finding 2] All evaluated agents achieve only ~70 % functional correctness, while their NFI scores range from 0.0 to 1.3 on structural improvements—significantly lower than the human reference score of 1.5.  
- [Finding 3] The benchmark reveals a persistent gap between agents’ functional performance and their ability to produce meaningful non‑functional gains, highlighting the need for evaluation beyond pure correctness.

## Methodology  
The authors approached the problem by first collecting 188 tasks from actual pull requests in open‑source Python repositories. They translated developer‑oriented NFIs—such as code readability, maintainability, and modularity—into a set of 92 executable rules that can be applied to candidate codebases. The evaluation suite couples traditional functional correctness testing with these rule‑based NFI checks, allowing systematic comparison across both dimensions.

## Results  
The best‑performing commercial or open‑source coding agent reaches a 70 % functional correctness rate on the benchmark tasks. However, when measured against the human reference, its overall NFI score is markedly lower: structural improvements range from 0.0 to 1.3 versus a human score of 1.5. This indicates that while agents excel at preserving functionality, they often miss opportunities for non‑functional enhancements.

## Significance  
SWE‑NFI offers a concrete foundation for researchers and practitioners to assess coding agents beyond functional correctness alone. By exposing the limitations in NFI generation, especially structural code improvements, the benchmark underscores the importance of holistic quality metrics in evaluating AI‑assisted software development tools.

## Related Concepts  
- Coding agents (AI systems that generate or modify code)  
- Non‑functional improvements (NFIs) – enhancements that do not alter observable behavior but improve quality  
- Benchmarking frameworks for AI evaluation  
- Functional correctness testing  
- Rule‑based evaluation of software properties

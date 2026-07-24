# Summary: 2026-07-21_04-34-35Z_DoAI_NativeBiotechsNeedDepartments_BenchmarkingCom.md
Saved: 2026-07-24 00:30
Source: 2026-07-21_04-34-35Z_DoAI_NativeBiotechsNeedDepartments_BenchmarkingCom.md
Model: None

---

## Summary  
The paper challenges the assumption that AI‑native biotech firms should replicate traditional departmental structures and instead proposes a “Company World Model” – a dynamic, asset‑to‑value representation that captures scientific progress, regulatory approvals, BD outcomes, commercial revenue, and execution constraints. By constructing a dry‑lab benchmark with 45 retrospective decision cases, the authors test four organisational architectures: human org‑mimic, stronger human org‑mimic plus AI agents, AI‑native asset‑centric, and AI‑native value‑conversion (a prompt‑level approximation of the World Model). The value‑conversion architecture achieved the highest automatic score and was preferred by blind judges, revealing that a shared predictive state is more effective than static departmental maps.  

## Key Contributions  
- **Company World Model** – Introduces a persistent asset‑to‑value representation with transition models, explicit value functions, planning, and updating across scientific, regulatory, BD, commercial, financial, and execution constraints.  
- **Benchmark & Findings** – Shows that an AI‑native “value‑conversion” architecture outperforms human‑org‑mimic baselines in a dry‑lab setting, with the strongest results under stress tests; however, neutral judges do not consistently favor it.  
- **Objective‑Sensitive Insight** – Demonstrates that departments may remain useful as governance views, but the core AI‑native operating primitive should be a shared, predictive asset‑to‑value state rather than a static org chart.  

## Methodology  
The authors built a dry‑lab benchmark containing 45 retrospective public‑information decision cases with strict time cutoffs and hidden outcomes. Each case follows common schemas and is scored automatically; judges evaluate pairwise comparisons blind to the underlying architecture. The evaluation measures automatic value‑conversion scores and human preference, isolating the impact of each organisational design on the target objective (BD success, regulatory approval, launch, revenue).  

## Results  
The AI‑native value‑conversion model achieved the highest automatic score and was strongly preferred by value‑specific judges. Stress tests revealed that a stronger human baseline remained competitive, indicating robustness limits. A neutral judge did not show robust dominance of the AI‑native approach. Codec‑only mechanistic ablations identified three “rooms” (Revenue Room, Deal Room, Approval Room) as contributing to performance, suggesting specific functional modules within the World Model are valuable. The study is confined to dry‑lab evaluation and does not claim real‑world drug success or revenue prediction accuracy.  

## Significance  
The findings shift the focus from static departmental hierarchies to a dynamic asset‑to‑value model that can be continuously updated as scientific, regulatory, and commercial signals evolve. This abstraction could inform more flexible AI‑native organizational structures in biotech, enabling better alignment of agent goals with complex, multi‑stage drug development pipelines.  

## Related Concepts  
- Company World Model (asset‑to‑value state representation)  
- Value conversion (prompt‑level approximation of dynamic value updates)  
- Agent roles vs. departmental structures in AI organizations  
- Dry‑lab benchmarking for organisational design evaluation

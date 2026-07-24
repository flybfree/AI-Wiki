# Summary: 2026-07-21_04-34-35Z_DoAI_NativeBiotechsNeedDepartments_BenchmarkingCom.md
Saved: 2026-07-24 00:47
Source: 2026-07-21_04-34-35Z_DoAI_NativeBiotechsNeedDepartments_BenchmarkingCom.md
Model: None

---

## Summary  
The paper investigates whether AI‑native biotechnology firms should organize themselves around traditional departmental silos or instead adopt a dynamic “Company World Model” (CWM) that captures an asset‑to‑value state across scientific, regulatory, commercial and financial dimensions. By introducing a dry‑lab benchmark with 45 retrospective decision cases, the authors compare four organizational architectures—human org‑mimic, stronger human org‑mimic, AI‑native asset‑centric, and AI‑native value‑conversion—and demonstrate that the value‑conversion architecture best aligns with objective‑driven outcomes. Their contribution is a novel abstraction of CWM as a persistent state representation with transition models and explicit value functions, together with empirical evidence that this model yields superior automatic scoring and human preference.

## Key Contributions  
- [Finding 1] AI‑native companies should operate around a shared asset‑to‑value state rather than static org charts; the CWM abstraction is more effective for prediction and governance.  
- [Finding 2] The value‑conversion architecture—a prompt‑level approximation of the Live Asset Value Record updated by Deal, Approval, Revenue and Investment Arbiter loops—achieves the highest automatic value‑conversion score and is strongly preferred by blinded judges.  
- [Finding 3] Stress tests reveal that stronger human baselines remain competitive under objective‑sensitive evaluation, while a neutral judge does not show robust dominance; mechanistic ablations indicate that Revenue Room, Deal Room and Approval Room are useful components of the CWM.

## Methodology  
The authors constructed a dry‑lab benchmark comprising 45 retrospective public‑information decision cases with hidden outcomes, common schemas, automatic scoring, and blinded pairwise judging. They contrasted four organizational models: (1) human org‑mimic, (2) stronger human org‑mimic + AI, (3) AI‑native asset‑centric, and (4) AI‑native value‑conversion. The value‑conversion model is a prompt‑level simulation of a Company World Model that tracks Live Asset Value Record through Deal, Approval, Revenue and Investment Arbiter loops, updating across scientific, regulatory, BD, commercial, financial and execution constraints.

## Results  
The value‑conversion architecture obtained the highest automatic value‑conversion score among all baselines. Blind judges consistently preferred it over the original org‑mimic designs. Stress tests showed that stronger human baselines could still compete with the AI‑native model when judged by objective criteria, but a neutral judge did not exhibit robust superiority of the AI model. Mechanistic ablations confirmed that the Deal Room, Approval Room and Revenue Room components contribute meaningfully to the CWM’s predictive power.

## Significance  
The study suggests that while traditional departmental structures may remain useful as governance views, the core operating primitive for AI‑native drug development should be a dynamic asset‑to‑value state rather than a static org chart. This insight guides the design of AI‑driven biotech organizations toward more predictive and value‑aligned decision processes.

## Related Concepts  
Company World Model, asset‑to‑value state representation, transition models, explicit value functions, planning and updating across scientific, regulatory, BD, commercial, financial and execution constraints, dry‑lab benchmark, value‑conversion architecture, Live Asset Value Record, Deal Room, Approval Room, Revenue Room, Investment Arbiter loops.

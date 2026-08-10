# Summary: 2026-08-07_10-40-53Z_Human_CenteredExplainableAIforTinyMLEdgeDevices_AP.md
Saved: 2026-08-09 22:54
Source: 2026-08-07_10-40-53Z_Human_CenteredExplainableAIforTinyMLEdgeDevices_AP.md
Model: None

---

## Summary  
The paper addresses the challenge of selecting explainable AI (XAI) methods for TinyML edge devices in clinical settings, where strict resource constraints and human interpretability are both critical. It proposes a Pareto‑based selection framework that couples large language model guidance with deterministic feasibility filtering to balance explanation fidelity, method stability, and deployment cost. The framework systematically maps stakeholder preferences to candidate XAI techniques, then optimizes trade‑offs using the Pareto front. This approach enables clinicians and patients to understand model predictions while respecting hardware limits.

## Key Contributions  
- [Finding 1] A human‑centered multi‑objective design problem formulation that integrates qualitative stakeholder preferences with quantitative explanation quality and proxy‑based deployment cost.  
- [Finding 2] An LLM‑guided interface that translates these preferences into a ranked set of candidate XAI methods, enabling systematic comparison across the design space.  
- [Finding 3] A Pareto‑optimization algorithm that identifies trade‑off points among fidelity, stability, and cost, producing a visual trade‑off map for decision support.

## Methodology  
The authors first collect stakeholder preferences through surveys or interviews, encoding them as preference vectors. These vectors are fed to an LLM that generates candidate XAI methods (e.g., saliency maps, counterfactuals) with estimated explanation fidelity and computational cost. The candidates undergo deterministic feasibility filtering based on MCU resource budgets. Remaining methods are evaluated for stability across model variations, and their trade‑offs are plotted in a Pareto front using multi‑objective optimization. The framework outputs the most efficient method(s) for a given stakeholder profile.

## Results  
The proof‑of‑concept evaluation on a skin lesion classification task demonstrates that the framework can compare at least 12 candidate XAI methods, identifies Pareto‑efficient sets, and provides clear visual trade‑off maps. Computational selection is fully automated; physical MCU deployment and human‑expert validation are not yet performed but are planned for future work.

## Significance  
By formalizing a human‑centered optimization problem for XAI on TinyML, the paper advances practical AI deployment in healthcare by ensuring explanations are both understandable and feasible. It bridges theory and practice, offering a reusable framework that can be adapted to other clinical domains where explainability is essential yet resources are scarce.

## Related Concepts  
- Explainable AI (XAI)  
- TinyML  
- Pareto front / multi‑objective optimization  
- Large language model (LLM) guided design  
- Proxy‑based deployment cost  
- Human‑centered design

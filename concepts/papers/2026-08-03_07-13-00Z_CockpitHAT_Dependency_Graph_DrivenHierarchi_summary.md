# Summary: 2026-08-03_07-13-00Z_CockpitHAT_Dependency_Graph_DrivenHierarchicalAttr.md
Saved: 2026-08-03 23:43
Source: 2026-08-03_07-13-00Z_CockpitHAT_Dependency_Graph_DrivenHierarchicalAttr.md
Model: None

---

## Summary  
The paper tackles the problem of correctness collapse in LLM multi‑agent systems, especially in safety‑critical embodied environments such as automotive cockpits where a single erroneous utterance can cause dangerous actions. It proposes CockpitHAT, a hierarchical attribution framework that replaces naïve positional windows with dependency‑distance thresholds extracted from interaction DAGs to capture the logical relationships between utterances and actions. The method also integrates multi‑channel evidence—dialogue, vehicle state, environment, and memory—through an embodied adapter and applies a safety‑uplift mechanism that elevates high‑risk failures during confidence‑weighted analyst consensus. By releasing CockpitBench, a benchmark of 212 annotated failure traces labeled with ISO 26262 ASIL severity, the authors demonstrate that their approach yields state‑of‑the‑art performance on both public and proprietary datasets.

## Key Contributions  
- **Finding 1:** Introduces CockpitHAT, a hierarchical attribution framework that uses dependency‑distance thresholds from interaction DAGs instead of positional windows to model logical dependencies between utterances and actions.  
- **Finding 2:** Integrates multi‑channel evidence via an embodied adapter, enabling the system to jointly consider dialogue, vehicle state, environmental conditions, and memory when attributing failures.  
- **Finding 3:** Applies a safety‑uplift mechanism that prioritizes high‑risk failures (according to ASIL severity) during confidence‑weighted analyst consensus, thereby improving diagnostic reliability in safety‑critical settings.

## Methodology  
The authors approached the problem by first constructing an interaction dependency graph for each multi‑agent dialogue. From this graph they computed distance thresholds that define “relevant” utterance pairs rather than fixed positional windows. These thresholds guide a hierarchical attention mechanism that assigns attribution scores to each failure event. To handle multiple evidence streams, an embodied adapter fuses signals from the four channels into a unified latent representation. Finally, the safety‑uplift is implemented by scaling the confidence of high‑ASIL failures before aggregating analyst votes, ensuring that critical errors are not suppressed by low‑confidence predictions.

## Results  
On the public Who&When benchmark, CockpitHAT achieves 77.9 % agent‑level accuracy and 37.8 % step‑exact accuracy on the hand‑crafted split, and 86.5 % / 46.0 % on the algorithm‑generated split—surpassing the text‑only SOTA ECHO by up to 17.6 and 16.7 points respectively. On CockpitBench, the system reaches 78.3 % agent‑level accuracy and 38.2 % step‑exact accuracy, confirming its efficacy across both datasets.

## Significance  
These results establish that dependency‑aware, multi‑channel, risk‑calibrated attribution is a viable paradigm for reliable failure diagnosis in real‑world embodied LLM multi‑agent systems, directly addressing the safety concerns highlighted by ISO 26262. By providing higher accuracy and better handling of high‑risk failures, CockpitHAT can improve diagnostic confidence for human operators and reduce the likelihood of hazardous outcomes.

## Related Concepts  
- Dependency graph (DAG)  
- Hierarchical attribution  
- Multi‑channel evidence fusion  
- Safety‑uplift mechanism  
- ISO 26262 ASIL severity labeling  
- Correctness collapse in LLM multi‑agent systems  
- Embodied adapter for sensor and state integration

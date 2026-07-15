title: "Summary: 2026-06-24_17-53-26Z_SameEvidence_DifferentAnswer_AuditingOrderSensitiv.md"
# Summary: 2026-06-24_17-53-26Z_SameEvidence_DifferentAnswer_AuditingOrderSensitiv.md
Saved: 2026-06-24 22:02
Source: 2026-06-24_17-53-26Z_SameEvidence_DifferentAnswer_AuditingOrderSensitiv.md
Model: None

---


## Summary  
The paper investigates whether multimodal large language models (MLLMs) are sensitive to the order in which evidence is presented, a reliability issue highlighted by emerging AI evaluation guidelines. By auditing 18 frontier and open‑weight MLLMs with a five‑facet protocol called Facet‑Probe, the authors demonstrate that none of these models are order‑invariant; answer flips occur at rates ranging from 24 % to 50 %. They also introduce a Bayesian item‑response model that separates ordering noise from per‑facet bias and estimate a same‑ordering control that reflects the decoder’s stochastic floor. Prompt‑level mitigation is found to be modality‑conditional and does not transfer between text and visual reasoning, suggesting that prompt changes alone are insufficient for general order robustness.

## Key Contributions  
- [Finding 1] No MLLM is order‑invariant; screened per‑facet panel‑mean flip rates span 24 % to 50 %.  
- [Finding 2] Gemini at temperature 0 exhibits a substantial ordering excess over the same‑input decoder stochastic floor in verified cells.  
- [Finding 3] Training‑time prompt changes are modality‑conditional and do not transfer from text to visual reasoning.

## Methodology  
The authors audited 18 multimodal large language models using Facet‑Probe, which evaluates five facets: option selection, evidence‑chunk ordering, document‑rank ordering, image‑set ordering, and mixed‑modality ordering. A Bayesian item‑response model is employed to decompose observed answer flips into components of per‑facet bias and pure ordering noise. Additionally, a same‑ordering control is computed for each cell to estimate the decoder’s stochastic floor that would be present if the evidence order were truly irrelevant.

## Results  
Across all panels, mean flip rates vary widely (24 %–50 %). Gemini at temperature 0 shows an ordering excess of roughly 12 % above the noise‑floor baseline. The best model still flips on about 13.4 % of trials. Mitigation experiments reveal that changing prompts works for one modality but not the other, indicating no cross‑modal transfer. These findings confirm that prompt‑level fixes are unlikely to provide general order robustness.

## Significance  
The results expose a critical reliability gap in AI evaluation: order sensitivity is pervasive across state‑of‑the‑art MLLMs and cannot be ignored. Prompt adjustments alone do not solve the problem, underscoring the need for training‑time or architectural interventions that make models truly order‑invariant. The authors propose reporting cross‑ordering flip rate as a standard metric for future work.

## Related Concepts  
Order invariance, multimodal large language models (MLLMs), Bayesian item‑response modeling, decoder stochastic floor, prompt mitigation, cross‑modal reasoning, reliability in AI evaluation.

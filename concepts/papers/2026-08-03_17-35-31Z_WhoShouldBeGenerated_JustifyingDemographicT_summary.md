# Summary: 2026-08-03_17-35-31Z_WhoShouldBeGenerated_JustifyingDemographicTargetsi.md
Saved: 2026-08-04 00:52
Source: 2026-08-03_17-35-31Z_WhoShouldBeGenerated_JustifyingDemographicTargetsi.md
Model: None

---

## Summary  
The paper addresses the challenge of defining fairness targets for open‑ended generative models when sensitive attributes are not specified in prompts. It argues that existing fairness frameworks assume known demographic inputs, but generative audits require constructing justifiable output distributions. The authors formalize a missing‑target problem and break target construction into four commitments. Their work shows that default geographic or occupational priors lead to large mismatches with generated outputs.  

## Key Contributions  
- Finding 1: They introduce a framework decomposing demographic target justification into evaluative object, prior admissibility, allocation, and operationalization.  
- Finding 2: The geographic prior is justified under a membership interpretation for public‑world use, while the occupational prior requires an independent objective like workforce‑composition fidelity.  
- Finding 3: Experiments on AP‑Bench reveal distribution divergence from geography‑derived targets of 0.508–0.606 and JSD₂ changes of 0.279–0.355 when using equal‑category comparators.  

## Methodology  
The authors treat target construction as a component of fairness evaluation rather than a pre‑step. They formalize the missing‑target problem, enumerate the four commitments, and apply them to generate synthetic demographic targets for AP‑Bench prompts. The process involves defining the evaluative object (e.g., “CEO in the United States”), selecting prior admissibility (geographic membership), allocating to occupations with an incumbency interpretation, and operationalizing via metric computation.  

## Results  
On AP‑Bench, the model’s generated CEO‑in‑US outputs deviate from the geographic target distribution by 0.508–0.606 on a 0‑1 scale. Replacing geography targets with equal‑category comparators while keeping generations and measurement fixed yields mean absolute cell‑level JSD₂ changes of 0.279–0.355, indicating substantial fairness drift.  

## Significance  
This work clarifies that fairness standards must be explicitly justified before being used as benchmarks, preventing reliance on implicit or arbitrary priors. It shifts the responsibility from model developers to auditors to construct transparent, defensible demographic targets.  

## Related Concepts  
- Open‑ended generation  
- Demographic value unspecification  
- Group fairness  
- Generative audit  
- Target construction  
- JSD₂ metric  
- Geographic membership interpretation  
- Incumbency interpretation

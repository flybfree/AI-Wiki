# Summary: 2026-08-01_06-51-38Z_CrossProjection_GeometricGroundingBeyondViewpointC.md
Saved: 2026-08-03 21:25
Source: 2026-08-01_06-51-38Z_CrossProjection_GeometricGroundingBeyondViewpointC.md
Model: None

---

## Summary  
CrossProjection introduces a diagnostic framework for evaluating whether vision‑language models preserve architectural component identity across heterogeneous drawing views (plans, sections, elevations) that cannot be explained by simple viewpoint changes. The study evaluates three tasks—Matching, Registration, and Geometric Grounding—using categorical judgments, candidate selection, and free localization on 23 real drawing sets. It compares state‑of‑the‑art models such as GPT‑5.5, Qwen3‑VL‑32B‑Instruct, and GLM‑4.5V across thousands of conditions and also measures human performance. The work shows that categorical success does not guarantee reliable explicit geometric grounding.

## Key Contributions  
- [Finding 1] CrossProjection reveals a gap between high categorical accuracy and true spatial reliability in vision‑language models.  
- [Finding 2] Closed‑choice matching scores are higher than free localization, indicating candidate selection mitigates but does not eliminate errors.  
- [Finding 3] Human participants achieve 87.3‑93.3% categorical accuracy and 76‑92% GT‑region hit rates, confirming task feasibility.

## Methodology  
The authors construct a benchmark using natural and vector‑text‑suppressed architectural drawings. For each model they generate candidate‑supported Matching/Registration outputs, free point localization, free line/endpoint localization, and GT‑region labeling. The dataset comprises 23 drawing sets with 1,954 categorical conditions per model, and human participants evaluate the same outputs to provide ground truth.

## Results  
Overall scores: GPT‑5.5 = 82.4%, Qwen3‑VL‑32B‑Instruct = 62.2%, GLM‑4.5V = 57.2%. Point/region PCK@0.05 ranges from 54‑76% (GPT) to 8‑10% (Qwen) and 14‑36% (GLM); line endpoint PCK@0.05 is 22%, 4%, 0%. A coordinate grid recovers some GPT point/region precision but not lines.

## Significance  
The findings caution that categorical correctness should not be taken as evidence of reliable spatial grounding in CAD/BIM systems. It underscores the need for reusable on‑sheet anchors, fixed‑denominator scoring, and hash‑locked artifacts to create an audit trail for this gap.

## Related Concepts  
CrossProjection, geometric grounding, multi‑view reasoning, vision‑language models, architectural drawing sets, Matching, Registration, Grounding, PCK@0.05, candidate selection, human evaluation.

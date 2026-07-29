# Summary: 2026-07-28_14-11-10Z_LossInvarianceDeterminesWhatConceptLayersEncode_Vo.md
Saved: 2026-07-28 22:49
Source: 2026-07-28_14-11-10Z_LossInvarianceDeterminesWhatConceptLayersEncode_Vo.md
Model: None

---

## Summary  
The paper investigates whether prediction accuracy alone is sufficient to validate the interpretability of a concept layer in a bottleneck model, using left ventricular volumes as concepts for ejection fraction estimation from echocardiographic video. It introduces a volume‑grounding approach where volumes form an intermediate variable and compares training with only ratio‑based loss versus additional supervision of absolute volume values. The study shows that without absolute supervision the predicted volumes collapse to near‑zero variance because the loss is invariant under scaling, while supervision in millilitres reduces error at a modest cost to accuracy.

## Key Contributions  
- [Finding 1] The concept bottleneck does not improve prediction accuracy of ejection fraction relative to direct regression.  
- [Finding 2] Without absolute volume supervision, predicted volumes collapse to near‑zero variance due to loss invariance under scaling.  
- [Finding 3] Adding absolute unit supervision reduces volume error significantly while only modestly affecting ejection fraction.

## Methodology  
The authors train a video transformer encoder on a publicly available echocardiography dataset. They create an end‑systolic and end‑diastolic concept layer (volumes) and compute ejection fraction analytically without any residual path to the output. Two training regimes are compared: one where the loss is based solely on the ratio of volumes (ejection fraction), and another where the loss includes supervision of absolute volume values in millilitres.

## Results  
The model achieves a mean absolute error of 6.89 for ejection fraction versus 7.13 for the baseline direct regression, indicating only a modest improvement. Without absolute supervision, predicted volumes have a spread of 0.1 ml compared with reference spreads of 35.7–45.7 ml; correlation is partly preserved. With absolute supervision, volume error drops from 89.8 to 25.8 ml at the expense of a 0.4 increase in ejection fraction error.

## Significance  
This work demonstrates that interpretability via concept accuracy can conceal a layer that carries no physical scale; validation should consider invariance properties of the objective rather than only prediction accuracy, informing the design of clinical interpretable models where volume grounding is used.

## Related Concepts  
Loss invariance, concept bottleneck, volume grounding, ratio‑based loss, absolute supervision, volumetric interpretation in medical imaging.

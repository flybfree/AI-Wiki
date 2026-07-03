# Summary: 2026-07-02_17-58-29Z_DemoPSD_Disagreement_ModulatedPolicySelf_Distillat.md
Saved: 2026-07-02 23:01
Source: 2026-07-02_17-58-29Z_DemoPSD_Disagreement_ModulatedPolicySelf_Distillat.md
Model: None

---


## Summary  
On‑policy self‑distillation (OPSD) enables a single model to act as both teacher and student for reasoning tasks, but dense token‑level supervision often causes overfitting, suppresses exploration, and leaks privileged information. The authors propose DemoPSD, which mitigates these issues by steering the student toward a reverse‑KL barycenter of the teacher and student distributions while using the inter‑distribution discrepancy to adaptively blend guidance at each token position.

## Key Contributions  
- **Leakage attenuation:** DemoPSD effectively reduces privileged information leakage that would otherwise create answer‑dependent shortcuts unavailable at test time.  
- **Exploration preservation:** The framework maintains a high training entropy, preserving the student’s capacity to explore diverse reasoning paths.  
- **Superior performance and generalization:** Experiments on SciKnowEval across four scientific domains show DemoPSD outperforms both GRPO and SDPO while delivering robust out‑of‑distribution results on GPQA.

## Methodology  
DemoPSD replaces the full teacher distribution with a *reverse‑KL barycenter* target, defined as a weighted geometric combination of the teacher and student distributions. The authors compute the difference between these two probability distributions and use this discrepancy to modulate the blending coefficient at each token position. This selective adoption of teacher guidance ensures that the student learns from the teacher only where it is beneficial, while avoiding over‑fitting to in‑domain patterns.

## Results  
Across four scientific fields on SciKnowEval, DemoPSD achieved higher accuracy and lower loss than GRPO and SDPO baselines. The training process retained a significantly higher entropy, indicating preserved exploration. On the out‑of‑distribution GPQA benchmark, DemoPSD’s models performed robustly, outperforming the competition in generalization.

## Significance  
By decoupling teacher guidance from student capacity through adaptive blending, DemoPSD tackles two longstanding problems in OPSD: privileged information leakage and exploration suppression. This leads to more reliable reasoning agents that can be deployed across domains without sacrificing performance or adaptability.

## Related Concepts  
- On‑policy self‑distillation (OPSD)  
- Teacher‑student distillation with token‑level supervision  
- Reverse‑KL barycenter as a distribution blending target  
- Gradient policy distillation  
- Exploration capacity and training entropy  
- Privileged information leakage in dense supervision

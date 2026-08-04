# Summary: 2026-08-02_14-16-14Z_DistillWhattheStudentCanSee_Fisher_ProjectedOn_Pol.md
Saved: 2026-08-03 23:27
Source: 2026-08-02_14-16-14Z_DistillWhattheStudentCanSee_Fisher_ProjectedOn_Pol.md
Model: None

---

## Summary  
The paper addresses the limitation of standard on‑policy distillation for vision‑language models by showing that teacher corrections can depend on visual details a compact student cannot capture. It proposes Fisher‑Projected On‑Policy Distillation (FP‑OPD), which projects only locally realizable teacher corrections onto the student’s visual tangent space using its Fisher metric. This capacity‑aware target improves downstream performance relative to both pretrained students and conventional OPD. The authors demonstrate that FP‑OPD yields consistent gains across multimodal benchmarks.

## Key Contributions  
- [Finding 1] Standard on‑policy distillation assumes the full teacher distribution is a valid target, leading to suboptimal student capacity utilization.  
- [Finding 2] As the target approaches the complete teacher distribution, student performance degrades because it cannot realize many of the prescribed shifts.  
- [Finding 3] Fisher‑Projected On‑Policy Distillation provides a locally realizable, capacity‑aware target that yields higher scores on vision‑language reasoning tasks.

## Methodology  
The authors employ continuous visual perturbations to estimate the student’s local visual tangent space. They compute the centered teacher–student log‑probability gap and project it onto this tangent space under the student’s Fisher metric, producing a compact target distribution. The distillation is performed via full‑vocabulary reverse KL minimization along student trajectories, preserving the on‑policy framework while respecting the model’s representational limits.

## Results  
In an 8B‑to‑2B distillation experiment across seven multimodal benchmarks, FP‑OPD improves all scores relative to the pretrained student and by an average of 1.60 points over standard OPD. The method raises the overall average score by 2.77 points compared with the baseline student, confirming its effectiveness in capturing only feasible teacher corrections.

## Significance  
By restricting distillation targets to those that the student can actually generate, FP‑OPD aligns training objectives with the model’s intrinsic capacity, leading to better generalization and performance on vision‑language reasoning tasks. This work advances the field of on‑policy distillation by introducing a Fisher‑based projection mechanism tailored to visual representations.

## Related Concepts  
- On‑policy distillation (OPD)  
- Teacher‑student log‑probability gap  
- Fisher metric in tangent space  
- Vision‑language reasoning benchmarks  
- Capacity‑aware target functions

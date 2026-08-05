# Summary: 2026-07-28_17-59-46Z_PasstheBaton_Trajectory_RelayedOn_PolicyDistillati.md
Saved: 2026-07-28 23:04
Source: 2026-07-28_17-59-46Z_PasstheBaton_Trajectory_RelayedOn_PolicyDistillati.md
Model: None

---

## Summary  
The paper tackles a persistent flaw in on‑policy distillation (OPD) where a student’s trajectory is derailed by an early, incorrect reasoning step, causing all later generations to inherit the wrong direction and produce unreliable supervision. To remedy this, the authors propose Relay On‑Policy Distillation (Relay‑OPD), which injects brief teacher‑led “handoff” legs at detected trigger points so that the student can resume on a corrected trajectory. This limited‑budget relay strategy concentrates intervention on critical early positions while preserving most of the student’s own policy, thereby reducing training length and improving output quality. The method demonstrates consistent gains across multiple reasoning benchmarks without sacrificing compute efficiency.

## Semantic links
- [[concepts/papers/2026-07-30_16-17-15Z_LightningOPD2_0_MitigatingStyleBiasinCross__summary.md|Summary: 2026-07-30_16-17-15Z_LightningOPD2_0_MitigatingStyleBiasinCross_Teacher.md]] — 3 title terms overlap; 13 summary/topic terms overlap; semantic match 0.11
- [[concepts/papers/2026-07-30_11-11-32Z_Flux_OPD_On_PolicyDistillationwithEvolvingC_summary.md|Summary: 2026-07-30_11-11-32Z_Flux_OPD_On_PolicyDistillationwithEvolvingContexts.md]] — 3 title terms overlap; 10 summary/topic terms overlap; semantic match 0.11
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 2 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The teacher‑student asymmetry in failed prefixes—teachers tend to redirect while students continue along the original direction—creates a label‑free handoff trigger that can be exploited for correction.  
- [Finding 2] Relay‑OPD constructs a relay trajectory by letting the teacher briefly take over at identified trigger points, producing a teacher leg followed by student resuming on the merged path.  
- [Finding 3] A limited relay budget yields substantial performance improvements and cuts training trajectory length by more than 50 %, making distillation more scalable.

## Methodology  
The authors address prefix failure by first detecting when a student’s reasoning diverges from the teacher’s intended direction, then inserting a short “teacher leg” that corrects the path. The resulting combined trajectory serves as supervision for the student, which is subsequently optimized on‑policy using the full merged sequence. This approach limits the number of teacher interventions to only those early positions where they matter most, preserving computational efficiency while steering the student away from misdirected continuations.

## Results  
Relay‑OPD achieves the best or second‑best results on eight mathematical reasoning benchmarks, outperforming standard OPD by an average +5.73 % and beating FastOPD by +1.49 % for the 1.7B model (with similar gains at 0.6B). Crucially, training trajectory length is reduced by over 50 %, indicating that fewer teacher‑led legs are needed to achieve high performance.

## Significance  
By mitigating prefix failure and concentrating teacher intervention on early, critical points, Relay‑OPD offers a more efficient alternative to conventional OPD. It enables smaller models (e.g., Qwen3‑0.6B) to match the reasoning capabilities of larger teachers while dramatically lowering compute costs, which is especially valuable for resource‑constrained deployment scenarios.

## Related Concepts  
- On‑policy distillation (OPD)  
- Prefix failure in language generation  
- Teacher‑student asymmetry  
- Relay trajectory construction  
- Label‑free handoff trigger  
- Limited‑budget intervention  
- Trajectory length reduction

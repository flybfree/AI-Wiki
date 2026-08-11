# Summary: 2026-08-09_14-20-12Z_PAST_PrivilegedAdaptationfromCompleteStudentTrajec.md
Saved: 2026-08-10 23:22
Source: 2026-08-09_14-20-12Z_PAST_PrivilegedAdaptationfromCompleteStudentTrajec.md
Model: None

---

## Summary  
The paper proposes PAST, a method that enriches on‑policy self‑distillation (OPSD) by treating complete student trajectories as privileged teacher signals while keeping the student’s prefix‑only distillation unchanged. By conditioning the teacher on both successful and failed rollouts, PAST captures hindsight information that standard OPSD ignores, enabling a more accurate teacher distribution. The authors show that this trajectory‑conditioned teacher can be projected to the conditional arithmetic mean of the teacher’s distributions via forward‑KL distillation, preserving student‑specific next‑token behavior on correct paths. Experiments across three mathematical reasoning benchmarks demonstrate a 5.6 percentage point gain in average@12 over vanilla OPSD.  

## Key Contributions  
- [Finding 1] PAST treats each completed student trajectory as additional privileged information for the teacher, enabling self‑distillation that leverages hindsight.  
- [Finding 2] The forward‑KL projection separates trajectory‑specific variation from the mean policy shift available to the student, yielding a distributional fixed point equal to the frozen student on correct trajectories.  
- [Finding 3] Empirically, PAST improves macro Avg@12 by 5.6 points over vanilla OPSD across three reasoning benchmarks.  

## Methodology  
The authors start with an existing on‑policy self‑distillation framework where a teacher is trained on prefixes sampled from its own rollouts. They augment this teacher by conditioning the loss on the full trajectory (both success and failure) while leaving the student’s prefix‑only objective unchanged. The adapted teacher is then projected onto the conditional arithmetic mean of its distribution using forward‑KL distillation, which averages over all trajectories sharing a given prefix but discards uncorrelated trajectory noise. This projection creates a teacher that respects both the prefix distribution (privileged) and the hindsight context (student‑proximity regularization).  

## Results  
Theoretically, PAST’s projected teacher has the frozen student as an ideal distributional fixed point on correct trajectories, meaning no further gradient would improve its distribution. Experimentally, on three mathematical reasoning datasets, PAST achieves a macro Avg@12 of 78.4 points versus 72.8 for vanilla OPSD—a 5.6‑point absolute improvement (≈5.6 pp). A $2×2$ factorial experiment confirms that both complete‑trajectory access and teacher adaptation contribute positively, while removing trajectories or shuffling them eliminates gains, indicating the adapted teacher truly uses matching hindsight context.  

## Significance  
By integrating trajectory information into OPSD, PAST moves beyond prefix‑only supervision toward a more faithful representation of student reasoning, potentially unlocking higher performance on complex tasks where success depends on subtle internal states. The method also provides a principled way to regularize teachers using student‑proximity loss, which could be applied to other self‑distillation regimes.  

## Related Concepts  
- On‑policy self‑distillation (OPSD)  
- Privileged adaptation  
- Trajectory conditioning  
- Forward‑KL projection  
- Student‑proximity regularization  
- Arithmetic mean of conditional distributions

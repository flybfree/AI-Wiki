# Summary: 2026-08-09_14-20-12Z_PAST_PrivilegedAdaptationfromCompleteStudentTrajec.md
Saved: 2026-08-10 23:23
Source: 2026-08-09_14-20-12Z_PAST_PrivilegedAdaptationfromCompleteStudentTrajec.md
Model: None

---

## Summary  
The paper proposes PAST (Privileged Adaptation from Student Trajectories), an extension of on‑policy self‑distillation that incorporates the full student trajectory—including both successes and failures—as privileged information. While vanilla OPSD only uses prefix‑level next‑token distributions, PAST preserves those distributions on correct trajectories and adapts the teacher using hindsight from failed ones. The adapted teacher is projected via forward‑KL distillation to a conditional arithmetic mean given the prefix, separating trajectory‑specific variation from the policy shift available to the student. This approach yields measurable gains over standard OPSD without altering the student’s distillation prefixes.

## Key Contributions  
- [Finding 1] PAST treats each completed student trajectory as additional privileged information that preserves the next‑token distribution on correct trajectories while leaving the prefix‑only distillation unchanged.  
- [Finding 2] The teacher is adapted via a student‑proximity regularization term that uses failed trajectories to verify success, ensuring the teacher aligns with verified outcomes.  
- [Finding 3] Forward‑KL projection of teacher distributions to their conditional mean given the prefix isolates trajectory‑specific variation from the overall policy shift.

## Methodology  
The authors begin with a standard OPSD setup where a student generates rollouts and prefixes are distilled from its next‑token distribution. Instead of discarding the full trajectory, PAST retains it as privileged data. For correct trajectories, the teacher’s distribution is frozen to match the student’s; for failed trajectories, a regularization term encourages the teacher to shift toward success while respecting proximity to the student’s policy. The forward‑KL step computes the conditional mean of the teacher over all prefixes sharing the same trajectory context, effectively projecting away unstructured variation and focusing on the trajectory‑specific signal.

## Results  
Across three mathematical reasoning benchmarks, PAST improves the Avg@12 macro average by 5.6 percentage points relative to vanilla OPSD. A $2\times2$ factorial experiment confirms that gains arise both from accessing complete trajectories and from teacher adaptation; removing trajectories or shuffling them eliminates improvements, indicating that the adapted teacher relies on matching hindsight context. These results demonstrate a robust boost in distillation performance when student‑specific trajectory information is leveraged.

## Significance  
PAST demonstrates that unutilized student‑level hindsight can substantially enhance on‑policy self‑distillation, offering a principled way to incorporate full trajectories without sacrificing the simplicity of prefix‑only training. By separating privileged trajectory variation from general policy shifts, PAST provides a more efficient and effective teacher that respects the student’s learning dynamics.

## Related Concepts  
- On‑policy self‑distillation (OPSD)  
- Privileged adaptation  
- Trajectory conditioning  
- Forward‑KL projection  
- Student‑proximity regularization  
- Distillation prefixes  
- Next‑token distribution

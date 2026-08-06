# Summary: 2026-08-05_12-59-10Z_Privileged_butBiased_HowPI_ConditionedTeachersBrea.md
Saved: 2026-08-05 20:36
Source: 2026-08-05_12-59-10Z_Privileged_butBiased_HowPI_ConditionedTeachersBrea.md
Model: None

---

## Summary  
The paper investigates self‑distillation (SD) when the teacher is conditioned on privileged information (PI), showing that such a setup can produce biased objectives that degrade reasoning performance. It reproduces reported gains in easy settings but fails to improve validation accuracy—or even causes it to drop—on difficult tasks across multiple domains and model sizes. The authors introduce a PI Bias Score to quantify how much the teacher’s per‑token target is pulled toward a specific reference solution rather than toward correctness. They demonstrate that this bias leads students to optimize low‑information tokens, penalizing reasoning hesitation, resulting in a flatter, less decisive student.

## Key Contributions  
- [Finding 1] Self‑distillation with PI‑conditioned teachers fails on difficult tasks; validation accuracy does not improve and often degrades.  
- [Finding 2] The teacher’s per‑token target is biased toward the specific reference solution, quantified by a PI Bias Score, causing the student to ignore correctness.  
- [Finding 3] The resulting loss focuses on low‑information tokens (stopwords, punctuation) rather than answer‑determining tokens, leading to a less decisive model.

## Methodology  
The authors first reproduce SDPO’s easy‑setting gains and then apply identical configurations—question answering, mathematics, coding, multi‑turn tool use—to hard tasks. They vary reasoning modes, model sizes, forms of PI, and both the SDPO and OPSD recipes while measuring per‑token loss and validation accuracy. To capture teacher bias they compute a PI Bias Score as the cosine similarity between the teacher’s target distribution and a uniform distribution.

## Results  
In easy tasks gains are observed, but in hard tasks the per‑token loss decreases while validation accuracy drops or stays flat. The PI Bias Score is consistently high across settings, indicating strong bias toward the reference trajectory. Token‑wise analysis shows the highest divergence on exploratory tokens (hesitation) rather than on answer tokens, confirming that the student’s objective decouples from task success.

## Significance  
This work reveals a fundamental flaw in assuming self‑distillation alone can improve reasoning; it highlights how privileged information introduces bias unaccounted for, undermining the method’s promise and guiding future RL design toward more robust objectives.

## Related Concepts  
- Self‑distillation (SD)  
- Reinforcement Learning with Verifiable Rewards (RLVR)  
- Privileged Information (PI)  
- Per‑token supervision  
- PI Bias Score  
- Self‑teacher  
- OPSD  
- SDPO

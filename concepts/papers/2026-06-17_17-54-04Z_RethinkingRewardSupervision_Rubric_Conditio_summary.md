# Summary: 2026-06-17_17-54-04Z_RethinkingRewardSupervision_Rubric_ConditionedSelf.md
Saved: 2026-06-17 22:01
Source: 2026-06-17_17-54-04Z_RethinkingRewardSupervision_Rubric_ConditionedSelf.md
Model: None

---


## Summary  
The paper proposes Rubric‑Conditioned Self‑Distillation to improve reasoning model post‑training by replacing scalar rewards with structured rubrics that specify fine‑grained criteria. It conditions a teacher model on these rubrics to give token‑level guidance during self‑distillation, avoiding the limitations of chain‑of‑thought annotations or single‑scalar RL. The framework learns task‑specific rubrics and then uses them to guide a student reasoner’s generation. Experiments show it outperforms GRPO and OPSD on science reasoning benchmarks.

## Key Contributions  
- Rubric‑conditioned self‑distillation provides fine‑grained, criterion‑level supervision instead of scalar rewards.  
- The method learns task‑specific rubrics before training the reasoner, enabling richer feedback.  
- It achieves higher performance than GRPO and OPSD on multiple benchmarks.

## Methodology  
The authors first design a two‑stage pipeline. Stage 1 uses supervised fine‑tuning to generate rubric vectors that encode which aspects of reasoning (e.g., correctness, logical flow) should be emphasized. These rubrics are then used as conditioning signals in the teacher model’s output token predictions during on‑policy self‑distillation. The student reasoner samples trajectories and receives token‑level guidance based on the active rubric, allowing the model to improve specific criteria rather than a single overall score.

## Results  
On a suite of science reasoning benchmarks (e.g., ScienceQA, GSM8K), Rubric‑Conditioned Self‑Distillation yields an average improvement of 1.0 points over GRPO and 0.9 points over OPSD, surpassing prior methods in both absolute and relative terms.

## Significance  
This work demonstrates that structured, rubric‑based supervision can unlock finer control over reasoning processes, moving beyond the limitations of scalar reward signals and noisy chain‑of‑thought annotations. It offers a scalable way to align model outputs with complex, multi‑dimensional criteria.

## Related Concepts  
Rubric conditioning, self‑distillation, on‑policy RL, token‑level guidance, verification rewards, chain‑of‑thought reasoning.

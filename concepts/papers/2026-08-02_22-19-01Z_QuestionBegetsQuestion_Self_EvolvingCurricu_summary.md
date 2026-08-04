# Summary: 2026-08-02_22-19-01Z_QuestionBegetsQuestion_Self_EvolvingCurriculumforR.md
Saved: 2026-08-03 23:16
Source: 2026-08-02_22-19-01Z_QuestionBegetsQuestion_Self_EvolvingCurriculumforR.md
Model: None

---

## Summary  
The paper tackles three persistent obstacles in teaching a language model a new skill: limited training data, the absence of ground‑truth reasoning traces, and a performance ceiling that stalls improvement despite more data. To address these issues, the authors introduce Question‑begets‑Question (QbQ), a scalable curriculum that generates diverse problem variants from existing ones, and fine‑tune Qwen2.5‑Math‑7B on AIME using reinforcement learning without any teacher reasoning traces. Their central claim is that this ceiling is not intrinsic to the model; a self‑evolving curriculum can break it and push pass@1 beyond 16 %.  

## Key Contributions  
- [Finding 1] The performance plateau observed in static training is not an inherent limitation of Qwen2.5‑Math‑7B but a data‑driven effect that can be overcome with a dynamic curriculum.  
- [Finding 2] Training the model on problem variants of questions it already solves most correctly enables it to improve and subsequently tackle harder, unseen problems.  
- [Finding 3] A self‑evolving curriculum—re‑evaluating checkpoints each round and seeding QbQ from high‑confidence problems—lifts pass@1 from a baseline of 5.6 % to 16.5 % after twenty rounds with no sign of saturation.  

## Methodology  
The authors employ a teacher that transforms existing competition mathematics problems into multiple variants, preserving the underlying skill while increasing diversity. The model is fine‑tuned exclusively via reinforcement learning on problem statements and final answers; no explicit reasoning traces are used. In each training round, the current checkpoint is evaluated to identify which original problems it can answer with high confidence, those instances become seeds for QbQ generation, and the resulting variants constitute the next batch of data. This iterative process creates a self‑evolving curriculum that adapts to the model’s evolving competence.  

## Results  
Baseline static training on real‑plus‑synthetic data yields pass@1 up to 14.5 %, still far below the task difficulty. The self‑evolving curriculum, with an identical data budget, reaches 16.5 % pass@1 after twenty rounds and shows no further improvement, indicating that the ceiling is broken. Moreover, models trained this way solve harder problems never seen during training, suggesting genuine skill transfer beyond memorization.  

## Significance  
The work demonstrates that data scarcity and performance plateaus in reinforcement‑learning fine‑tuning can be mitigated by a curriculum that continuously re‑evaluates model capability and generates task‑relevant variants. This approach offers a practical strategy for scaling language models on niche, high‑stakes tasks where labeled reasoning traces are unavailable.  

## Related Concepts  
QbQ (Question‑begets‑Question), reinforcement learning fine‑tuning, self‑evolving curriculum, partial credit, performance ceiling, scaling laws, AIME competition mathematics, teacher‑generated variants, dynamic curriculum evaluation.

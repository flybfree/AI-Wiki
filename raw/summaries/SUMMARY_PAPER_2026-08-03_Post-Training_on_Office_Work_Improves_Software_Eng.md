---
title: Post-Training on Office Work Improves Software Engineering: A Behavioral Account of Cross-Domain Transfer
url: http://arxiv.org/abs/2608.01604v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_02-22-02Z_Post_TrainingonOfficeWorkImprovesSoftwareEngineeri.md
generated_at: 2026-08-03 23:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether long‑horizon post‑training improves a model’s ability to transfer skills from office workflows to software engineering tasks. It shows that after fine‑tuning Qwen3.5 on 363 Long‑Horizon Multi‑Tool Agent tasks, the model’s pass@1 score on SWE‑Bench Pro rises by five point eight points, indicating a measurable boost in performance.

## Key Takeaways
- The post‑training process strengthens four GDE behaviors—goal selection, state construction, fidelity maintenance, and verification—across both office workflows and software repositories.  
- The improvement is consistent across all tasks, suggesting the model reorganizes knowledge to support long‑horizon execution beyond its original domain.  
- Aggregate SWE‑Bench Pro results show gains in information gathering, implementation, and verification, aligning with the behavioral changes observed.

## Context
Long‑horizon task performance remains a challenge for large language models because they often lose coherence when tasks diverge. This study provides evidence that post‑training can enhance cross‑domain transfer by reinforcing structured behaviors rather than merely memorizing content. The findings contribute to understanding how training data diversity influences model adaptability.

## Implications
For industry practitioners, the results suggest that enriching fine‑tuning datasets with long‑horizon office tasks may improve software engineering outcomes without retraining from scratch. It also signals a shift toward evaluating models on behavioral consistency rather than just static metrics, guiding future research and deployment strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01604v1)

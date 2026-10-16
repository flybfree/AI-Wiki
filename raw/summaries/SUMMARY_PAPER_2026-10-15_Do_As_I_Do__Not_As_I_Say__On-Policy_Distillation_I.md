---
title: Do As I Do, Not As I Say: On-Policy Distillation Inherits the Teacher in Vision-Language Models
url: http://arxiv.org/abs/2610.20989v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_22-04-32Z_DoAsIDo_NotAsISay_On_PolicyDistillationInheritsthe.md
generated_at: 2026-10-15 22:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how on-policy distillation (OPD) transfers teacher behavior to student vision-language models, comparing it against filtered supervised fine-tuning (SFT) across tasks with varying teacher reliability. The authors find that OPD is only effective when the teacher remains reliable on student-generated trajectories, and that OPD can actually erase completion behaviors previously learned through SFT, effectively inheriting the teacher's failure modes rather than just its knowledge.

## Key Takeaways
- On ChartQA, where the teacher successfully completes 99% of its solutions, OPD trained on only 10% of the data achieves performance within 1.4 accuracy points of full-data SFT, demonstrating that OPD can be highly data-efficient when the teacher is consistently reliable on the states the student visits.
- On Geometry3K, where the teacher fails to complete 22% of its solutions, OPD underperforms SFT by 7.9 accuracy points, with the majority of this performance gap attributable to incomplete responses inherited from the teacher's failures on student-generated trajectories rather than a lack of knowledge transfer.
- Starting OPD from a model already fine-tuned via SFT causes the student's completion rate to drop from 76% to 62%, effectively erasing the completion behavior learned during SFT. Filtering teacher demonstrations for completeness alone recovers much of SFT's advantage, indicating that the problem is not the on-policy mechanism itself but the propagation of teacher failure modes through student-visited states.

## Context
Post-training strategies for vision-language models increasingly rely on distillation from stronger teacher models, with SFT and OPD representing two dominant paradigms. While OPD has been promoted as a more data-efficient alternative because it supervises the student's own trajectories rather than fixed teacher demonstrations, this paper provides the first controlled comparison isolating how teacher reliability at each state shapes the student's learned behavior. This matters because the assumption that on-policy supervision is inherently superior has not been rigorously tested against the teacher's own failure patterns on student-generated states.

## Implications
For practitioners deploying VLM post-training pipelines, this work warns that choosing OPD without auditing teacher reliability on student-visited states can silently degrade model completion behavior and introduce persistent failure modes that are difficult to detect. The finding that filtering for completeness recovers SFT's advantage suggests that practitioners should prioritize data quality filtering over the choice of distillation mechanism, and that hybrid approaches combining SFT initialization with carefully filtered OPD may offer the best balance between data efficiency and behavioral consistency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20989v1)

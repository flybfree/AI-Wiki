---
title: Where LLM Graders Succeed and Break: Evidence from Two Computer-Science Exams
published: 2026-09-24T10:07:57Z
authors: Ali Habibullah, Yazan Alshoibi, Mohammad Alshiekh, Salman Khan, Naeemullah Khan
url: http://arxiv.org/abs/2609.29333v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where LLM Graders Succeed and Break: Evidence from Two Computer-Science Exams

## Abstract
One long-form exam in a large course costs hundreds of grader-hours, and qualified graders are scarce; LLM graders are a tempting alternative. To show its pitfalls we grade a practical Computer Vision exam ($570$ dual-graded students) under $171$ configurations spanning closed and open-weights models; the best reaches mean absolute error $1.64/35$, below the $2.61/35$ two human graders achieve against each other. The catch is the prompt: a short ''strict grader'' preamble drives $14$ of $17$ open-weights models out of the graded band ($\text{MAE} \ge 8$), three stopping grading altogether. The damage traces to the preamble's two credit-withholding sentences, not to tone or model scale; one of them, ''never give partial credit'', alone makes two of three probed models stop grading. The closed flagships of three vendors shift calibration under it but stay in the band. In $162$ further configurations on a second, independent Machine Learning exam from another course ($1{,}038$ dual-graded students), the preamble worsens ten models, moving three out of the band into collapse and one into refusal, yet improves seven whose neutral prompts over-mark: the vulnerability replicates, but its direction is exam-specific. Light LoRA fine-tuning repairs it: one adapter on the two exams' pooled $\sim 3{,}900$ graded examples brings five small open models to parity or better with a human grader in agreement with the grader pair, and sensitivity to the three harsh personas nearly vanishes ($\le 0.32$ MAE). We release the anonymised dataset, full ablation grid, and grading, fine-tuning and analysis pipelines.

## Metadata
- **Published**: 2026-09-24T10:07:57Z
- **Authors**: Ali Habibullah, Yazan Alshoibi, Mohammad Alshiekh, Salman Khan, Naeemullah Khan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.29333v1)
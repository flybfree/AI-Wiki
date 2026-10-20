---
title: Does Unlearning Survive Collaboration? Robust Unlearning for Shared-Model LLM Teams
published: 2026-10-19T03:33:58Z
authors: Hengsong Liu, Liangyu Teng, Jingnan Cai, Yuntian Shi, Jingyu Zhang, Yang Liu, Jing Liu, Liang Song
url: http://arxiv.org/abs/2610.25731v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does Unlearning Survive Collaboration? Robust Unlearning for Shared-Model LLM Teams

## Abstract
LLM unlearning is essential for removing sensitive or unwanted knowledge while preserving useful capabilities. As LLM teams are increasingly used to solve complex problems, forgetting must remain effective during collaboration. Despite advances in forgetting effectiveness, efficiency, and robustness to relearning, team deployment remains underexplored. We find that collaboration weakens forgetting: final-answer evaluations miss recoverable evidence in team messages, including complementary clues supporting joint recovery. We establish theoretically and confirm empirically that controlling final answers or individual messages does not ensure low recovery from their combination. To address this challenge, we propose Aggregation-Conditioned Unlearning (ACU). ACU trains a shared model using reconstruction feedback from individual and pooled messages, prioritizes views with higher recovery risk, and uses replacement-based credit assignment while protecting direct and collaborative utility. TOFU evaluates trajectory-level recovery, while WMDP-bio tests native forgetting and retained utility. On TOFU, ACU lowers full-trajectory recovery from 41.8% to 19.3% in ROUGE-L recall and factual recovery from 34.2% to 18.7% versus output-supervised training, with comparable retained-task performance. These results demonstrate that ACU curbs information leakage in LLM teams and generalizes across team sizes and readers.

## Metadata
- **Published**: 2026-10-19T03:33:58Z
- **Authors**: Hengsong Liu, Liangyu Teng, Jingnan Cai, Yuntian Shi, Jingyu Zhang, Yang Liu, Jing Liu, Liang Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25731v1)
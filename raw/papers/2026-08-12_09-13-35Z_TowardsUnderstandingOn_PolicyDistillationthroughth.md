---
title: Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling
published: 2026-08-12T09:13:35Z
authors: Xinmu Ge, Zizhuo Zhang, Yu Huang, Jianing Zhu, Lin Yuan, Wanli Gu, Weichang Wu, Weiran Huang, Xiaolu Zhang, Bo Han, Jun Zhou, Jiangchao Yao
url: http://arxiv.org/abs/2608.11829v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling

## Abstract
On-policy distillation (OPD) has emerged as a promising post-training technique for enhancing LLM reasoning. It is commonly believed to enable the student model to distill knowledge from a stronger teacher model, thereby expanding capabilities beyond the pre-OPD base model. In this study, we examine this view through the lens of test-time scaling by varying the sampling budget K and evaluating performance with pass@K and avg@K. Specifically, across several OPD variants, we observe that OPD-trained models maintain superior avg@K performance across sampling budgets, while the advantage in pass@K gradually shifts to the pre-OPD base models as K increases. These results suggest that OPD primarily improves sampling efficiency rather than consistently expanding the student's reasoning capability boundary. The pass@K dynamics throughout OPD training further reveal a progressive shift toward stronger small-K performance at the expense of the large-K capability boundary. Furthermore, a problem-level solvability analysis using pass@1024 as the criterion reveals an asymmetry: OPD causes more previously solvable problems to become unsolvable than previously unsolvable problems to become solvable. Together, these findings suggest that, from the perspective of capability expansion, OPD behaves more like an "illusory distillation": its apparent gains arise primarily from improved sampling efficiency rather than from acquiring genuinely new reasoning capabilities from the teacher.

## Metadata
- **Published**: 2026-08-12T09:13:35Z
- **Authors**: Xinmu Ge, Zizhuo Zhang, Yu Huang, Jianing Zhu, Lin Yuan, Wanli Gu, Weichang Wu, Weiran Huang, Xiaolu Zhang, Bo Han, Jun Zhou, Jiangchao Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11829v1)
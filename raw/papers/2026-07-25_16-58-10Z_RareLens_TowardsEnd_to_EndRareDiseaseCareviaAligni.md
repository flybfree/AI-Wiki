---
title: RareLens: Towards End-to-End Rare Disease Care via Aligning Divergent Large Language Model Reasoning
published: 2026-07-25T16:58:10Z
authors: Xi Chen, Hongru Zhou, Shiyu Feng, Hanyu Zhou, Huahui Yi, Rongsheng Wang, Tiancheng He, Kun Wang, Pingping Liu, Qiankun Li, Sicheng Lin, Huiying Ou, Xiaohong Zheng, Tianying Zang, Zhuohang Wu, Leheng Jiang, Kexin Cao, Wenhan Zhang, ChengYi Li, Zhiyang Wang, Songlin Li, Benyou Wang, Ningbei Yin, Shaoting Zhang, Weili Fu, Jian Li, Kang Li
url: http://arxiv.org/abs/2607.23290v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RareLens: Towards End-to-End Rare Disease Care via Aligning Divergent Large Language Model Reasoning

## Abstract
Rare diseases collectively affect an estimated 3.5% to 5.9% of the population, yet more than 70% of patients are misdiagnosed and many endure years of evaluation before a diagnosis is reached, because early presentations are nonspecific and relevant expertise is scarce and unevenly distributed. Artificial intelligence could provide support, but existing systems address isolated stages of care, overwhelmingly diagnosis. They typically depend on the results of downstream investigations, and they treat the variability between models as noise to be eliminated. Here we present RareLens, a system that supports clinical decision-making across the entire rare disease trajectory by exploiting this variability. When heterogeneous large language models evaluate the same case, they generate divergent but complementary reasoning, which RareLens aligns and calibrates into a single convergent, actionable decision at each stage. Four coordinated modules perform primary-visit risk screening, diagnosis, treatment planning and prognosis. Developed and evaluated on RareBench, a real-world dataset of 157,525 cases spanning all 33 Orphanet categories and more than 7,000 conditions, RareLens outperformed every frontier model tested, including GPT-5, DeepSeek-R1, Claude-3.7-Sonnet and Gemini-2.5-Pro, at each stage. It achieved an area under the curve of 0.917 for screening and top-1 accuracies of 65.5% and 89.8% for diagnosis and treatment. In an external study spanning 1,287 cases and 23 physicians, autonomous RareLens and physicians assisted by RareLens both substantially outperformed unaided physicians. These findings indicate that aligning divergent model reasoning, rather than scaling a single model, offers a generalizable strategy for high-uncertainty clinical decision-making.

## Metadata
- **Published**: 2026-07-25T16:58:10Z
- **Authors**: Xi Chen, Hongru Zhou, Shiyu Feng, Hanyu Zhou, Huahui Yi, Rongsheng Wang, Tiancheng He, Kun Wang, Pingping Liu, Qiankun Li, Sicheng Lin, Huiying Ou, Xiaohong Zheng, Tianying Zang, Zhuohang Wu, Leheng Jiang, Kexin Cao, Wenhan Zhang, ChengYi Li, Zhiyang Wang, Songlin Li, Benyou Wang, Ningbei Yin, Shaoting Zhang, Weili Fu, Jian Li, Kang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23290v1)
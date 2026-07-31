---
title: AutoSupervision: Closing the Feedback Loop in Scientific Workflows with Grounded Revision Verification
published: 2026-07-30T08:24:58Z
authors: Haobo Li, Eunseo Jung, Wenxiao Zhao, Feng Liu, Jiong Wang, Kaiyi Xu, Zijie Guo, Zixin Chen, Ben Fei, Fenghua Ling, Lei Bai
url: http://arxiv.org/abs/2607.27845v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoSupervision: Closing the Feedback Loop in Scientific Workflows with Grounded Revision Verification

## Abstract
Recent advances in large language models (LLMs) have enabled AI systems to assist scientific research and peer review. However, an essential capability for reliable AI-assisted scientific workflows remains underexplored: verifying whether reviewer feedback leads to meaningful and evidence-supported manuscript improvements. We introduce AutoSupervision, which evaluates whether scientific manuscript revisions genuinely address reviewer concerns through grounded evidence. AutoSupervision leverages transparent peer-review records as a natural source of supervision, where reviewer comments specify scientific concerns, author responses describe claimed resolutions, and revised manuscripts provide evidence of changes. Given reviewer comments, author responses, and revised manuscripts, models must characterize reviewer concerns, determine whether concerns have been addressed, and identify supporting manuscript evidence. We construct AutoSupervision from 56,000 Nature Communications articles and corresponding review records. Then we conducted experiments on LLMs, the ablation study, and the case study. Our results show that while LLMs perform well in characterizing reviewer concerns, with GPT-5.5 achieving a score of 0.754, evidence-based verification remains the primary bottleneck, with the best-performing model reaching only 0.501.

## Metadata
- **Published**: 2026-07-30T08:24:58Z
- **Authors**: Haobo Li, Eunseo Jung, Wenxiao Zhao, Feng Liu, Jiong Wang, Kaiyi Xu, Zijie Guo, Zixin Chen, Ben Fei, Fenghua Ling, Lei Bai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27845v1)
---
title: Can Vision-Language Models Stay Helpful When Facing Implicit Risks? Intent-Privilege OPSD for Efficient Safety-Helpfulness Alignment
published: 2026-09-29T15:38:25Z
authors: Haotian Deng, Wenbin Xing, Gang Xu, Tao He, Jinkai Zheng, Chun Li, Zheng Zhu, Ming Li
url: http://arxiv.org/abs/2609.37837v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Vision-Language Models Stay Helpful When Facing Implicit Risks? Intent-Privilege OPSD for Efficient Safety-Helpfulness Alignment

## Abstract
Vision-Language Models (VLMs) remain vulnerable to cross-modal implicit risks: visual and textual inputs that appear benign in isolation can jointly elicit unsafe responses. Existing safety methods often require large preference datasets, costly multi-rollout training, or additional safeguards at inference time. They may also sacrifice helpfulness by directly refusing requests that could be answered safely. In this paper, we propose Intent-Privilege On-Policy Self-Distillation (OPSD), which leverages evidence-grounded intent as privileged supervision during training to help VLMs recognize implicit risks and provide safe, useful responses instead of blanket refusals. OPSD distills a teacher's intent-conditioned preferences over responses into a student using a single rollout per prompt; the student then responds without intent annotations or an additional safety module. With only 1,447 safety-specific examples - 95% fewer than standard preference datasets - OPSD reduces training time by 5x relative to multi-rollout GRPO-style training and average inference length by 7%. It attains the highest ratio for joint safety-helpfulness success, which measures the proportion of responses that are both safe and helpful, across all five evaluation groups. Remarkably, on pooled SIUO+HoliSafe, this success ratio rises from 43.9% to 53.5%. These results show that training-time intent supervision can improve both safety and helpfulness while substantially reducing data, training, and inference costs.

## Metadata
- **Published**: 2026-09-29T15:38:25Z
- **Authors**: Haotian Deng, Wenbin Xing, Gang Xu, Tao He, Jinkai Zheng, Chun Li, Zheng Zhu, Ming Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37837v1)
---
title: VISTA: Verifier-Informed Student-to-Teacher Adaptation for On-Policy Self-Distillation
published: 2026-08-28T13:10:34Z
authors: Zewen Ding, Zezhong Wu, Zhou Tao, Shida Wang, Shizhuo Hou, YongXiang Hua, Haoyu Cao, Linli Xu
url: http://arxiv.org/abs/2608.28306v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VISTA: Verifier-Informed Student-to-Teacher Adaptation for On-Policy Self-Distillation

## Abstract
On-policy self-distillation (OPSD) improves reasoning by training a problem-only student on its own rollouts using dense token-level supervision from a privileged teacher that also sees a reference solution. However, standard OPSD treats the teacher distribution as a fixed target along the student's rollout and updates only the student %, although -- even though privileged conditioning does not guarantee that the teacher always provides the most appropriate target for problem-only reasoning. This one-way supervision can therefore misdirect the student when the teacher distribution is misaligned with valid student reasoning. We therefore introduce Verifier-Informed Student-to-Teacher Adaptation (VISTA), which preserves the standard OPSD student update while using outcome-verified rollouts to adapt the teacher toward the student distribution. Within each verified rollout, VISTA further restricts this adaptation to the top-$k$ positions with the largest teacher--student KL divergence. Notably, VISTA reuses the rollout and loss function from standard OPSD, introducing no additional sampling or separate reward objective. Across AIME24, AIME25, and HMMT25 with Qwen3 models at 1.7B, 4B, and 8B, VISTA achieves the highest Avg@12 at every scale, improving over OPSD by $0.6$, $0.7$, and $2.1$ points, respectively. These results demonstrate the value of student supervision from outcome-verified rollouts and highlight student-to-teacher adaptation as a promising direction for OPSD.

## Metadata
- **Published**: 2026-08-28T13:10:34Z
- **Authors**: Zewen Ding, Zezhong Wu, Zhou Tao, Shida Wang, Shizhuo Hou, YongXiang Hua, Haoyu Cao, Linli Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28306v1)
---
title: Self-Supervised Visual On-Policy Distillation
published: 2026-08-14T09:52:01Z
authors: Yijiang Li, Yijun Liang, Yunjie Tian, Bingyang Wang, Ke Zhang, Zhenfei Yin, Di Fu, Philip Torr, Nuno Vasconcelos
url: http://arxiv.org/abs/2608.14144v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Supervised Visual On-Policy Distillation

## Abstract
Visual on-policy distillation relies heavily on an informative teacher-student asymmetry, through either a larger, stronger teacher or privileged supervision, such as reference answers or ground-truth regions of interest. This raises a fundamental question: where can informative asymmetry come from when nothing privileged is available? We answer this by inverting where the asymmetry comes from. Rather than adding privileged information to the teacher, we subtract information from the student. This asymmetry creates the same effective learning signal for free as a teacher with access to information unavailable to the student, without ground-truth annotations, rewards, or a separate stronger teacher model. Building on this principle, we introduce Self-Supervised Visual On-Policy Distillation (S$^2$VOPD), a simple yet effective method that constructs on-policy learning signals from asymmetric augmented views. S$^2$VOPD distills the teacher's distribution conditioned on the original image on-policy into the student distribution conditioned on a strongly augmented view of the same image. We systematically explore a broad design space of visual augmentations and uncover that (1) asymmetry matters: all four augmentation families improve performance, while symmetric self-distillation degrades it; (2) strength matters: performance peaks at a moderate strength; and (3) the gap must remain task-consistent: augmentations that completely remove the question-relevant evidence can induce large but uninformative discrepancies. Across six fine-grained perception benchmarks, S$^2$VOPD improves Qwen3.5-4B from 70.7% to 77.4%, above all open-source models compared, up to Qwen3-VL at 235B, and surpasses GPT-5.4. While holding training data the same, it recovers 96% of the improvement achieved by methods with privileged information. Website is at https://williamium3000.github.io/s2vopd

## Metadata
- **Published**: 2026-08-14T09:52:01Z
- **Authors**: Yijiang Li, Yijun Liang, Yunjie Tian, Bingyang Wang, Ke Zhang, Zhenfei Yin, Di Fu, Philip Torr, Nuno Vasconcelos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14144v1)
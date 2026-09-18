---
title: What Does Privileged Information Add to On-Policy Self-Distillation?
url: http://arxiv.org/abs/2609.20612v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-17_15-57-10Z_WhatDoesPrivilegedInformationAddtoOn_PolicySelf_Di.md
generated_at: 2026-09-17 21:21
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates the specific contribution of privileged information—such as full reasoning traces or polished solutions—to on-policy self-distillation (OPSD) in language models. By utilizing a custom dataset called AMPLE-Math, the authors evaluate how much "extra" information actually improves student model performance compared to standard reference-free distillation techniques.

## Key Takeaways
- The researchers developed AMPLE-Math, a specialized suite of 5,319 mathematical problems featuring six different reasoning views that share identical answers, allowing for a controlled comparison between various distillation methods.
- The study found that reference-free distillation accounts for a significant portion of the performance improvements in models like Qwen3-1.7B, suggesting that much of the gain comes from the distillation process itself rather than the specific "privileged" information provided by the teacher.
- While providing full reasoning traces did offer some benefits—such as a two percentage point increase for SmolLM3-3B at step 50—the overall impact was found to be relatively modest compared to other factors like student training status and rollout types.
- The findings suggest that the primary value of a privileged reference is its ability to facilitate cross-mode transfer, helping the student access existing reasoning capabilities through parameters shared by direct-response and thinking-enabled inference.

## Context
As the AI community works toward creating more capable and efficient small language models (SLMs), understanding the mechanics of self-distillation is critical for optimizing training costs and performance. This paper addresses a fundamental question in machine learning: whether providing "more" data to a student model actually improves its reasoning or if it simply provides a shortcut that doesn't translate into better general capabilities.

## Implications
For AI researchers and practitioners, these findings suggest that the focus of self-distillation should shift toward improving cross-mode transfer rather than just increasing the amount of reference information provided during training. These insights could lead to more efficient training methodologies for small models where data efficiency is paramount, helping developers understand which specific components of a teacher's output are most effective for student learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.20612v1)

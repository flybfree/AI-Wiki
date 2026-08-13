---
title: AWARe: Mitigating Catastrophic Forgetting via Activation-Weighted Adaptive REtention
published: 2026-08-12T07:55:15Z
authors: Juncheng Liao, Jinfan Lv, Guoming Wang, Jupeng Zheng, Ling Xiao, Siliang Tang
url: http://arxiv.org/abs/2608.11758v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AWARe: Mitigating Catastrophic Forgetting via Activation-Weighted Adaptive REtention

## Abstract
Multimodal Large Language Models (MLLMs) exhibit strong generalization and reasoning abilities due to large-scale multimodal pre-training. However, fine-tuning these models on downstream tasks often leads to catastrophic forgetting, where newly learned task-specific knowledge degrades previously acquired capabilities. This issue arises because gradient updates for new tasks overwrite parameters critical to prior knowledge, limiting the practical deployment of MLLMs. To address this challenge, we propose Activation-Weighted Adaptive REtention (AWARe), a fine-tuning method that mitigates catastrophic forgetting by dynamically controlling parameter updates based on activation patterns. AWARe assigns activation-based importance scores to parameters, selectively freezing those essential for preserving prior capabilities while allowing less important parameters to adapt to new tasks. Importantly, AWARe operates without modifying model architectures, ensuring compatibility with existing inference engines. Extensive experiments demonstrate that AWARe effectively preserves upstream capabilities while achieving superior downstream performance compared to existing methods. Code is available at https://github.com/kaln27/AWARe.

## Metadata
- **Published**: 2026-08-12T07:55:15Z
- **Authors**: Juncheng Liao, Jinfan Lv, Guoming Wang, Jupeng Zheng, Ling Xiao, Siliang Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11758v1)
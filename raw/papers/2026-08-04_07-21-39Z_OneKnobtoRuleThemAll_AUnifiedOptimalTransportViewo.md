---
title: One Knob to Rule Them All: A Unified Optimal Transport View of Cold-Start Active Learning
published: 2026-08-04T07:21:39Z
authors: Ning Zhu, Xiaochuan Ma, Juntao Xu, Jingze Liang, Mengfei Zhao, An Chen, Liang-Jian Deng
url: http://arxiv.org/abs/2608.03249v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Knob to Rule Them All: A Unified Optimal Transport View of Cold-Start Active Learning

## Abstract
Cold-Start Active Learning (CSAL) aims to select a valuable subset from an unlabeled pool without any prior knowledge or human assistance. Existing methods take diverse routes based on typicality, coverage, or diversity. Each rests on its own inductive bias and therefore performs well on some tasks yet poorly on others. We argue that the real challenge is not to design yet another selection heuristic, but to make CSAL adapt automatically to the data and task at hand. To this end, we revisit CSAL through the lens of optimal transport. First, we propose a generalized transport selection framework that reveals the shared allocation structure of existing methods and exactly subsumes representative formulations. Second, we introduce a theoretical analysis that characterizes the trade-off controlled by entropic regularization and establishes a task-agnostic minimax bound for cold-start selection. These results provide a principled foundation for adapting the regularization strength to the unlabeled data. Third, we derive a data-adaptive regularization rule and present a novel Sinkhorn-based CSAL algorithm, termed $ε$-Adaptive Selection ($ε$-AS). Extensive experiments on six public datasets and multiple annotation budgets show that $ε$-AS consistently achieves state-of-the-art performance. On ImageNet-1k, it improves the average accuracy over ActiveFT by 1.29% while reducing selection time by 56.2%. Code will be released at https://github.com/Z-yiwei/OT-CSAL

## Metadata
- **Published**: 2026-08-04T07:21:39Z
- **Authors**: Ning Zhu, Xiaochuan Ma, Juntao Xu, Jingze Liang, Mengfei Zhao, An Chen, Liang-Jian Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03249v1)
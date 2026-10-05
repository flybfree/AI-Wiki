---
title: When History Fails to Become Experience: Action Calibration in Language Agents
published: 2026-10-02T03:50:34Z
authors: Jingyu Liu, Zhiwen Wang, Yuxin Jing, Huanyu Zhou, Yong Liu
url: http://arxiv.org/abs/2610.02769v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When History Fails to Become Experience: Action Calibration in Language Agents

## Abstract
Language agents should draw on prior attempts and environmental feedback to improve subsequent decisions within the same task. However, providing additional interaction history can sometimes reduce task success, suggesting that agents do not consistently use this information effectively. To investigate this limitation, we examine how agents use history. We find that history improves task completion overall, yet much of this benefit persists even when past actions are shuffled. Disrupting the correspondence between actions and observations causes only a modest decline in task success. We therefore hypothesize that agents do not reliably connect past actions with their outcomes when deciding how to proceed. To test this hypothesis, we explicitly label each returned observation as the outcome of the preceding action. This simple annotation improves task success and reduces next-action repetition without introducing new environmental information. Building on this insight, we introduce a learned calibrator that explicitly reassesses past actions and selectively records experience to guide subsequent decisions, improving task success beyond outcome labeling alone.

## Metadata
- **Published**: 2026-10-02T03:50:34Z
- **Authors**: Jingyu Liu, Zhiwen Wang, Yuxin Jing, Huanyu Zhou, Yong Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02769v1)
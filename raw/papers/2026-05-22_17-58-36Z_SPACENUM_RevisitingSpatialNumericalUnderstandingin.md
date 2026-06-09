---
title: SPACENUM: Revisiting Spatial Numerical Understanding in VLMs
published: 2026-05-22T17:58:36Z
authors: Jianshu Zhang, Yijiang Li, Huifeixin Chen, Haoran Lu, Letian Xue, Bingyang Wang, Han Liu
url: http://arxiv.org/abs/2605.23898v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPACENUM: Revisiting Spatial Numerical Understanding in VLMs

## Abstract
Vision-Language Models (VLMs) are increasingly deployed in embodied environments, where they need produce numerical outputs such as action magnitudes and spatial coordinates. Although these numbers appear meaningful, it remains unclear whether these numerical outputs are genuinely grounded in spatial perception. Therefore, in this work, we revisit spatial numerical understanding through SpaceNum, a unified framework that captures two complementary settings: numbers as dynamic transitions during spatial exploration, and numbers as static layouts in spatial reasoning. We formulate two bidirectional tasks, Num2Space and Space2Num, to evaluate how well VLMs map between vision-side spatial structure and language-side numerical representations. We systematically study whether current VLMs truly understand numerical values in spatial settings. Across dynamic transitions and static layouts, we find that models largely fail to ground numbers in spatial meaning and often perform close to random guess. Through error analysis, reasoning trace analysis, and controlled interventions, we show that current VLMs rely heavily on shallow spatial cues, struggle to build stable coordinate-aware representations, and fail to abstract structured spatial layouts from visual observations. We further show that explicit reasoning provides only marginal gains, while tuning can partially improve spatial numerical understanding and transfer to external spatial reasoning benchmarks.

## Metadata
- **Published**: 2026-05-22T17:58:36Z
- **Authors**: Jianshu Zhang, Yijiang Li, Huifeixin Chen, Haoran Lu, Letian Xue, Bingyang Wang, Han Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23898v1)
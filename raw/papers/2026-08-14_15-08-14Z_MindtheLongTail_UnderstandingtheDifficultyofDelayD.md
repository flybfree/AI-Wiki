---
title: Mind the Long Tail: Understanding the Difficulty of Delay Detection in Business Processes
published: 2026-08-14T15:08:14Z
authors: Keyvan Amiri Elyasi, Lukas Kirchdorfer, Heiner Stuckenschmidt
url: http://arxiv.org/abs/2608.14367v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mind the Long Tail: Understanding the Difficulty of Delay Detection in Business Processes

## Abstract
The early detection of delayed cases in business processes is a critical capability for organizations. Predictive process monitoring (PPM) supports this task by using historical event logs to predict the remaining time of ongoing cases, enabling timely interventions to avoid missed deadlines and service level violations. Although remaining time prediction has advanced considerably through sophisticated deep learning architectures, little is known about the intrinsic difficulty of delay detection itself. Since performance is typically assessed using aggregate metrics, prior work provides limited insight into how models perform across the target distribution, especially on the operationally most critical cases with large delays. In this paper, we address this gap by analyzing the difficulty of delay detection. Across 14 event logs, we show that remaining times are typically strongly right-skewed, with only a small fraction of cases exhibiting large delays. Existing models capture the mode of this distribution well but perform poorly on high-delay cases. We further uncover pronounced heteroscedasticity, showing that predictive uncertainty increases with delay magnitude. Based on these findings, we evaluate approaches to mitigate the imbalance problem, but find only limited benefits, suggesting that the key underlying problem may not be imbalance but higher uncertainty associated with delayed cases. We show that this correlation can be exploited to substantially improve the identification of delayed cases. Overall, our work provides new insights into the sources of difficulty in delay detection and identifies uncertainty-aware modeling as a promising direction for future PPM research.

## Metadata
- **Published**: 2026-08-14T15:08:14Z
- **Authors**: Keyvan Amiri Elyasi, Lukas Kirchdorfer, Heiner Stuckenschmidt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14367v1)
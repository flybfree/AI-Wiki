---
title: Action from Adjacent Set in Physical Space Outperforms the Best Prediction in World Models
published: 2026-07-26T11:11:23Z
authors: Liangyu Li, Qingwen Liu, Mingqing Liu
url: http://arxiv.org/abs/2607.23602v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Action from Adjacent Set in Physical Space Outperforms the Best Prediction in World Models

## Abstract
Controllers based on sampling and latent world models assign a predicted terminal cost to each candidate action sequence, choose the minimum, execute its first action block, and replan. This rule can fail even when the terminal cost perfectly and accurately reflects the true task objective in the physical world. Residual prediction error can give an infeasible sequence an anomalously low cost, and a larger proposal pool gives such errors more chances to outrank feasible alternatives. We call this conditional failure proposal overgeneration. In Cube candidate execution audits, increasing the total proposal budget from 72 to 288 reduces the feasibility of selection by minimum latent cost from .375 to .062 for position targets and from .344 to .031 for targets defined by position and yaw, although every larger pool contains a feasible sequence. We introduce Adjacent Set Action Reconstruction (ASAR). Among proposals with low cost, ASAR measures density from standardized early action prefixes and reconstructs a full sequence from an adjacent set with a light anchor from the sequence with minimum cost. On a Carry and Release evaluation set of 75 queries, Kernel ASAR improves event completion success over matching selection by 28.0, 24.0, and 18.7 percentage points under latent cost and by 18.7, 20.0, and 17.3 points under a trajectory reachability cost at 72, 144, and 288 proposals. Analysis of finite proposal pools characterizes selection risk from the lower tail, separation by a related radius support statistic, and sequence containment under an explicit local feasibility condition.

## Metadata
- **Published**: 2026-07-26T11:11:23Z
- **Authors**: Liangyu Li, Qingwen Liu, Mingqing Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23602v1)
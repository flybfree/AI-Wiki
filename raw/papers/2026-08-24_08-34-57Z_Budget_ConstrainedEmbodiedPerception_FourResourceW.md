---
title: Budget-Constrained Embodied Perception: Four Resource Walls and a Pre-Registered Evaluation of Access-Structured Perception on Open Models at less than 31B
published: 2026-08-24T08:34:57Z
authors: Defu Lin, Wenhui Chen, Ziyao Lin, Jianlin Chen, Peiji Long, Chi Man Vong
url: http://arxiv.org/abs/2608.22975v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Budget-Constrained Embodied Perception: Four Resource Walls and a Pre-Registered Evaluation of Access-Structured Perception on Open Models at less than 31B

## Abstract
Embodied multimodal agents must answer from growing observation streams under a fixed per-decision token budget. We formalize this constraint through four resource walls: a perceptual Shannon wall for bounded state, a horizon wall for query-independent frame selection, a round wall for non-adaptive retrieval, and a conditional composition wall for fixed-depth inference. We introduce ASP, a training-free wrapper for frozen multimodal models that combines a capped structured state, a verbatim episodic index, and query-conditioned budget allocation with iterative access. Following a pre-registered protocol, we evaluate seven open-weight models from 3B to 31B on SEW-Bench, a license-free synthetic long-horizon walkthrough benchmark constructed to instantiate these walls. The registered natural-video benchmarks were not run because their frames require dataset agreements; our evidence therefore concerns access mechanisms, not natural-scene perception. Under a 4,096-token decision budget, ASP reaches 75 to 94% episodic retrieval accuracy, compared with 3 to 19% for equal-budget query-independent sampling, and budget reallocation outperforms quadrupling the sampling budget on every backbone. However, the full three-component architecture does not validate channel duality: removing the compressive state raises the flagship mean from 35.4 to 58.0, ASP does not outperform the verbatim-only baseline on any backbone, and two of four pre-registered falsification criteria fire. These results show that query-conditioned access, rather than parameter count or context growth alone, is decisive under a fixed budget, while prompted online compression does not earn its cost in this setting.

## Metadata
- **Published**: 2026-08-24T08:34:57Z
- **Authors**: Defu Lin, Wenhui Chen, Ziyao Lin, Jianlin Chen, Peiji Long, Chi Man Vong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22975v1)
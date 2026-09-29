---
title: Toward Comprehensive 3D Grounding: Orientation Grounding through Vision-Language Models
published: 2026-09-27T02:29:30Z
authors: Tuo Liang, Disheng Liu, Nengbo Wang, Vipin Chaudhary, Yu Yin
url: http://arxiv.org/abs/2609.33109v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward Comprehensive 3D Grounding: Orientation Grounding through Vision-Language Models

## Abstract
Grounding is a core capability of spatial vision-language models, yet most existing work focuses only on where a referred object is. Many 3D tasks also require knowing how it is oriented. Although existing 3D VLMs may predict oriented boxes, box pose does not explicitly capture object-centric orientation or symmetry-induced ambiguities. We introduce orientation grounding, a referring grounding task that predicts an object's 6D orientation and axial symmetry from a language or box query in single-view or multi-view scenes. To support this task, we construct ReferOri, with 331K multi-view and 387K single-view orientation-grounding queries obtained through scalable reconstruction, consistency checking, and human verification. We further present OG-VLM, which adapts a 3D VLM with structured box/orientation outputs, sign and symmetry tokens, and geometry-aware auxiliary losses. Across single-view and multi-view benchmarks, OG-VLM substantially outperforms orientation-aware VLM baselines and surpasses object-level orientation foundation models on scene-level referring benchmarks, showing that explicit orientation grounding is a distinct and learnable capability beyond localization. Downstream results validate its benefit for orientation-related spatial reasoning.

## Metadata
- **Published**: 2026-09-27T02:29:30Z
- **Authors**: Tuo Liang, Disheng Liu, Nengbo Wang, Vipin Chaudhary, Yu Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33109v1)
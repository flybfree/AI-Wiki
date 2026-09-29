---
title: Toward Comprehensive 3D Grounding: Orientation Grounding through Vision-Language Models
url: http://arxiv.org/abs/2609.33109v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_02-29-30Z_TowardComprehensive3DGrounding_OrientationGroundin.md
generated_at: 2026-09-28 21:56
model: qwen3.6-35b-a3b
---

## Summary
Toward Comprehensive 3D Grounding introduces orientation grounding, a novel task enabling spatial vision-language models to predict an object's precise 6D orientation and axial symmetry alongside localization. The authors release ReferOri, a massive dataset comprising over 700K queries across single- and multi-view scenes, and propose OG-VLM, a model architecture enhanced with structured outputs and geometry-aware losses. Experimental results demonstrate that OG-VLM significantly surpasses existing baselines, proving that explicit orientation prediction is a distinct capability that improves downstream spatial reasoning performance.

## Key Takeaways
- Orientation Grounding Task: The paper defines orientation grounding as predicting an object's 6D orientation and axial symmetry from language or box queries in single- and multi-view scenes, addressing the limitation of standard bounding boxes which fail to capture object-centric orientation and symmetry-induced ambiguities.
- ReferOri Dataset: A comprehensive dataset is constructed featuring 331K multi-view and 387K single-view orientation-grounding queries, generated via scalable reconstruction, rigorous consistency checking, and human verification to ensure high-quality training data for this new task.
- OG-VLM Architecture and Performance: The proposed OG-VLM model adapts a 3D VLM with

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33109v1)

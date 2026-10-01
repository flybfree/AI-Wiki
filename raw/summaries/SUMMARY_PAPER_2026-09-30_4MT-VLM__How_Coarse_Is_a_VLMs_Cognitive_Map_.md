---
title: 4MT-VLM: How Coarse Is a VLMs Cognitive Map?
url: http://arxiv.org/abs/2609.39238v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_08-06-49Z_4MT_VLM_HowCoarseIsaVLMsCognitiveMap.md
generated_at: 2026-09-30 21:58
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces 4MT-VLM, a benchmark dataset designed to evaluate the spatial reasoning capabilities of Vision-Language Models by testing their ability to recognize places from novel viewpoints without relying on appearance cues. Through a four-alternative forced-choice task across procedurally generated landscapes with varying stimulus modes, the study reveals that while current models can identify locations from static views, they fail significantly when the camera rotates, performing below chance levels at moderate angles compared to human observers. This demonstrates that existing VLMs possess only rudimentary cognitive maps with insufficient spatial resolution to maintain a stable 3D understanding of environments under viewpoint changes.

## Key Takeaways
- The authors present 4MT-VLM, a procedurally generated dataset featuring landscapes rendered in five distinct stimulus modes that strip away appearance cues while preserving layout consistency, including conditions like shape-only, color-only, and bare terrain peaks, with the final mode mimicking clinical tests for hippocampal function by placing peaks on the horizon.
- Evaluation across sixteen open and closed-source models shows a stark contrast between human and AI performance; while humans score 85% at a 135-degree rotation, VLMs drop below the 25% chance level, indicating a fundamental inability to track spatial relationships as the

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39238v1)

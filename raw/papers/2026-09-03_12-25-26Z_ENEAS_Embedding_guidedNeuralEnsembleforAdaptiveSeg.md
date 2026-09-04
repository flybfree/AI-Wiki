---
title: ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation
published: 2026-09-03T12:25:26Z
authors: Javier del Pino, Salvador Rodríguez, Alejandro Garabito, Javier Álvarez, Chema Garabito
url: http://arxiv.org/abs/2609.03756v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation

## Abstract
We present ENEAS, a unified, text-promptable method for instance tracking and semantic discovery. Text-promptable segmentation models, including the latest foundation models such as SAM 3, still suffer from temporal hallucinations, spatial fragmentation, and semantic misclassification: they fail to report target absence when an object leaves the field of view, segment local textures instead of the complete object during extreme close-ups, and prioritize visual features over ontological reality, so that visually similar artifacts such as statues, paintings, or reflections are segmented as target entities.   ENEAS works two ways from a single method: precise tracking and high-quality segmentation of a unique instance, and open-concept discovery of every instance a text query names, resolved by a semantic verification layer. For tracking, we extend the geometrically robust SeC architecture, previously limited to point interactions, with a text-prompting adapter and leverage its temporal memory, so that the target is held through disappearance without drifting to distractors and kept whole even when it fills the entire view. For discovery, the verification layer combines high-speed visual embedding matching with conditional VLM refinement, invoking semantic reasoning only for ambiguous candidates, which filters out the ontological errors that visual-only models cannot distinguish while keeping latency low. Designed with 3D reconstruction in mind, where a single misclassified distractor corrupts the asset, ENEAS unlocks high-quality semantic tracking and segmentation of video, of broad libraries, and of collections of temporally or spatially unordered data, together with the discrimination to tell true instances from their doppelgangers: things that look alike but are not the same. The code and models are available at https://github.com/speridlabs/eneas

## Metadata
- **Published**: 2026-09-03T12:25:26Z
- **Authors**: Javier del Pino, Salvador Rodríguez, Alejandro Garabito, Javier Álvarez, Chema Garabito
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03756v1)
---
title: V2TATC: A Joint Voice-Trajectory Embedding Framework and Dataset for Air Traffic Controller Situational Awareness
published: 2026-08-29T01:22:52Z
authors: Louis Brusset, Mathurin Petit, Jordan Kam, Alexandre Bayen
url: http://arxiv.org/abs/2608.28981v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# V2TATC: A Joint Voice-Trajectory Embedding Framework and Dataset for Air Traffic Controller Situational Awareness

## Abstract
As air traffic volumes in the National Airspace System continue to expand, in particular in the low altitude airspaces, the need for scalable decision support tools used by air traffic controllers will also require more development. This article introduces Voice-to-Trajectory for Air Traffic Control, a joint voice communication-flight trajectory data embedding framework, that can be a component of situational awareness in congested airspaces, and assist the development of tools for ATC as they reason in real-time over Automatic Dependent Surveillance-Broadcast trajectories, or the intent expressed by pilots in natural language. We show that these data modalities are not independent and represent a common physical referent: an aircraft flying through the airspace. V2TATC maps a voice instruction and the trajectory of the addressed aircraft to nearby points in a single latent space that can be queried in both directions. It combines a self-supervised trajectory encoder, a frozen large-scale speech encoder, a contrastive joint embedding, and a bijective lifting via normalizing flows. We demonstrate V2TATC's effectiveness on the San Francisco Bay Area, for its concentration of major airports, and its mix of commercial and general aviation low altitude traffic. Lastly, we release a novel paired voice-trajectory dataset, and report experiments on cross-modal retrieval, ablations, and latent-space analysis.

## Metadata
- **Published**: 2026-08-29T01:22:52Z
- **Authors**: Louis Brusset, Mathurin Petit, Jordan Kam, Alexandre Bayen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28981v1)
---
title: Sparse Autoencoders Encode Both Concepts and Functions: The Downstream Geometry of Feature Effects
published: 2026-07-27T16:45:08Z
authors: Phu Gia Hoang, Anwoy Chatterjee, Tanmoy Chakraborty, Iryna Gurevych, Subhabrata Dutta
url: http://arxiv.org/abs/2607.24645v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sparse Autoencoders Encode Both Concepts and Functions: The Downstream Geometry of Feature Effects

## Abstract
The wide-scale use of sparse autoencoders (SAEs) as interpretability tools is limited by inconsistent links between SAE features and model behavior. Features with clear activation descriptions may have weak or unexpected causal effects; steering can vary across prompts or oppose the intended direction; and activation-based feature selection can miss features that produce the desired output change. Prior work has studied feature geometry inside the model, where features are computed. We instead study the geometry of changes in model logits caused by feature interventions. We introduce Feature-Effect Geometry Analysis (FEGA), an unsupervised framework that removes the same active SAE feature across contexts and analyzes the resulting cloud of logit changes. Across SAE variants, consistent one-dimensional effects are rare: few features behave like reusable directions. To interpret this variation, we distinguish value-like features, tied to static information such as factual attributes, from pointer-like features, associated with context-dependent operations. Value-like features more often exhibit structured, low-dimensional effects, although these effects typically span several directions. Pointer-like features, by contrast, predominantly exhibit diffuse effects. Our results show that a feature can be interpretable and causally relevant without providing a stable direction for steering.

## Metadata
- **Published**: 2026-07-27T16:45:08Z
- **Authors**: Phu Gia Hoang, Anwoy Chatterjee, Tanmoy Chakraborty, Iryna Gurevych, Subhabrata Dutta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24645v1)
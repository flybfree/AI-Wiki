---
title: Looking Beyond the Scale: Do Surgical Skill Models Learn Transferable Representations Across Assessment Rubrics?
published: 2026-08-18T08:44:31Z
authors: Hanna Hoffmann, Felix von Bechtolsheim, Stefanie Speidel, Rebecca Hisey
url: http://arxiv.org/abs/2608.17519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Looking Beyond the Scale: Do Surgical Skill Models Learn Transferable Representations Across Assessment Rubrics?

## Abstract
Vision-based surgical skill assessment has shown strong in-domain results, yet a fundamental question remains unasked: do these models learn transferable representations of surgical proficiency, or do they merely encode dataset-specific visual patterns?   This paper systematically analyzes what limits cross-domain skill transfer between the GOALS and OSATS assessment scales using the LASANA and JIGSAWS datasets. Each evaluated method serves a targeted diagnostic purpose: end-to-end training to test whether supervised skill learning transfers directly, Adaptive Sharpness-Aware Minimization (ASAM) to probe whether flatter loss landscapes improve generalization, and augmentation-based self-supervised and contrastive learning to assess whether domain-invariant pretraining decouples skill from visual context. Transfer is evaluated in both directions using a disjoint-participant held-out test set for JIGSAWS.   Results reveal an asymmetry: backbones pretrained on JIGSAWS achieve CCC values of 0.77 to 0.80 on LASANA, closely matching the end-to-end baseline, showing cross-rubric transfer is feasible when the target domain provides consistent supervision. Transfer to JIGSAWS fails across all methods, likely due to annotation inconsistencies. Control experiments with a Kinetics-pretrained backbone suggest task-specific heads carry the majority of the skill prediction burden, while the backbone need only provide adequate spatiotemporal features.   These findings offer a new perspective on vision-based skill assessment: the central question of whether skill representations transfer across scoring systems has not been previously investigated. Results indicate the visual component is dominant but not solely responsible for skill prediction; further work is needed to conclusively disentangle transferable skill features from those bound to a specific visual domain.

## Metadata
- **Published**: 2026-08-18T08:44:31Z
- **Authors**: Hanna Hoffmann, Felix von Bechtolsheim, Stefanie Speidel, Rebecca Hisey
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17519v1)
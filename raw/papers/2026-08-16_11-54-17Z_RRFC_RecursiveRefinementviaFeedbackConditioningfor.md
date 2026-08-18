---
title: RRFC: Recursive Refinement via Feedback Conditioning for Iterative Image-to-Image Generation
published: 2026-08-16T11:54:17Z
authors: Kareem Hassani, Chaymaa Abbas, Hadi Al Mubasher, Mariette Awad
url: http://arxiv.org/abs/2608.15694v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RRFC: Recursive Refinement via Feedback Conditioning for Iterative Image-to-Image Generation

## Abstract
Conditional image-to-image generators are single-shot: they map input features to an output in one forward pass and treat it as final, with no opportunity to improve on it. Although trained to produce the best possible result in one step, such a model leaves room for improvement if it can adaptively revise its own output over iterations. We propose Recursive Refinement via Feedback Conditioning (RRFC), a novel feedback-conditioning framework for iterative output refinement that teaches a model to adaptively revise its output by conditioning on a new signal, namely its most recent previous prediction, which is fed back as an auxiliary set of channels alongside the original input. This preserves the generator's core architecture while modifying its conditioning interface and, depending on the model family, its training or inference procedure, so RRFC can be attached to existing generators without redesign. We evaluate RRFC across six baselines spanning adversarial, equilibrium, and diffusion-based models and three paired image-to-image translation tasks. Across 18 architecture-task settings, RRFC yields seven Holm-corrected improvements, seven degradations, and four non-significant changes. The gains concentrate on reconstruction-fidelity and identity settings, while five of the seven degradations fall on the single semantic-layout task, where every model declines. These results indicate that feedback-based refinement helps when its objective overlaps with the evaluated property, and that its gains concentrate on the tasks where that overlap holds.

## Metadata
- **Published**: 2026-08-16T11:54:17Z
- **Authors**: Kareem Hassani, Chaymaa Abbas, Hadi Al Mubasher, Mariette Awad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15694v1)
---
title: Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation
published: 2026-08-20T21:09:50Z
authors: Emilio Ferrara
url: http://arxiv.org/abs/2608.20569v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation

## Abstract
Are frontier models able to introspect about their internal states? Recent work suggests that under certain conditions a complex enough model can audit its own internals, call out what changed, and report back confidently about it. We tested that claim on eight open-weight models from seven families and found no such ability: asked whether their own computation had been altered, none answered better than chance. To test it we built Open-Weight Masked Introspection (OWMI), a framework that intervenes on residual-stream sites, attention heads and sparse-autoencoder features, then interrogates the model about the change against the null conditions an answer has to beat: sham runs where nothing was altered, impact-matched random perturbations, and a text-only observer that sees only the visible output.   Over 78,000 measurements, no model's report discriminates a real intervention from a sham beyond chance (AUROC ~0.5007), and an equivalence test bounds the effect below 0.15 percentage points of AUROC. Surprisingly, all the information needed is in the models. A model fine-tuned to report this class of intervention reaches near-perfect recovery on held-out directions, and a linear probe recovers intervention presence from the same activations at 75% to 95.8% accuracy, sharpening to no held-out error at the last layer before the model speaks. In one model the signal surfaces in the confidence rather than the words: its yes-or-no report never varies, while the confidence attached to it separates intervention from sham at AUROC 0.647. The failure sits in the path from internal state to verbal report, so oversight that reads a model's own testimony needs validating against an internal reference.   While our results show the inability of current open-weight models to introspect, the debate is not settled for future models.

## Metadata
- **Published**: 2026-08-20T21:09:50Z
- **Authors**: Emilio Ferrara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20569v1)
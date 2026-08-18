---
title: Towards Reasonable Molecular Structure Elucidation from Infrared Spectroscopy with Chemical Feedback
published: 2026-08-17T04:26:12Z
authors: Yusen Tan, Hongyu Zhan, Hai-tao Yu, Changxi Chi, Wenjie Du, Jun Xia
url: http://arxiv.org/abs/2608.16082v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Reasonable Molecular Structure Elucidation from Infrared Spectroscopy with Chemical Feedback

## Abstract
Infrared (IR) spectra provide characteristic signals of molecular structure, which are often interpreted by experts via functional-group identification or library matching, making the process time-consuming and ambiguous. Recent machine learning methods have made progress in molecular structure elucidation using molecular formulas and IR spectra. However, these models often infer unreasonable candidate molecular structures, including top-ranked predictions. More specifically, the molecular formula implied by a candidate structure often fails to match the input molecular formula, and the candidate's theoretical IR spectrum is often inconsistent with the observed IR spectrum. To address these issues, we propose Formula- and IR-Matched Preference Optimization (FIRMPO), a general and plug-and-play chemical feedback-driven preference optimization framework for molecular structure elucidation. FIRMPO incorporates chemical feedback as preference signals based on exact molecular formula matching and IR spectral consistency to guide reasonable structure predictions. Unlike generic preference optimization methods, FIRMPO is tailored to molecular structure elucidation while remaining model-agnostic, enabling it to be readily integrated with different structure prediction models in this class. This encourages models to prioritize structures that satisfy the chemical feedback, leading to a substantial improvement in the accuracy of top-ranked predictions. Extensive experiments on three widely used IR datasets show that FIRMPO significantly improves molecular structure elucidation accuracy over existing baselines.

## Metadata
- **Published**: 2026-08-17T04:26:12Z
- **Authors**: Yusen Tan, Hongyu Zhan, Hai-tao Yu, Changxi Chi, Wenjie Du, Jun Xia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16082v1)
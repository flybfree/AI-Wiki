---
title: Causal Inference with Unstructured Outcomes
published: 2026-08-04T03:53:04Z
authors: Kevin Christian Wibisono, Yixin Wang
url: http://arxiv.org/abs/2608.03085v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Causal Inference with Unstructured Outcomes

## Abstract
Causal inference has traditionally centered on scalar outcomes: whether a patient recovers, how much a worker earns, or how many visits a website receives. Modern studies increasingly ask causal questions about outcomes with richer form, such as clinical notes, open-ended survey responses, and images. A hospital may want to know how an AI documentation tool changes the notes physicians write, or how a nurse training program alters what patients say in survey responses. For such outcomes, the usual average treatment effect is ill-defined: one cannot meaningfully subtract one text or image from another. To this end, we propose a causal query for unstructured outcomes. The key idea is to learn what features of the outcome are most causally affected by the treatment, which we call the maximally contrasting feature (MCF). To estimate the MCF, we learn a feature-scoring function that maps each outcome to a scalar and exposes the sharpest contrast between treated and control potential outcomes. We develop identification conditions and estimation algorithms for this query, and extend it to heterogeneous effects by allowing the feature-scoring function to depend on observed covariates. We also handle settings where both the treatment and the outcome are unstructured. Empirical studies on text and images show that the algorithm recovers salient aspects of an outcome changed by a treatment.

## Metadata
- **Published**: 2026-08-04T03:53:04Z
- **Authors**: Kevin Christian Wibisono, Yixin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03085v1)
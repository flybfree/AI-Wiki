---
title: Causal Inference with Unstructured Treatments
published: 2026-08-01T13:21:46Z
authors: Kevin Christian Wibisono, Yixin Wang
url: http://arxiv.org/abs/2608.00657v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Causal Inference with Unstructured Treatments

## Abstract
Causal inference usually concerns a scalar treatment, yet in many problems the treatment is unstructured: a text, an image, or a sequence of clinical decisions. Consider an instructor writing a course description to attract more students: the treatment is the course description, and the outcome is enrollment. The standard target, the average treatment effect of fixing the treatment to one exact value versus another, runs into two problems. It cannot be estimated, because almost no exact description recurs across courses, leaving no comparable group from which to measure its effect; and it would be of little use even if it could, since no one wants every course to carry the same description. What the instructor actually wants to know is which features of a description raise enrollment, and which of those features can be acted on across many courses. To this end, we propose a causal query for unstructured treatments: the maximally influential feature (MIF), the feature of the treatment that most strongly influences the outcome. We formalize the MIF as a binary feature of the treatment, defined by a feature-scoring function, constrained so that both of its values stay well populated, and chosen to maximize the causal effect it induces. Turning the feature on shifts the distribution of treatments toward those that display it, turning it off shifts away, and the MIF effect contrasts the two average potential outcomes. We study identification conditions for the MIF, develop algorithms to estimate it, and make it actionable through a nudging algorithm that revises a treatment along the MIF into an outcome-improving version. We illustrate the MIF algorithm across applications in text, image, and dynamic treatment sequences.

## Metadata
- **Published**: 2026-08-01T13:21:46Z
- **Authors**: Kevin Christian Wibisono, Yixin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00657v1)
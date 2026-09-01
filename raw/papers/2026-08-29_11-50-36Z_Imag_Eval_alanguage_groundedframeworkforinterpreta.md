---
title: Imag-Eval: a language-grounded framework for interpretable Text-to-Image instruction following evaluation
published: 2026-08-29T11:50:36Z
authors: Ibrahim Mohamed Serouis, David Jaramillo Duque
url: http://arxiv.org/abs/2608.29210v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Imag-Eval: a language-grounded framework for interpretable Text-to-Image instruction following evaluation

## Abstract
Text-to-Image (T2I) models have recently achieved impressive visual fidelity, yet their evaluation remains constrained by benchmarks that are often difficult to interpret and insufficiently diagnostic. Existing skill-based evaluations tend to overlook critical failure modes that strongly impact usability but fall outside standard taxonomies, such as global incoherence arising from missing parts or physically implausible configurations (e.g., floating objects). In addition, prompt difficulty is typically controlled along a single dimension; either prompt length or the number of elements to generate. To address these limitations, we introduce Imag-Eval, a controlled benchmark designed to assess how T2I models ground compositional natural-language instructions into visual outputs. Unlike prior work that conflates surface linguistic complexity with compositional difficulty, Imag-Eval explicitly seeks to disentangles these factors by independently varying both the number of instances and the combination of constraints (rules), while avoiding error propagation. This design enables fine-grained and interpretable analysis of where cross-modal instruction following fails. Our benchmark comprises 1,140 prompts and 8,842 combined rules, and we evaluate it on several state-of-the-art models. Complementing this analysis with an additional study of over 2,000 prompts from a concurrent benchmark, our results suggest that, for structured skills, compositional difficulty is primarily governed by the number of grounded rules and their binding to instances,, rather than by prompt length alone.

## Metadata
- **Published**: 2026-08-29T11:50:36Z
- **Authors**: Ibrahim Mohamed Serouis, David Jaramillo Duque
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29210v1)
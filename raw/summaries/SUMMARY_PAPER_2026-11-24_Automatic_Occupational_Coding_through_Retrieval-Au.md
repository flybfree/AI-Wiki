---
title: Automatic Occupational Coding through Retrieval-Augmented Generation
url: http://arxiv.org/abs/2611.31051v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_17-15-08Z_AutomaticOccupationalCodingthroughRetrieval_Augmen.md
generated_at: 2026-11-24 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper presents OPERAG, a Retrieval-Augmented Generation framework for automatic occupational coding of free-text job descriptions. It targets the slow, unreliable, and costly manual standardization of job descriptions into occupational classifications and their linkage to hazardous exposures via Job Exposure Matrices (JEM). Validated on AsiaLymph's 36,062 real-world job descriptions, OPERAG achieved 42.6% occupational classification accuracy at the 4th coding level and 89.9-98.6% accuracy on exposure assessment using the ALOHA+ and SHOCK JEMs.

## Key Takeaways
- Manual occupational coding is slow, unreliable (44-89% inter-coder reliability), and costly because job descriptions are short and ambiguous, classifications contain hundreds to thousands of categories, and gold standards are absent.
- State-of-the-art automatic tools reach 46-79% accuracy (human level) in-distribution but drop to 17-26% on out-of-distribution datasets, and their supervised architectures cannot generalize beyond classifications seen in training, leaving JEMs built on other classifications incompatible.
- OPERAG retrieves coding index information and combines it with Large Language Model-based classification to classify into any occupational classification without expert-labelled databases; it approached human coders' 51-56% inter-coder reliability at the 4th coding level and delivered high exposure-assessment accuracy across two JEMs.

## Context
Occupational exposures such as welding fumes, silica dust, and noise pollution cause roughly 1.9 million deaths and 89.7 million disability-adjusted life years annually, making high-quality exposure assessment a public-health priority. This work sits at the intersection of retrieval-augmented LLM methods and occupational epidemiology, addressing a domain where unstructured text, fine-grained taxonomies, and distribution shift make supervised classification fragile.

## Implications
For researchers and practitioners, OPERAG offers a scalable, classification-agnostic route to standardize job descriptions and link them to hazardous exposures, reducing dependence on expert-labelled databases and enabling reuse of JEMs across classifications. This can improve exposure-response associations and large-scale worker-health surveillance, although 4th-level accuracy still trails human inter-coder reliability and should be interpreted with appropriate validation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.31051v1)

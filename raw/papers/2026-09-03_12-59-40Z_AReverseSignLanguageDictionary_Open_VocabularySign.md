---
title: A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval
published: 2026-09-03T12:59:40Z
authors: Santiago Poveda-Gutiérrez, Hideki Nakayama, Mayumi Bono
url: http://arxiv.org/abs/2609.03788v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval

## Abstract
Isolated Sign Language Recognition (ISLR) is conventionally cast as closed-set classification over gloss labels, which cannot generalize to signs unseen in training and ties every deployment to a gloss-annotated lexicon. We instead recognize signs extracted from continuous signing by (1) captioning a sign-level clip into a free-form procedural description of the articulation with an open-weight vision-language model, and (2) retrieving the closest entry from a vocabulary of target descriptions with a multilingual sentence encoder: a reverse sign language dictionary that needs no gloss supervision and admits an open vocabulary. On 1,300 sign-level segments from a Japanese Sign Language (JSL) dialogue corpus annotated with procedural descriptions (against a 2% top-10 chance floor over the 503-entry target vocabulary), fine-tuning the captioner substantially improves seen-class retrieval: language and vision tower fine-tuning raises top-10 retrieval on seen classes from 4.5% (untrained) to 49%, becoming statistically indistinguishable from a standard supervised closed-set classifier (I3D) on two of the three test sets where a closed-set classifier can be evaluated at all. More importantly, unseen-class retrieval also improves significantly over the untrained pipeline (11.5% -> 21.0% top-10, p=0.0094), a regime in which the closed-set classifier cannot participate. A matcher-side empirical upper-bound analysis shows the sentence encoder already recovers close to 100% of paraphrased gold descriptions, locating a gap in captioning quality that we aim to address in future work. To our knowledge this is the first description-based, open-vocabulary sign lookup from continuous signing without gloss supervision, and the first for JSL.

## Metadata
- **Published**: 2026-09-03T12:59:40Z
- **Authors**: Santiago Poveda-Gutiérrez, Hideki Nakayama, Mayumi Bono
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03788v1)
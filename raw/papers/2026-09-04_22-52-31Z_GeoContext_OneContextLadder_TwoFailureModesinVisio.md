---
title: GeoContext: One Context Ladder, Two Failure Modes in Vision-Language Geolocation: Flat Reliance on User-Provided Location Context and False Confirmation of Location Claims
published: 2026-09-04T22:52:31Z
authors: Yifan Zhang, Kai Wang
url: http://arxiv.org/abs/2609.05761v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GeoContext: One Context Ladder, Two Failure Modes in Vision-Language Geolocation: Flat Reliance on User-Provided Location Context and False Confirmation of Location Claims

## Abstract
Visual geolocation benchmarks typically ask a model where an image was captured without accounting for the location context that users often provide. We introduce GeoContext, a resource supporting two complementary tasks: GeoHint, open-ended localization given a true but coarse location hint, and GeoVerify, binary verification of whether an image was taken within 150 m of a claimed place. GeoContext constructs a context ladder by stratifying nearby reference points according to distance and referenceability, allowing the image to remain fixed while the supplied context varies. The benchmark covers 109 sites in 30 cities and evaluates five vision-language models using 21,933 GeoHint responses and 6,270 GeoVerify responses.   Our evaluation reveals three main patterns. First, hint repetition varies by only 1.5 percentage points across referenceability tiers and by less than 3 points across distance bands, while the resulting localization error increases steadily with hint distance. Second, behavior depends strongly on no-context performance: at sites with low no-context accuracy, the median ratio between localization error and hint distance is approximately 1.00, whereas at higher-accuracy sites it ranges from 0.24 to 0.69. After correcting for bias introduced by the site grouping procedure, only one of the five models retains a negative accuracy estimate when given a nearby hint. Third, in GeoVerify, no model reaches d' = 1 for decoys immediately beyond the 150 m tolerance. Model rankings also change when sensitivity is separated from response bias, and 83.8% of false acceptances are reported with confidence of at least 0.8. We release the benchmark, construction pipeline, audit decisions, and scoring code.

## Metadata
- **Published**: 2026-09-04T22:52:31Z
- **Authors**: Yifan Zhang, Kai Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05761v1)
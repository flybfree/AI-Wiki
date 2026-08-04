---
title: TIDES: A Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics
url: http://arxiv.org/abs/2608.01724v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_05-42-40Z_TIDES_ALongitudinalBilingualDatasetforModelingMult.md
generated_at: 2026-08-03 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TIDES, a longitudinal bilingual dataset that tracks 12 university project teams over a semester to capture real‑world multi‑party social dynamics. Fine‑tuning on TIDES boosts next‑speaker prediction by 13.8 percentage points compared with a bigram baseline and matches the state of the art on the AMI Meeting Corpus while using roughly half the data.

## Key Takeaways
- The dataset contains 75,971 utterances in English and Korean from 12 teams over a full semester, providing high‑resolution records of natural group conversations.  
- Fine‑tuned models achieve a next‑speaker prediction accuracy of 64.53%, which is 13.8 percentage points higher than the bigram baseline.  
- The model’s performance is within 2.1 percentage points of the published state‑of‑the‑art on AMI, using about 42% less training data.

## Context
Current large language models often rely on short‑term lab datasets that do not reflect the evolving social structures of real teams, limiting their ability to model long‑term collaboration. This work bridges that gap by offering a realistic, longitudinal resource for studying team dynamics in multilingual settings.

## Implications
For researchers, TIDES enables more accurate modeling of group evolution and can be leveraged to improve next‑speaker generation in collaborative AI systems. For industry practitioners, the dataset suggests that while prediction accuracy improves with richer data, human preferences may still favor simpler, less structured outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01724v1)

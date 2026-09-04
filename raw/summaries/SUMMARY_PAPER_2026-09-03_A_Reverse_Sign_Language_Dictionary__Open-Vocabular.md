---
title: A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval
url: http://arxiv.org/abs/2609.03788v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_12-59-40Z_AReverseSignLanguageDictionary_Open_VocabularySign.md
generated_at: 2026-09-03 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a reverse sign language dictionary that enables open‑vocabulary recognition of Japanese Sign Language signs from continuous video streams without requiring gloss annotations. By captioning each sign clip with a procedural description using an open‑weight vision‑language model and then retrieving the nearest entry in a target vocabulary via a sentence encoder, the system achieves strong performance on both seen and unseen classes.

## Key Takeaways
- The method eliminates the need for a pre‑annotated gloss lexicon by generating free‑form descriptions of sign articulation. 
- Fine‑tuning the vision‑language captioner together with language and vision towers raises seen‑class retrieval to near 50% top‑10, matching a supervised closed‑set classifier on two test sets. 
- Unseen‑class retrieval improves from 11.5% to 21.0% top‑10 (p=0.0094), demonstrating capability beyond any closed‑set baseline.

## Context
This work addresses the limitation of traditional ISLR approaches that rely on fixed gloss labels, which hinder generalization and require extensive annotation effort. By leveraging continuous signing data and a multilingual sentence encoder, the system demonstrates an open‑vocabulary paradigm that can be applied to other sign languages with minimal additional supervision.

## Implications
For practitioners developing assistive technologies, this pipeline offers a scalable way to recognize signs in real time without costly manual labeling. The approach could integrate into video‑based communication tools, improving accessibility for Deaf users and enabling richer multimodal interactions beyond simple label matching.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03788v1)

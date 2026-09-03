---
title: Candidate Generation and Definition-Guided Verification for Sentence-Level Depression Symptom Recognition
published: 2026-09-01T20:08:03Z
authors: Weiming Li, Catarina Barata, Miguel Constante, Joao Sanches
url: http://arxiv.org/abs/2609.01833v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Candidate Generation and Definition-Guided Verification for Sentence-Level Depression Symptom Recognition

## Abstract
Sentence-level recognition of depression symptoms is challenging because similar expressions can differ in symptom relevance, and language-model inference is insufficiently grounded in diagnostic definitions. This study proposes a two-stage framework separating symptom-candidate generation from definition-grounded verification. A contrastively fine-tuned sentence encoder generates a symptom candidate per sentence, and a fine-tuned language model verifies whether the candidate is present or absent using the sentence, its context, and a candidate-specific diagnostic definition, checking its judgment against that definition before answering. Evaluated against encoder, inference-based, medical, and general LLM baselines and a matched single-stage supervised classifier, the proposed pipeline attains the best accuracy and F1 scores of all methods, with rationales matching expert-authored annotations. A preliminary clinical audit indicates moderate alignment with diagnostic definitions, with explanation quality strongly dependent on prediction correctness. The results support decomposing symptom recognition into candidate generation and definition-grounded verification, though performance remains limited for rare categories.

## Metadata
- **Published**: 2026-09-01T20:08:03Z
- **Authors**: Weiming Li, Catarina Barata, Miguel Constante, Joao Sanches
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01833v1)
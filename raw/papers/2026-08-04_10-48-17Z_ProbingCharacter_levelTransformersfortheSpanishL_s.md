---
title: Probing Character-level Transformers for the Spanish L-shaped Morphome
published: 2026-08-04T10:48:17Z
authors: Akhilesh Kakolu Ramarao, Kevin Tang, Wiebke Petersen, Dinah Baer-Henney
url: http://arxiv.org/abs/2608.03452v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Probing Character-level Transformers for the Spanish L-shaped Morphome

## Abstract
When a transformer learns an irregular morphological pattern, what has it learned? Our test case is the Spanish \emph{L-shaped morphome}, a complex irregular pattern in which the verb's stem alternates in exactly the first-person singular indicative and all subjunctive forms, and whose membership no phonological, semantic, or syntactic feature predicts. Prior studies have shown that character-level transformers can reproduce this pattern, but that evidence describes what models produce, not what they represent. Probing five architectures, twelve trained models each, under lemma-disjoint cross-validation with controls and surface baselines, we show that the models encode the L-shaped class itself, not just its visible alternations. It is decodable above every surface baseline, survives instances in which every form shows the same stem, and probes trained on alternating instances still classify non-alternating ones. The encoding is localized where the stem choice is made, at the stem-final consonant position of the middle decoder, before the alternant is read. And it is item-specific: which verbs a model learned matters far more than which architecture it is. The models store the morphome as an item-specific lexical abstraction, sufficient to reproduce the pattern but not to generalize it as humans do.

## Metadata
- **Published**: 2026-08-04T10:48:17Z
- **Authors**: Akhilesh Kakolu Ramarao, Kevin Tang, Wiebke Petersen, Dinah Baer-Henney
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03452v1)
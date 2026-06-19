---

title: Multilingual Knowledge Transfer under Data Constraints via Lexical Interventions
published: "2026-05-22T17:45:49Z"
authors: Anastasiia Sedova, Natalie Schluter, Skyler Seto, Maartje ter Hoeve
url: http://arxiv.org/abs/2605.23885v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Multilingual Knowledge Transfer under Data Constraints via Lexical Interventions



**Source**: [Original Paper](http://arxiv.org/abs/2605.23885v1)
## Abstract
Cross-lingual knowledge transfer is critical for building high-performing multilingual language models for languages with insufficient training data. When target language data is scarce, the knowledge required for many downstream tasks involving scientific reasoning, commonsense inference, and world knowledge must be acquired primarily from the high-resource language, making effective knowledge transfer essential. Existing methods for improving such cross-lingual knowledge transfer require large amounts of parallel data, translation systems, auxiliary models, or additional training stages that are largely unavailable for many languages. We propose LINK - a data-level intervention method that improves knowledge transfer during model pretraining through lexical substitutions in high-resource part of pretraining data using bilingual vocabularies. For a given replacement ratio, randomly selected words in a portion of the high-resource (English) training corpus are swapped with their word-level translations, requiring no additional model training and only a bilingual vocabulary, which can be obtained at near-zero cost for virtually any language. Evaluation on eight languages across five model sizes shows notable improvements on downstream tasks in the target language, with up to a 2x speedup in training to reach equivalent performance.

## Metadata
- **Published**: 2026-05-22T17:45:49Z
- **Authors**: Anastasiia Sedova, Natalie Schluter, Skyler Seto, Maartje ter Hoeve
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23885v1)
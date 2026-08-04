---
title: Morphology Aware Reversible Semantic Tokenization and Hierarchical Word Composition for Tamil Language Models
published: 2026-08-02T11:07:53Z
authors: Anand Murugan
url: http://arxiv.org/abs/2608.01153v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Morphology Aware Reversible Semantic Tokenization and Hierarchical Word Composition for Tamil Language Models

## Abstract
Statistical subword tokenizers can process arbitrary text, but their units need not align with lexical or grammatical structure. This is especially important for Tamil, where a written word may encode stem changes, case, number, tense, agreement, voice, clitics, and linked verbs. We present a Tamil morphology system extending the open-source ThamizhiMorph analyzer and generator, together with a byte-exact semantic tokenizer and a learned hierarchical word composer. Twelve finite-state transducers analyze words into lemmas and grammatical features, while character and byte fallbacks preserve exact reconstruction.   We compare a flat morphology tokenizer, a signal-preserving word composer, and tokenizers based on Sarvam-1, AI4Bharat IndicBERTv2, and BrahmicTokenizer-131K. All systems use the same 69,591 Tamil-English training pairs, 18.97-million-parameter encoder-decoder, 40,000 updates, target tokenizer, optimizer, positional method, and generation settings.   On a protected 3,539-row IN22 and FLORES+ evaluation, morphology-flat achieves the best pooled scores: 10.63 BLEU, 35.26 chrF++, and 0.6276 COMETKiwi. Relative to AI4Bharat, the strongest external-tokenizer baseline, these are improvements of 7.2%, 3.2%, and 2.6%. The word composer scores 10.30, 34.88, and 0.6241, improving on AI4Bharat by 3.8%, 2.1%, and 2.0%.   The composer reduces mean global source states from 71.48 to 29.08, a 59.3% reduction, and is estimated to require 9-21% fewer inference FLOPs depending on decoder caching. Its remaining quality gap is concentrated in longer FLORES+ sentences. These results show that explicit Tamil morphology improves translation under a fixed small-model budget, while hierarchical composition substantially reduces sequence length and estimated inference cost.

## Metadata
- **Published**: 2026-08-02T11:07:53Z
- **Authors**: Anand Murugan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01153v1)
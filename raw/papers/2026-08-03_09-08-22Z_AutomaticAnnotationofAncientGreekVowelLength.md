---
title: Automatic Annotation of Ancient Greek Vowel Length
published: 2026-08-03T09:08:22Z
authors: Albin Thörn Cleland, Eric Cullhed
url: http://arxiv.org/abs/2608.01935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automatic Annotation of Ancient Greek Vowel Length

## Abstract
Prior work in Ancient Greek NLP relies on corpora that do not disambiguate the phonemic vowel length of alpha, iota, and ypsilon, together known as the dichrona. Depending on lexeme, morphology, sandhi, syntax, and conventions of period, genre, and verse form, each of these letters can represent either a long or a short vowel. Deciding and marking the correct length is known as "macronizing", a long-tail problem given the sheer mass of word forms and the context dependency of individual instances. No macronized corpus of Ancient Greek is publicly available at scale, so a stand-alone macronizer is needed. While previous work has shown how to build a static, corpus-bespoke vowel-length dictionary, the present paper constructs the first general-purpose macronizer for arbitrary Ancient Greek input. Given input carrying lemma, part-of-speech, and morphological annotation in the standard CoNLL-U format, a set of recursive modules lets less common word forms inherit markup from more common forms of the same lexical word. The macronizer's chief application is generating training data for machine learning: we show that a small character-level transformer trained on the macronizer's own output learns to generalize past the cases the rule-based system leaves unmarked, matching or exceeding its accuracy on a gold-standard, manually annotated benchmark of verse and prose. We also show that macronization can improve downstream prosodical NLP tasks like verse scansion.

## Metadata
- **Published**: 2026-08-03T09:08:22Z
- **Authors**: Albin Thörn Cleland, Eric Cullhed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01935v1)
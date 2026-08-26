---
title: Wontopos Tablet 2: Measuring Multilingual and Multimodal Memory Retrieval Without Lexical Matching
published: 2026-08-24T23:54:08Z
authors: Sunwoo Kim
url: http://arxiv.org/abs/2608.23920v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Wontopos Tablet 2: Measuring Multilingual and Multimodal Memory Retrieval Without Lexical Matching

## Abstract
We measure tablet-2, a production long-term memory engine for language models, on the text benchmarks the field already uses and on cross-lingual retrieval of photographs stored with no text at all. Its retrieval path contains no lexical matching, no keyword scoring, and no language model of its own.   On LongMemEval-S (500 questions) it scores 95.7% [93.4, 97.1]; on BEAM-1M (700 questions, 2.21M stored memories) 67.5% [64.8, 70.2]. Those are question-sampling intervals, not the run-to-run spread, which is an order of magnitude narrower.   Most of the paper is about how little they mean alone. Holding engine, corpus, settings and judge fixed, changing only the reader moves LongMemEval-S by 2.0 points; changing only the re-ask budget moves BEAM-1M by 8.9. Neither is stated in the reports we compare against, and the second exceeds most gaps there, so we give that table as a placement and not a ranking.   For the multimodal axis we run two controls. Against BM25, configured as strongly as we could, we reach 95.2% mean recall@5 over 70 store-and-query language cells where BM25 reaches 19.0% and is exactly zero in 54. On captionless photographs a lexical method has no document to score at all. Open dense baselines on 300 Crossmodal-3600 photographs in 14 languages show that density confers no language independence: one scores 91.0% on English and 4.7% on Russian from identical image vectors, and a multilingual variant collapses on Telugu and Swahili. Our spread across languages is 14.0 against their 27.5 and 27.7.   Three results run against us and are reported at equal weight: low-resource languages degrade sharply (Swahili 53.0%, Telugu 64.0%), attaching captions lowers cross-lingual retrieval by 11.4 points, and one setting omitted into one stage of our own retrieval cost 37 points of Korean top-1 accuracy while leaving nine languages untouched.

## Metadata
- **Published**: 2026-08-24T23:54:08Z
- **Authors**: Sunwoo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23920v1)
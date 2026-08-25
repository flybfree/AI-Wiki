---
title: Does a Modern-Handwriting Warm-Up Help Historical Arabic OCR? A Reproducible, Compute-Matched Evaluation on Muharaf and KHATT
published: 2026-08-23T09:29:27Z
authors: Sumaih Almarshad, Maram Alamri, Dona Aloraini, Fares Altuwaim, AlJawharh AlOtaibi, Reem Alyabis, Rayah Aldawsari
url: http://arxiv.org/abs/2608.22316v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does a Modern-Handwriting Warm-Up Help Historical Arabic OCR? A Reproducible, Compute-Matched Evaluation on Muharaf and KHATT

## Abstract
Whether an intermediate stage of modern Arabic handwriting helps or hurts historical Arabic HTR is usually decided from one implementation and one comparison, too thin a basis for a claim either way. We test stability by running the same nominal ablation four times, letting the base checkpoint, encoder-freezing strategy, epoch budget, precision, and learning-rate schedule vary as they naturally did during development, while holding the normalization, scorer, and interval estimation fixed. Each run compares intermediate training on modern handwriting (KHATT) then fine-tuning on historical manuscripts (Muharaf) against fine-tuning on Muharaf directly. Across the four runs the estimated effect swings from -17.64 to +14.52 CER points and reverses sign. The two extremes are exactly the two runs with an identifiable confound (a fivefold lower learning rate in one; a checkpoint of undisclosed provenance in the other); the two clean runs land at -0.25 and +0.94, i.e. no effect. A tight interval from one implementation says nothing about the next. We then run a compute-matched experiment with identical budgets over three seeds: KHATT warm-up is +2.42 CER points worse than a matched same-domain control (95% interval [+0.60, +4.25]); the part of that gap specific to the handwriting domain is only about 0.6 points a small negative effect under this configuration, not a universal result. We release a SaudiHeritage-OCR package with the normalizer, interval scorer, a verified KHATT decoder, experimental manifests, VLM baselines, and an edition-alignment protocol, so the result can be checked independently. The Al-Mahd inscription line is held strictly out and is not offered as a benchmark.

## Metadata
- **Published**: 2026-08-23T09:29:27Z
- **Authors**: Sumaih Almarshad, Maram Alamri, Dona Aloraini, Fares Altuwaim, AlJawharh AlOtaibi, Reem Alyabis, Rayah Aldawsari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22316v1)
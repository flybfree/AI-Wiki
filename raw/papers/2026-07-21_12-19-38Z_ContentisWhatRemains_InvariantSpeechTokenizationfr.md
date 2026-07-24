---
title: Content is What Remains: Invariant Speech Tokenization from Parallel Utterances
published: 2026-07-21T12:19:38Z
authors: Laurin Wagner, Bernhard Thallinger, Miroslav Stankovic, Mario Zusag
url: http://arxiv.org/abs/2607.19033v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Content is What Remains: Invariant Speech Tokenization from Parallel Utterances

## Abstract
Discrete speech tokenizers aim to disentangle semantic from acoustic information, yet targets from self-supervised learning (SSL) models like HuBERT retain non-linguistic variation: speaker identity, prosody, and channel conditions leak into the tokens, inflating entropy. Our key insight is that when enough speakers utter the same words under varying conditions, linguistic content is the only shared factor. We propose PINT (Parallel INvariant Tokenization), which fine-tunes an SSL encoder with alignment losses across parallel utterances and augmentations to distill this shared residual. PINT collapses identical words onto consistent token sequences, drastically reducing conditional entropy. Unlike ASR text, PINT tokens preserve frame-level temporal grounding and serve as drop-in semantic targets for audio codecs. Experiments show a 98.7% relative reduction in speaker probe accuracy (93.1% to 1.2%), a 42% lower ABX error rate, and 27-30% lower LM perplexity versus baselines, confirming that the right invariance is key to efficient learning.

## Metadata
- **Published**: 2026-07-21T12:19:38Z
- **Authors**: Laurin Wagner, Bernhard Thallinger, Miroslav Stankovic, Mario Zusag
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19033v1)
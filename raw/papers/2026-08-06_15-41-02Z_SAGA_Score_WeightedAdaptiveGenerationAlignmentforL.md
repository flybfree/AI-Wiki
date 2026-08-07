---
title: SAGA: Score-Weighted Adaptive Generation Alignment for Low-Resource Nordic Language Models
published: 2026-08-06T15:41:02Z
authors: Hoda Fakharzadehjahromy, Emil Wiman, Andreas Bueff, Hafsteinn Einarsson, Fredrik Heintz
url: http://arxiv.org/abs/2608.06179v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAGA: Score-Weighted Adaptive Generation Alignment for Low-Resource Nordic Language Models

## Abstract
Preference optimisation has proven effective for improving large language models but typically relies on costly human preference annotations. Extending these methods to morphologically rich, low-resource languages remains challenging because such annotations are scarce. We present SAGA (Score-weighted Adaptive Generation Alignment), a parser-guided preference optimisation framework that replaces human labels with dependency-parser supervision. SAGA converts parser judgements into preference pairs for delta-DPO, combines parser quality with lexical diversity in a composite reward, filters low-information pairs using a reward-gap criterion, and monitors reward hacking to maintain reliable supervision. Across Danish, Icelandic, and Norwegian Bokmål using GPT-SW3-1.3B, SAGA consistently improves grammatical quality without requiring human preference labels. Danish parse success increases from 69.0% to 93.8%, Icelandic achieves a +4.5 percentage-point improvement on an independent Stanza evaluation (three-run mean +3.3 percentage points) while native speakers prefer SAGA outputs in 80% of pairwise comparisons, and Norwegian Bokmål improves by +28 percentage points. These results demonstrate that parser-derived supervision is a practical alternative to human preference annotation for grammatical alignment in low-resource languages where high-quality dependency parsers are available.

## Metadata
- **Published**: 2026-08-06T15:41:02Z
- **Authors**: Hoda Fakharzadehjahromy, Emil Wiman, Andreas Bueff, Hafsteinn Einarsson, Fredrik Heintz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06179v1)
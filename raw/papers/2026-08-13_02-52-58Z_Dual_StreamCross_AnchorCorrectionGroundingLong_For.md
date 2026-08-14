---
title: Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors
published: 2026-08-13T02:52:58Z
authors: LingKai Bu
url: http://arxiv.org/abs/2608.12746v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors

## Abstract
Object hallucination in multimodal large language models arises when language priors and corpus co-occurrence bias outweigh the visual evidence, with nothing tying an individual object mention to what the image shows. Most remedies intervene at decoding time without training, yet under a unified protocol their benefit is confined to short captions;supervised fine-tuning (SFT) on a detail- rich corpus lengthens captions, but over forty percent still name absent objects. This paper proposes Dual-Stream Cross-Anchor Correction (DSCC). Unlike work that post-processes decoding, DSCC is the first to inject object-level visual anchors into the language model itself during fine- tuning: a perception stream aligns object-level hidden states at an intermediate layer to frozen text anchors by a bidirectional contrastive objective; a cognition stream lets deeper layers query those anchors by cross-attention at every generation step; and a two-stage curriculum gate couplesthem, making evidence retrieval a structural constraint at each autoregressive step. Under one backbone and one scoring protocol, experiments span long-caption hallucination, object-existence discrimination and cross-domain generalisation, with vanilla SFT on the same corpus and schedule as a length- and density-matched control, so gains are attributed layer by layer. DSCC is the only method reaching the long-caption, low-hallucination region: captions roughly 1.9 times the baseline length at 88.19% precision per object mention, the highest under a density-independent criterion. Ablations expose a synergy: the perception stream alone degrades precision yet reverses sign when stacked on the cognition stream. No universal superiority is claimed: three out-of- domain benchmarks yield a predictable, falsifiable domain-conditionality, the synergy being bound to the anchors' semantic domain and breaking on charts and optical illusions.

## Metadata
- **Published**: 2026-08-13T02:52:58Z
- **Authors**: LingKai Bu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12746v1)
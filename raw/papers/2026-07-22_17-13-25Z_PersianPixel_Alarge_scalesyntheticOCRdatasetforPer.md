---
title: Persian Pixel: A large-scale synthetic OCR dataset for Persian language
published: 2026-07-22T17:13:25Z
authors: Pouria Mahdi, Haq Nawaz Malik
url: http://arxiv.org/abs/2607.20385v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Persian Pixel: A large-scale synthetic OCR dataset for Persian language

## Abstract
Optical Character Recognition (OCR) for Persian remains substantially less mature than for Latin-script languages despite Persian being spoken by more than 110 million people across multiple countries. This gap arises from two fundamental challenges: the intrinsic complexity of the Perso-Arabic writing system and the limited availability of large-scale, high-quality annotated datasets. Persian script exhibits obligatory cursive connectivity, context-dependent glyph shaping, extensive ligatures, diacritic placement, and stylistic variation across writing forms such as Naskh and Nastaliq, all of which significantly complicate text recognition. At the same time, the high cost and labor-intensive nature of manual annotation have created a persistent data bottleneck, limiting the development of robust OCR systems and slowing progress in Persian document digitization.In this paper, we introduce Persian Pixel, a comprehensive synthetic OCR dataset specifically designed to address these challenges. Comprising over 343,000 high-fidelity image text pairs, the dataset spans sentence, paragraph, and full-page document layouts generated from a carefully curated seven-million-word Persian corpus using the SynthOCR-Gen rendering framework. The generation pipeline faithfully models the typographic characteristics of Persian script, including contextual character joining, positional glyph variants, diacritic placement, and multiple representative Persian typefaces. To bridge the synthetic-to-real domain gap, the rendered images are further enriched with more than twenty-five stochastic degradation models that emulate realistic document acquisition artifacts, including ink bleed, paper aging, blur, illumination variation, scanner imperfections, compression artifacts, and multiple noise processes.By overcoming the long-standing scarcity of annotated Persian OCR data, Persian Pixel provides a scalable and openly available resource for training and fine-tuning modern OCR architectures, including transformer-based models such as TrOCR and Donut. The dataset establishes a strong foundation for research in Persian document analysis, historical manuscript digitization, and end-to-end document understanding, while demonstrating that programmatic synthetic data generation offers a practical, cost-effective, and scalable alternative to manual annotation for advancing OCR in low-resource and typographically complex scripts.

## Metadata
- **Published**: 2026-07-22T17:13:25Z
- **Authors**: Pouria Mahdi, Haq Nawaz Malik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20385v1)
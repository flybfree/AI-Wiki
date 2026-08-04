---
title: RadPRISM: Schema-stratified radiology-report supervision for concept-disentangled image representations and visual grounding
published: 2026-07-31T16:14:24Z
authors: Fabian Drexel, Marlene Fritzsche, Era Stambollxhiu, Miriam Kumpf, Lena Schmitzer, Lea Schumann, Jannik Kahmann, Friedrich Puttkammer, Johannes Moll, Jannik Lübberstedt, Zeineb Ben Chaaben, Anirudh Narayanan, Cosmin I. Bercea, Sebastian Ziegelmayer, Marcus R. Makowski, Daniel Rueckert, Lisa C. Adams, Keno K. Bressem
url: http://arxiv.org/abs/2608.00147v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RadPRISM: Schema-stratified radiology-report supervision for concept-disentangled image representations and visual grounding

## Abstract
Vision-language pretraining learns rich medical image representations from radiology reports, but previous model variants commonly operate within a single shared embedding space, so concept-level structure and interpretability must be recovered post hoc, limiting model transparency and, hence, clinical utility. We introduce RadPRISM, which makes a clinician-defined radiology schema a designated stratification axis: an on-premise large language model extracts per-concept text spans from free-text reports, and each clinical concept is aligned in its own dedicated visual subspace, turning concept stratification into direct, top-level alignment supervision. Instantiated on chest radiographs with a 19-concept schema over $203{,}602$ examinations from an internal multi-year archive, RadPRISM improved internal dataset zero-shot classification from $0.717$ (95% CI, $0.710-0.723$) to $0.868$ (95% CI, $0.863-0.872$) macro AUROC over a matched global-alignment baseline, performed on par with the purpose-built CARZero reference in external zero-shot classification while substantially outperforming it (up to 4.3-fold) in pointing-game visual grounding. In addition, a radiologist reader study demonstrated concept-stratified retrieval ability ($0.78$ macro retrieval correctness rate within rank 3), surfacing disentangled descriptive findings that report-level retrieval and fixed-label vocabularies cannot express. RadPRISM yields discriminative, spatially faithful, natively concept-stratified representations shaped by and transparently inspectable by clinicians.

## Metadata
- **Published**: 2026-07-31T16:14:24Z
- **Authors**: Fabian Drexel, Marlene Fritzsche, Era Stambollxhiu, Miriam Kumpf, Lena Schmitzer, Lea Schumann, Jannik Kahmann, Friedrich Puttkammer, Johannes Moll, Jannik Lübberstedt, Zeineb Ben Chaaben, Anirudh Narayanan, Cosmin I. Bercea, Sebastian Ziegelmayer, Marcus R. Makowski, Daniel Rueckert, Lisa C. Adams, Keno K. Bressem
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00147v1)
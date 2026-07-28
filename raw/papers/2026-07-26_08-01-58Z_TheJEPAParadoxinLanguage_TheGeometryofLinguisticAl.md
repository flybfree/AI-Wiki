---
title: The JEPA Paradox in Language: The Geometry of Linguistic Alternatives
published: 2026-07-26T08:01:58Z
authors: Anh Trac Duc Dinh, Khang Nhat Hoang Vo
url: http://arxiv.org/abs/2607.23531v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The JEPA Paradox in Language: The Geometry of Linguistic Alternatives

## Abstract
Joint-Embedding Predictive Architectures (JEPAs) are effective for images, video, and audio, yet deterministic JEPA-style latent prediction has not become a standard objective for text encoders. We argue that this gap reflects a mismatch between squared-error latent prediction and the conditional structure of language. The key requirement is conditional concentration: given a context and target location, the target representation should lie near a single meaningful point. Local image prediction often satisfies this through spatial continuity, whereas masked text can admit multiple valid token or span completions whose representations need not share a coherent center. We formalize this mismatch through three conditions---predictability, non-collapse, and low conditional variance---and show how their failure creates centroid degeneracy and collapse pressure in text. Matched I-JEPA and T-JEPA experiments reveal the predicted sequence: mutual-information saturation and elevated target variance precede train--validation instability, effective-rank degeneration, cosine collapse, and poor downstream transfer. The same pattern appears across five independent data seeds, indicating that it is not a sampling artifact. These results do not rule out predictive learning for language; they show that text-compatible JEPA objectives must preserve multiple plausible completions rather than compress them into a single latent point.

## Metadata
- **Published**: 2026-07-26T08:01:58Z
- **Authors**: Anh Trac Duc Dinh, Khang Nhat Hoang Vo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23531v1)
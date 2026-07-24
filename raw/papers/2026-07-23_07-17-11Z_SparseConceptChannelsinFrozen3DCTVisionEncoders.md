---
title: Sparse Concept Channels in Frozen 3D CT Vision Encoders
published: 2026-07-23T07:17:11Z
authors: Farhad Nooralahzadeh, Lea Bogensperger, Christian Bluethgen, Michael Krauthammer
url: http://arxiv.org/abs/2607.20993v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sparse Concept Channels in Frozen 3D CT Vision Encoders

## Abstract
Large vision-language models are becoming increasingly dominant in 3D medical image interpretation, but we rarely know <i>which</i> internal units encode clinical findings or <i>where</i> that information lives in the representation. We first study this on a 3D chest vision-language model (Pillar-0) by probing its frozen vision embeddings. We show that (i) each radiological finding is encoded by a <i>sparse</i> set of ~10 vision-encoder channels that match full-feature classification performance and far exceed a zero-shot text prompting; (ii) turning off the channels tied to one finding, that finding's score collapses while unrelated labels stay stable; and (iii) the same sparse probe <i>replicates</i> on an architecturally unrelated 3D abdominal VLM (Merlin) suggesting a general property of frozen medical encoders. Our training-free concept channel probe (CCP) method, paired with a corpus-derived report template, outperforms published CT-CHAT on clinical efficacy and NLG metrics (F1 0.549 vs. 0.184; BLEU 0.483 vs. 0.373) at 22x lower latency. Our results provide a clear, reproducible characterization of how frozen medical encoders represent findings, demonstrating direct applicability across models.

## Metadata
- **Published**: 2026-07-23T07:17:11Z
- **Authors**: Farhad Nooralahzadeh, Lea Bogensperger, Christian Bluethgen, Michael Krauthammer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20993v1)
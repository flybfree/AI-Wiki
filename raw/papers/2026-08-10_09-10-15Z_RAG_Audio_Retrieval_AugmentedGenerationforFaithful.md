---
title: RAG-Audio: Retrieval-Augmented Generation for Faithful Brain-to-Audio Reconstruction
published: 2026-08-10T09:10:15Z
authors: Ambuj Mehrish, Sebastiano Vascon
url: http://arxiv.org/abs/2608.09331v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RAG-Audio: Retrieval-Augmented Generation for Faithful Brain-to-Audio Reconstruction

## Abstract
Brain-to-audio reconstruction is limited by \emph{prior domination}: when a pretrained generator is conditioned on a weak neural signal, it produces realistic but stimulus-inaccurate audio. We introduce RAG-Audio, which decodes fMRI into a semantic audio embedding, retrieves a matching real-audio exemplar, and initializes the frozen generator's sampling trajectory from that exemplar while retaining the decoded embedding as conditioning. On Brain2Music, RAG-Audio improves 10-way stimulus identification from $0.14$--$0.18$ for direct generation, near the $0.10$ chance level, to $0.40$--$0.43$, comparable to retrieval. It also reduces Fréchet Audio Distance by roughly an order of magnitude, from $13.49$ to $1.25$ for AudioLDM. RAG-Audio approaches nearest-neighbor retrieval in identification while remaining generative; its higher FAD is expected because retrieval directly replays real audio. An autoregressive negative control, which lacks an initializable latent trajectory, shows no comparable gain, attributing the improvement to trajectory initialization. These results suggest that retrieval-guided initialization can mitigate prior domination in brain-to-audio generation.

## Metadata
- **Published**: 2026-08-10T09:10:15Z
- **Authors**: Ambuj Mehrish, Sebastiano Vascon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09331v1)
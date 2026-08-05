---
title: LoopMTP: A looped transformer guided by latent multi-token prediction
published: 2026-08-04T13:13:09Z
authors: Behzad Shomali, Markus Frey, David Berghaus, Joachim Koehler, Mehdi Ali
url: http://arxiv.org/abs/2608.03624v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LoopMTP: A looped transformer guided by latent multi-token prediction

## Abstract
Looped transformers have emerged as a parameter-efficient alternative to scaling depth for strong reasoning. By reusing one stack of layers across $T$ iterations, they attain the effective depth and reasoning capabilities of larger models at a fixed parameter count. Yet existing approaches suffer from latent overthinking and undifferentiated computation, largely because intermediate representations receive no guidance across loops. Multi-token prediction (MTP) supplies exactly the dense, forward-looking supervision the loop is missing. We propose \textsc{LoopMTP}, which links the two through a structural correspondence in latent space: a model that loops $T$ times can anticipate $T$ future tokens. \textsc{LoopMTP} realizes this by softly aligning the hidden state of loop $t$ with the embedding of the token $t$ steps ahead, while a lightweight gate preserves useful information across iterations. \textsc{LoopMTP} improves average accuracy by up to 8.1\% (relative) over the non-looped baseline, with training remaining stable for up to 15 loops.

## Metadata
- **Published**: 2026-08-04T13:13:09Z
- **Authors**: Behzad Shomali, Markus Frey, David Berghaus, Joachim Koehler, Mehdi Ali
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03624v1)
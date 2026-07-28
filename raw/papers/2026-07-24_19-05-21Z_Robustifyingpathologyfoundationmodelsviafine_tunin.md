---
title: Robustifying pathology foundation models via fine-tuning
published: 2026-07-24T19:05:21Z
authors: Alexandre Filiot, Oskar Thaeter, Benoit Schmauch, Lionel Guillou
url: http://arxiv.org/abs/2607.22861v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robustifying pathology foundation models via fine-tuning

## Abstract
Pathology foundation models (FMs) produce powerful tile-level representations which remain sensitive to scanner and staining variability, undermining deployment across laboratories. We develop a novel fine-tuning recipe that improves the robustness of pathology FMs to acquisition factors. Applied to ten different FMs, our fine-tuning strategy consistently improves robustness for every model as well as downstream performance, with no observed trade-off. On average, it raises the PathoROB robustness index by 23% (from 0.72 to 0.87) and increases the overall cross-benchmark performance by 43% on Patho-Bench, HEST and THUNDER combined, with individual gains reaching up to 72% in robustness (Phikon-v2) and 76% in performance (Midnight-12k). We publicly release the fine-tuned versions of Phikon-v2 (Phaet) and Midnight-12k (Mascaret) at https://huggingface.co/wearewaiv/models.

## Metadata
- **Published**: 2026-07-24T19:05:21Z
- **Authors**: Alexandre Filiot, Oskar Thaeter, Benoit Schmauch, Lionel Guillou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22861v1)
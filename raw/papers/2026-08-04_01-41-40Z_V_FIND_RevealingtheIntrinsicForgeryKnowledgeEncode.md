---
title: V-FIND: Revealing the Intrinsic Forgery Knowledge Encoded in Video Forgery Detectors
published: 2026-08-04T01:41:40Z
authors: Shichao Kan, Chengpeng Hong, Jingtong Dou, Chuancheng Shi, Yuhan Liu, Linrui Xu, Yixiong Liang, Yigang Cen, Yanpeng Sun, Fei Shen, Tat-Seng Chua
url: http://arxiv.org/abs/2608.03008v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# V-FIND: Revealing the Intrinsic Forgery Knowledge Encoded in Video Forgery Detectors

## Abstract
As generated videos become increasingly realistic, reliable video forgery detection is increasingly important. Existing studies typically optimize and use video forgery detectors as black boxes, while the latent forgery-discriminative knowledge inside them remains largely unexplored. Instead of continuing to rely on resource-intensive full-model retraining to steadily improve detection performance, we ask whether video forgery detection can also be achieved by uncovering and activating sparse forensic knowledge within the detector. We find that forgery-discriminative knowledge is not uniformly distributed across the full representation space, but is concentrated in a sparse set of functionally specialized neurons. Based on this insight, we propose a video forgery-intrinsic neuron discovery (V-FIND) framework. V-FIND first localizes critical layers that exhibit pronounced discrepancies between real and forged videos, and then identifies latent anchor neurons that consistently carry forgery-discriminative signals, organizing them into a compact forensic subspace. With the original backbone frozen and only a lightweight linear classifier trained, this subspace still delivers strong detection performance across multiple external benchmarks for generated videos. Further neuron intervention experiments provide direct evidence for the functional specificity of the discovered neurons. Overall, these results suggest that video forgery detectors contain sparse, extractable, and reusable forgery-discriminative knowledge, offering a new perspective on understanding and exploiting their intrinsic forensic capability.

## Metadata
- **Published**: 2026-08-04T01:41:40Z
- **Authors**: Shichao Kan, Chengpeng Hong, Jingtong Dou, Chuancheng Shi, Yuhan Liu, Linrui Xu, Yixiong Liang, Yigang Cen, Yanpeng Sun, Fei Shen, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03008v1)